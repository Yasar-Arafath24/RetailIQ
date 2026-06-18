# RetailIQ Email Automation - Usage Guide

## Overview
Your RetailIQ system is now configured with **real-time email automation** that sends alerts when critical stock shortages are detected.

---

## Email Configuration
- **Sender Email:** yaseregspec@gmail.com
- **Receiver Email:** ya3081115@gmail.com
- **Alert Type:** Critical stock shortages

---

## Two Ways to Run the System

### **Option 1: One-Time Full Analysis (with Email Alerts)**

Run the complete analysis pipeline once with automatic email alerts:

```bash
python main.py
```

**What it does:**
- ✓ Loads and analyzes sales data
- ✓ Generates forecasts for all products
- ✓ Performs stock risk analysis
- ✓ **Sends email alert for any CRITICAL stock levels**
- ✓ Generates Excel reports
- ✓ Generates PDF report with insights
- ✓ Provides market intelligence recommendations

**Time:** ~2-3 minutes to complete

**When to use:** Running daily or when you need a complete report

---

### **Option 2: Real-Time Continuous Monitoring**

Run continuous monitoring that checks inventory every hour and sends automatic alerts:

```bash
python real_time_monitor.py
```

**What it does:**
- ✓ Checks inventory status every 1 hour
- ✓ Forecasts demand for all products
- ✓ Performs stock risk analysis
- ✓ **Automatically sends email if critical items detected**
- ✓ Shows real-time status dashboard
- ✓ Continues running indefinitely until stopped

**To customize check interval:**
Edit `real_time_monitor.py` line 28:
```python
CHECK_INTERVAL = 3600  # seconds (1 hour)
# For testing: use 60 for every 1 minute
```

**To stop monitoring:**
Press `Ctrl+C` in the terminal

**When to use:** 24/7 inventory monitoring for active operations

---

## Email Alert Details

### Alert Triggers
The system sends an email when any product has:
- **CRITICAL status** = Predicted shortage within 30 days

### What's in the Alert Email
```
CRITICAL STOCK ALERT
==================================================

The following products have critical shortage:

Product Name shortage: X units
Product Name shortage: Y units

==================================================
Alert Time: 2026-06-18 20:38:21
RetailIQ Inventory Management System
```

---

## Test the Email System

### Quick Test - Run Main Script
```bash
python main.py
```
This will immediately analyze current inventory and send alerts if any products are critical.

### Quick Test - Run Monitor for Testing
Edit `real_time_monitor.py` to check every 1 minute:
```python
CHECK_INTERVAL = 60  # Check every minute instead of 1 hour
```

Then run:
```bash
python real_time_monitor.py
```

---

## Important Notes

1. **Gmail App Password:** The password provided (jsrs migp octq qksi) is a Google App Password, NOT your regular Gmail password. This is more secure.

2. **Security:** The credentials are currently in the code. For production, consider:
   - Using environment variables
   - Using a config file with restricted permissions
   - Using Gmail's OAuth2 instead of app passwords

3. **Email Delivery:** Emails may take 30 seconds - 2 minutes to arrive

4. **No Duplicate Alerts:** Each run only sends one email per critical product

5. **Log Files:** System logs are saved in the `logs/` folder

---

## Troubleshooting

### "Email not sending"
- Check internet connection
- Verify sender email: yaseregspec@gmail.com
- Verify app password is correct
- Check if Gmail has blocked the app (check Google Account security settings)

### "Real-time monitor crashes"
- Ensure all dependencies are installed: `pip install -r requirements.txt`
- Check logs folder for error details
- Try running `python main.py` first to test basic functionality

### "No alerts being sent"
- Confirm there are actually critical stock levels
- Check if CRITICAL products appear in the "STOCK RISK REPORT" section
- Review inventory data in `data/sales.csv`

---

## Example Execution Flow

**When you run `python main.py`:**

1. Load sales data from `data/sales.csv`
2. Analyze historical sales
3. Forecast demand for next 30 days
4. Compare forecasted demand vs current stock
5. Mark products as CRITICAL if shortage detected
6. **Send email alert** ← NEW!
7. Generate Excel and PDF reports
8. Provide recommendations

---

## System Status

✅ Email automation configured and tested
✅ Gmail SMTP connection working
✅ Alerts sending to ya3081115@gmail.com
✅ Real-time monitoring script ready
✅ All dependencies installed

---

## Next Steps

1. **Run full analysis:** `python main.py`
2. **Monitor continuously:** `python real_time_monitor.py`
3. **Check received emails** at ya3081115@gmail.com
4. **Adjust alert frequency** as needed

---

*RetailIQ - Real-Time Inventory Management System*
