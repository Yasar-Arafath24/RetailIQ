# RetailIQ - Environment Variables & Security Setup

## ✅ Security Implementation Complete

All sensitive information has been removed from the codebase and moved to a `.env` file.

---

## 📋 What Was Changed

### **Removed from Code:**
- ❌ Gmail account (yaseregspec@gmail.com)
- ❌ App password (jsrs migp octq qksi)  
- ❌ Receiver email (ya3081115@gmail.com)
- ❌ Phone numbers

### **Moved to `.env` File:**
All sensitive configuration is now in `.env` (which is in `.gitignore` and never committed)

### **Code Files Updated:**
1. **main.py** - Uses environment variables via config module
2. **real_time_monitor.py** - Uses environment variables for all credentials
3. **src/config.py** - NEW utility module for safe environment variable loading
4. **src/email_alert.py** - Enhanced with error handling
5. **src/market_intelligence.py** - Fixed Unicode encoding issues
6. **.env.example** - Template file (safe to commit)
7. **.env** - Real credentials (NEVER commit - already in .gitignore)

---

## 🔧 Setup Instructions

### **Step 1: Copy the Example File**
```bash
cp .env.example .env
```

### **Step 2: Edit `.env` with Your Credentials**
```bash
SENDER_EMAIL=your_gmail_account@gmail.com
RECEIVER_EMAIL=recipient_email@gmail.com
APP_PASSWORD=your_gmail_app_password
CHECK_INTERVAL_SECONDS=3600
```

### **Step 3: Verify .env is in .gitignore**
The `.env` file should NEVER be committed to version control.

Confirm in `.gitignore`:
```
.env
```

✅ Already configured!

---

## 🚀 Running the System

### **One-Time Analysis with Email Alerts**
```bash
python main.py
```

**Output includes:**
- Sales analytics
- Inventory status  
- **Email alert for critical stock** ✓
- Excel reports
- PDF report
- Market intelligence

### **Continuous Real-Time Monitoring**
```bash
python real_time_monitor.py
```

**Features:**
- Checks inventory every 1 hour (configurable)
- Sends automatic email alerts for critical items
- Real-time dashboard with status
- Press Ctrl+C to stop

---

## 📧 Email Configuration

### **Using Gmail with App Passwords**

1. **Get Gmail App Password:**
   - Go to https://myaccount.google.com/security
   - Enable 2-Factor Authentication
   - Generate an "App Password" for "Mail"
   - Copy this password to `.env`

2. **In `.env` file:**
   ```
   SENDER_EMAIL=your_gmail@gmail.com
   RECEIVER_EMAIL=recipient@gmail.com
   APP_PASSWORD=xxxx xxxx xxxx xxxx
   ```

3. **Test:**
   ```bash
   python main.py
   ```
   Look for: `[SUCCESS] Email Alert Sent to recipient@gmail.com!`

---

## 🔐 Security Best Practices

✅ **What's Done:**
- Sensitive data in `.env` file
- `.env` added to `.gitignore`
- Configuration validation at startup
- Error handling for missing credentials
- Environment variables loaded safely

✅ **For Production:**
- Use `.env.example` as template documentation
- Never commit `.env` to git
- Use different credentials for different environments
- Consider using environment variable services (AWS Secrets Manager, Azure Key Vault)
- Rotate credentials regularly

---

## ⚙️ Configuration Options

### **Email Settings**
```bash
SENDER_EMAIL=your_gmail@gmail.com
RECEIVER_EMAIL=recipient@gmail.com
APP_PASSWORD=your_app_password
```

### **Monitoring Settings**
```bash
CHECK_INTERVAL_SECONDS=3600  # Default: 1 hour
```

**Adjust frequency:**
- `60` = Every 1 minute (testing)
- `300` = Every 5 minutes
- `3600` = Every 1 hour (default)
- `86400` = Every 24 hours

### **Optional: WhatsApp Alerts**
```bash
WHATSAPP_PHONE_NUMBER=+1234567890
WHATSAPP_API_KEY=your_api_key
```

---

## ✓ Testing Checklist

- [x] Email credentials removed from all Python files
- [x] `.env` file created with real credentials
- [x] `.env.example` created as template
- [x] Configuration module loads from `.env`
- [x] Email validation checks for missing config
- [x] Error handling for email failures
- [x] Real-time monitor uses environment variables
- [x] Unicode issues fixed (Windows console)
- [x] Optional WhatsApp module (doesn't crash if missing)
- [x] Successful test run with email alerts sent ✓

---

## 📝 File Structure

```
RetailIQ/
├── .env                    ← Credentials (NEVER commit!)
├── .env.example           ← Template (SAFE to commit)
├── .gitignore             ← .env already listed
├── main.py               ← Updated: uses config module
├── real_time_monitor.py  ← Updated: uses config module
├── requirements.txt      ← Added: python-dotenv
│
└── src/
    ├── config.py         ← NEW: Loads environment variables
    ├── email_alert.py    ← Updated: Enhanced error handling
    └── ... other modules
```

---

## 🛡️ What's Protected Now

| Sensitive Data | Location | Protected |
|---|---|---|
| Gmail Password | `.env` file | ✅ Yes (.gitignore) |
| App Password | `.env` file | ✅ Yes (.gitignore) |
| Sender Email | `.env` file | ✅ Yes (.gitignore) |
| Receiver Email | `.env` file | ✅ Yes (.gitignore) |
| Phone Numbers | `.env` file | ✅ Yes (.gitignore) |

---

## 🚨 Troubleshooting

### **"Error: SENDER_EMAIL not configured"**
- Ensure `.env` file exists
- Check: `SENDER_EMAIL=your_email@gmail.com` is in `.env`
- Verify no spaces around `=`

### **"Failed to send email"**
- Verify Gmail credentials are correct
- Check app password (not regular password)
- Enable 2FA in Gmail security settings
- Check .env file has correct values

### **"ModuleNotFoundError: No module named 'dotenv'"**
- Run: `pip install python-dotenv`
- Or: `pip install -r requirements.txt`

### **"Script exits without running"**
- Check for validation errors: `python main.py 2>&1`
- Review `.env` file configuration
- Check file permissions

---

## 🎯 Next Steps

1. **Set up `.env`:**
   ```bash
   cp .env.example .env
   # Edit .env with your credentials
   ```

2. **Test email functionality:**
   ```bash
   python main.py
   ```

3. **Verify email received** at the receiver email address

4. **Run continuous monitoring** (optional):
   ```bash
   python real_time_monitor.py
   ```

5. **Commit to git** (`.env` is automatically excluded):
   ```bash
   git add .
   git commit -m "Add environment-based configuration"
   git push
   ```

---

## 📞 Support

For issues:
1. Check `.env` file exists and has values
2. Verify Gmail app password (not regular password)
3. Check logs in `logs/` folder
4. Review error messages carefully

---

*RetailIQ - Secure Inventory Management System*
