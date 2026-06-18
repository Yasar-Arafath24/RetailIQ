"""
Configuration module for loading environment variables
Handles email credentials and other settings securely
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Email Configuration
SENDER_EMAIL = os.getenv("SENDER_EMAIL")
RECEIVER_EMAIL = os.getenv("RECEIVER_EMAIL")
APP_PASSWORD = os.getenv("APP_PASSWORD")

# Monitoring Settings
CHECK_INTERVAL_SECONDS = int(
    os.getenv("CHECK_INTERVAL_SECONDS", "3600")
)

# WhatsApp Configuration (optional)
WHATSAPP_PHONE_NUMBER = os.getenv("WHATSAPP_PHONE_NUMBER")
WHATSAPP_API_KEY = os.getenv("WHATSAPP_API_KEY")


def validate_email_config():
    """
    Validate that all required email configuration is present
    Returns: True if valid, False otherwise
    """
    if not SENDER_EMAIL:
        print("✗ Error: SENDER_EMAIL not configured in .env")
        return False
    if not RECEIVER_EMAIL:
        print("✗ Error: RECEIVER_EMAIL not configured in .env")
        return False
    if not APP_PASSWORD:
        print("✗ Error: APP_PASSWORD not configured in .env")
        return False
    
    return True


def get_email_config():
    """
    Get email configuration dictionary
    Returns: Dict with sender_email, receiver_email, app_password
    """
    return {
        "sender_email": SENDER_EMAIL,
        "receiver_email": RECEIVER_EMAIL,
        "app_password": APP_PASSWORD,
    }
