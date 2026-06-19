import pywhatkit
import datetime
import time
import os

from dotenv import load_dotenv


load_dotenv()



def send_whatsapp_alert(message):


    phone_number = os.getenv(
        "VENDOR_PHONE"
    )


    if not phone_number:

        raise Exception(
            "Vendor WhatsApp number missing"
        )


    now = datetime.datetime.now()


    hour = now.hour

    minute = now.minute + 1


    pywhatkit.sendwhatmsg(
        phone_number,
        message,
        hour,
        minute
    )


    time.sleep(5)


    return True