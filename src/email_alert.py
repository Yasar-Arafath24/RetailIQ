import smtplib
from email.message import EmailMessage
from datetime import datetime


def send_stock_alert(
    risk_report,
    sender_email,
    app_password,
    receiver_email
):
    """Send email alert for critical stock levels"""
    
    critical_products = []

    for product, data in (
        risk_report.items()
    ):

        if (
            data["Status"]
            ==
            "CRITICAL"
        ):

            critical_products.append(

                f"{product} shortage: "
                f"{data['Shortage']} units"

            )

    if not critical_products:

        print(
            "No critical stock alerts."
        )

        return False

    try:
        msg = EmailMessage()

        msg["Subject"] = (
            "RetailIQ Critical Stock Alert - "
            f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        )

        msg["From"] = sender_email

        msg["To"] = receiver_email

        email_body = (
            "CRITICAL STOCK ALERT\n"
            "=" * 50 + "\n\n"
            "The following products have critical shortage:\n\n"
            + "\n".join(critical_products)
            + "\n\n" + "=" * 50 + "\n"
            + f"Alert Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
            + "RetailIQ Inventory Management System"
        )

        msg.set_content(email_body)

        with smtplib.SMTP_SSL(
            "smtp.gmail.com",
            465
        ) as smtp:

            smtp.login(
                sender_email,
                app_password
            )

            smtp.send_message(msg)

        print(
            f"[SUCCESS] Email Alert Sent to {receiver_email}!"
        )
        
        return True
        
    except Exception as e:
        print(
            f"[ERROR] Failed to send email: {str(e)}"
        )
        return False


def send_daily_report(
    sender_email,
    app_password,
    receiver_email,
    report_content
):
    """Send daily inventory report email"""
    
    try:
        msg = EmailMessage()

        msg["Subject"] = (
            f"RetailIQ Daily Report - "
            f"{datetime.now().strftime('%Y-%m-%d')}"
        )

        msg["From"] = sender_email

        msg["To"] = receiver_email

        msg.set_content(report_content)

        with smtplib.SMTP_SSL(
            "smtp.gmail.com",
            465
        ) as smtp:

            smtp.login(
                sender_email,
                app_password
            )

            smtp.send_message(msg)

        print(
            f"[SUCCESS] Daily Report Sent to {receiver_email}!"
        )
        
        return True
        
    except Exception as e:
        print(
            f"[ERROR] Failed to send report: {str(e)}"
        )
        return False
