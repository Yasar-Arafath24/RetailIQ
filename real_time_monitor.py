"""
Real-Time Inventory Monitoring System
Continuously monitors stock levels and sends email alerts for critical items
"""

import schedule
import time
from datetime import datetime

from src.load_data import load_sales_data
from src.inventory import (
    check_inventory_status,
    get_inventory
)
from src.forecast import forecast_product, predicted_demand
from src.stock_predictor import stock_risk_analysis
from src.email_alert import send_stock_alert
from src.config import (
    validate_email_config,
    get_email_config,
    CHECK_INTERVAL_SECONDS
)

# ====================================
# EMAIL CONFIGURATION
# ====================================
if not validate_email_config():
    print("\n[ERROR] Email configuration error. Please check your .env file.")
    print("Copy .env.example to .env and fill in your credentials.")
    exit(1)

email_config = get_email_config()
SENDER_EMAIL = email_config["sender_email"]
RECEIVER_EMAIL = email_config["receiver_email"]
APP_PASSWORD = email_config["app_password"]

# ====================================
# MONITORING FREQUENCY (in seconds)
# ====================================
CHECK_INTERVAL = CHECK_INTERVAL_SECONDS  # From .env file

def run_inventory_check():
    """
    Run a complete inventory check and send alerts if needed
    """
    
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"\n{'='*60}")
    print(f"REAL-TIME INVENTORY CHECK - {timestamp}")
    print(f"{'='*60}")
    
    try:
        # Load latest sales data
        df = load_sales_data()
        
        # Get current inventory status
        inventory_report = check_inventory_status()
        
        # Get inventory data for forecasting
        inventory_data = get_inventory()
        
        # Get all products
        products = df["Product"].unique()
        
        # Forecast for all products
        forecast_results = {}
        for product in products:
            try:
                forecast = forecast_product(
                    df,
                    product,
                    30
                )
                demand = predicted_demand(forecast)
                forecast_results[product] = demand
            except Exception as e:
                print(f"Warning: Could not forecast {product}: {str(e)}")
                forecast_results[product] = 0
        
        # Perform stock risk analysis
        risk_report = stock_risk_analysis(
            inventory_data,
            forecast_results
        )
        
        # Print current status
        print("\nCurrent Inventory Status:")
        critical_count = 0
        for product, data in risk_report.items():
            status = data['Status']
            if status == "CRITICAL":
                critical_count += 1
                print(f"  [CRITICAL] {product}: {status} (Shortage: {data['Shortage']} units)")
            elif status == "WARNING":
                print(f"  [WARNING] {product}: {status} (Stock: {data['Current Stock']} units)")
            else:
                print(f"  [OK] {product}: {status}")
        
        print(f"\nTotal Critical Items: {critical_count}")
        
        # Send email alert if there are critical items
        if critical_count > 0:
            print("\n" + "="*60)
            print("SENDING EMAIL ALERTS")
            print("="*60)
            send_stock_alert(
                risk_report,
                SENDER_EMAIL,
                APP_PASSWORD,
                RECEIVER_EMAIL
            )
        else:
            print("\n[OK] No critical alerts - inventory levels are healthy")
        
        print(f"\nNext check scheduled for: ", end="")
        
    except Exception as e:
        print(f"\n[ERROR] Error during inventory check: {str(e)}")
        print("Attempting to send alert email about the error...")
        
        error_msg = f"""
        ERROR OCCURRED DURING INVENTORY CHECK
        
        Time: {timestamp}
        Error: {str(e)}
        
        Please check the system logs for more details.
        
        RetailIQ Real-Time Monitoring System
        """
        
        try:
            send_stock_alert(
                {"System Error": {"Status": "CRITICAL", "Shortage": 0}},
                SENDER_EMAIL,
                APP_PASSWORD,
                RECEIVER_EMAIL
            )
        except:
            pass


def schedule_monitoring(interval_seconds=CHECK_INTERVAL):
    """
    Schedule the inventory check to run at regular intervals
    
    Args:
        interval_seconds: Time between checks in seconds (default: 3600 = 1 hour)
    """
    
    # Calculate interval in minutes for display
    interval_minutes = interval_seconds // 60
    
    print(f"\n{'='*60}")
    print("REAL-TIME INVENTORY MONITORING STARTED")
    print(f"{'='*60}")
    print(f"Check Interval: Every {interval_minutes} minute(s)")
    print(f"Sender: {SENDER_EMAIL}")
    print(f"Receiver: {RECEIVER_EMAIL}")
    print(f"\nPress Ctrl+C to stop monitoring")
    print(f"{'='*60}\n")
    
    # Schedule the job
    schedule.every(interval_seconds).seconds.do(run_inventory_check)
    
    # Run the first check immediately
    run_inventory_check()
    
    # Keep the scheduler running
    while True:
        try:
            schedule.run_pending()
            time.sleep(1)
        except KeyboardInterrupt:
            print(f"\n\n{'='*60}")
            print("MONITORING STOPPED BY USER")
            print(f"{'='*60}")
            break
        except Exception as e:
            print(f"\nScheduler error: {str(e)}")
            time.sleep(5)


if __name__ == "__main__":
    # Start monitoring with 1-hour intervals
    # Change CHECK_INTERVAL above for different frequencies
    schedule_monitoring(CHECK_INTERVAL)
