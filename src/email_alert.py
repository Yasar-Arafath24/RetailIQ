import smtplib
import os

from email.message import EmailMessage
from dotenv import load_dotenv


# ====================================
# LOAD ENV FILE FROM PROJECT ROOT
# ====================================

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

ENV_PATH = os.path.join(
    BASE_DIR,
    ".env"
)


load_dotenv(ENV_PATH)


# ====================================
# SEND STOCK ALERT EMAIL
# ====================================

def send_stock_alert(message):


    sender = os.getenv(
        "SENDER_EMAIL"
    )

    password = os.getenv(
        "APP_PASSWORD"
    )

    receiver = os.getenv(
        "RECEIVER_EMAIL"
    )


    print("======================")
    print("ENV CHECK")
    print("SENDER:", sender)
    print("PASSWORD:", password)
    print("RECEIVER:", receiver)
    print("======================")


    # ==========================
    # VALIDATION
    # ==========================

    if not sender:

        raise Exception(
            "SENDER_EMAIL missing in .env"
        )


    if not password:

        raise Exception(
            "APP_PASSWORD missing in .env"
        )


    if not receiver:

        raise Exception(
            "RECEIVER_EMAIL missing in .env"
        )


    # Remove spaces from Gmail app password

    password = password.replace(
        " ",
        ""
    )


    # ==========================
    # CREATE EMAIL
    # ==========================

    email = EmailMessage()


    email["From"] = sender

    email["To"] = receiver

    email["Subject"] = (
        "RetailIQ Critical Stock Alert"
    )


    email.set_content(
        message
    )


    # ==========================
    # SEND EMAIL
    # ==========================

    try:

        smtp = smtplib.SMTP_SSL(
            "smtp.gmail.com",
            465
        )


        smtp.login(
            sender,
            password
        )


        smtp.send_message(
            email
        )


        smtp.quit()


        print(
            "EMAIL SENT SUCCESSFULLY"
        )


        return True


    except Exception as e:


        print(
            "EMAIL ERROR:",
            e
        )


        raise e