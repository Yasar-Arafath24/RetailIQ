from src.load_data import load_sales_data

# Analytics
from src.analytics import (
    total_sales_per_product,
    best_selling_product,
    worst_selling_product,
    total_units_sold,
    daily_sales
)

# Inventory
from src.inventory import (
    check_inventory_status,
    calculate_reorder_quantity,
    get_inventory
)

# Visualization
from src.visualization import (
    plot_product_sales,
    plot_daily_sales,
    plot_product_share
)

# Forecasting
from src.forecast import (
    forecast_product,
    predicted_demand
)

# Stock Risk Analysis
from src.stock_predictor import (
    stock_risk_analysis
)
from src.purchase_order import (
    generate_purchase_order
)
from src.excel_reports import (
    generate_sales_report,
    generate_forecast_report,
    generate_inventory_report,
    generate_purchase_order_excel
)
from src.business_intelligence import (
    classify_products,
    high_demand_products,
    high_risk_products,
    generate_recommendations
)
from src.automation import (
    write_log,
    log_system_completion
)
from src.dashboard_summary import (
    generate_dashboard_summary
)
from src.pdf_report import (
    generate_pdf_report
)
from src.market_intelligence import (
    compare_prices
)
from src.email_alert import (
    send_stock_alert,
    send_daily_report
)
from src.whatsapp_alert import (
    send_whatsapp_alert
)
# ====================================
# EMAIL CONFIGURATION
# ====================================
SENDER_EMAIL = "yaseregspec@gmail.com"
RECEIVER_EMAIL = "ya3081115@gmail.com"
APP_PASSWORD = "jsrs migp octq qksi"

# ====================================
# LOAD DATA
# ====================================

df = load_sales_data()

# ====================================
# SALES ANALYTICS REPORT
# ====================================

print("\n" + "=" * 50)
print("SALES ANALYTICS REPORT")
print("=" * 50)

print("\nTotal Sales Per Product:")
print(total_sales_per_product(df))

print("\nTotal Units Sold:")
print(total_units_sold(df))

best_product, best_units = best_selling_product(df)

print("\nBest Selling Product:")
print(f"{best_product} ({best_units} units)")

worst_product, worst_units = worst_selling_product(df)

print("\nWorst Selling Product:")
print(f"{worst_product} ({worst_units} units)")

print("\nDaily Sales:")
print(daily_sales(df))

# ====================================
# INVENTORY REPORT
# ====================================

print("\n" + "=" * 50)
print("INVENTORY REPORT")
print("=" * 50)

inventory_report = check_inventory_status()

for product, details in inventory_report.items():

    print(f"\nProduct: {product}")
    print(f"Current Stock: {details['Current Stock']}")
    print(f"Minimum Stock: {details['Minimum Stock']}")
    print(f"Status: {details['Status']}")
    print("-" * 30)

# ====================================
# REORDER REPORT
# ====================================

print("\n" + "=" * 50)
print("REORDER REPORT")
print("=" * 50)

reorders = calculate_reorder_quantity()

if reorders:

    for product, qty in reorders.items():

        print(f"{product} → Order {qty} units")

else:

    print("No products require reordering.")

# ====================================
# CHART GENERATION
# ====================================

print("\n" + "=" * 50)
print("GENERATING CHARTS")
print("=" * 50)

plot_product_sales(df)
plot_daily_sales(df)
plot_product_share(df)

print("Charts generated successfully!")
print("Saved inside reports folder.")

# ====================================
# SINGLE PRODUCT FORECAST
# ====================================

print("\n" + "=" * 50)
print("MILK DEMAND FORECAST")
print("=" * 50)

forecast = forecast_product(
    df,
    "Milk",
    30
)

print(
    forecast[
        ["ds", "yhat"]
    ].tail(10)
)

future_demand = predicted_demand(
    forecast
)

print(
    f"\nPredicted Milk Demand for Next 30 Days: "
    f"{future_demand} units"
)

# ====================================
# MULTI PRODUCT FORECAST
# ====================================

print("\n" + "=" * 50)
print("ALL PRODUCT DEMAND FORECAST")
print("=" * 50)

products = df["Product"].unique()

forecast_results = {}

for product in products:

    forecast = forecast_product(
        df,
        product,
        30
    )

    demand = predicted_demand(
        forecast
    )

    forecast_results[product] = demand

    print(
        f"{product} → {demand} units"
    )

# ====================================
# FORECAST SUMMARY
# ====================================

print("\n" + "=" * 50)
print("FORECAST SUMMARY")
print("=" * 50)

print(forecast_results)

# ====================================
# STOCK RISK ANALYSIS
# ====================================

inventory_data = get_inventory()

risk_report = stock_risk_analysis(
    inventory_data,
    forecast_results
)

print("\n" + "=" * 50)
print("STOCK RISK REPORT")
print("=" * 50)

for product, data in risk_report.items():

    print(f"\nProduct: {product}")

    print(
        f"Current Stock: "
        f"{data['Current Stock']}"
    )

    print(
        f"Predicted Demand: "
        f"{data['Predicted Demand']}"
    )

    print(
        f"Shortage: "
        f"{data['Shortage']}"
    )

    print(
        f"Status: "
        f"{data['Status']}"
    )

    print("-" * 30)

print("\n" + "=" * 50)
print("SENDING EMAIL ALERTS")
print("=" * 50)

send_stock_alert(
    risk_report,
    SENDER_EMAIL,
    APP_PASSWORD,
    RECEIVER_EMAIL
)

print("\n" + "=" * 50)
print("RETAILIQ EXECUTION COMPLETED")
print("=" * 50)
# ====================================
# PURCHASE ORDER GENERATION
# ====================================

print("\n" + "=" * 50)
print("PURCHASE ORDER GENERATION")
print("=" * 50)

generate_purchase_order(
    risk_report
)
# ====================================
# EXCEL REPORT GENERATION
# ====================================

print("\n" + "=" * 50)
print("EXCEL REPORT GENERATION")
print("=" * 50)

generate_sales_report(df)

generate_inventory_report(
    inventory_report
)

generate_forecast_report(
    forecast_results
)

generate_purchase_order_excel(
    risk_report
)

print(
    "\nAll Excel Reports Generated!"
)
# ====================================
# BUSINESS INTELLIGENCE ENGINE
# ====================================

print("\n" + "=" * 50)
print("BUSINESS INTELLIGENCE")
print("=" * 50)

fast_moving, slow_moving = (
    classify_products(df)
)

high_demand = (
    high_demand_products(
        forecast_results
    )
)

high_risk = (
    high_risk_products(
        risk_report
    )
)

recommendations = (
    generate_recommendations(
        forecast_results,
        risk_report
    )
)

print("\nFAST MOVING PRODUCTS")
print(fast_moving)

print("\nSLOW MOVING PRODUCTS")
print(slow_moving)

print("\nHIGH DEMAND PRODUCTS")
print(high_demand)

print("\nHIGH RISK PRODUCTS")
print(high_risk)

print("\nAI RECOMMENDATIONS")

for recommendation in recommendations:

    print(
        f"• {recommendation}"
    )
write_log(
    "Sales data loaded successfully."
)
write_log(
    "Demand forecasting completed."
)
write_log(
    "Stock risk analysis completed."
)
write_log(
    "Purchase order generated."
)
log_system_completion()
# ====================================
# EXECUTIVE SUMMARY REPORT
# ====================================

generate_dashboard_summary(
    total_units_sold(df),
    best_product,
    worst_product,
    forecast_results,
    risk_report
)
generate_pdf_report(
    forecast_results,
    risk_report
)
print("\n" + "=" * 50)
print("MARKET INTELLIGENCE")
print("=" * 50)

compare_prices()

send_whatsapp_alert(
    risk_report,
    "+919952610449"
)
