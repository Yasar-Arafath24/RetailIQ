from src.whatsapp_alert import send_whatsapp_alert


message = """
🚨 RetailIQ Alert

Milk shortage detected.

Current Stock:
100 units

Purchase order required.
"""


send_whatsapp_alert(
    message
)


print(
    "WhatsApp message sent"
)