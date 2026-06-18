import pywhatkit


def send_whatsapp_alert(
    risk_report,
    phone_number
):

    critical_products = []

    for product, data in risk_report.items():

        if data["Status"] == "CRITICAL":

            critical_products.append(

                f"{product}\n"
                f"Shortage: {data['Shortage']} units"

            )

    if not critical_products:

        print(
            "No critical products found."
        )

        return

    message = (
        "🚨 RetailIQ Alert 🚨\n\n"
        + "\n\n".join(
            critical_products
        )
        + "\n\nPurchase Order Required."
    )

    pywhatkit.sendwhatmsg_instantly(
        phone_number,
        message,
        wait_time=15,
        tab_close=True,
        close_time=3
    )

    print(
        "WhatsApp Alert Sent Successfully!"
    )