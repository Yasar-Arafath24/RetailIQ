def generate_purchase_order(risk_report):

    with open(
        "reports/purchase_order.txt",
        "w"
    ) as file:

        file.write(
            "PURCHASE ORDER REPORT\n"
        )

        file.write(
            "=" * 50 + "\n\n"
        )

        for product, data in risk_report.items():

            if data["Shortage"] > 0:

                file.write(
                    f"Product: {product}\n"
                )

                file.write(
                    f"Current Stock: "
                    f"{data['Current Stock']}\n"
                )

                file.write(
                    f"Predicted Demand: "
                    f"{data['Predicted Demand']}\n"
                )

                file.write(
                    f"Required Purchase: "
                    f"{data['Shortage']}\n"
                )

                file.write(
                    "-" * 40 + "\n"
                )

    print(
        "\nPurchase Order Generated Successfully!"
    )