from datetime import datetime


def generate_dashboard_summary(
    total_units,
    best_product,
    worst_product,
    forecast_results,
    risk_report
):

    with open(
        "reports/dashboard_summary.txt",
        "w"
    ) as file:

        file.write(
            "=" * 40 + "\n"
        )

        file.write(
            "RETAILIQ EXECUTIVE SUMMARY\n"
        )

        file.write(
            "=" * 40 + "\n\n"
        )

        file.write(
            f"Execution Date:\n"
        )

        file.write(
            f"{datetime.now()}\n\n"
        )

        file.write(
            "-" * 40 + "\n"
        )

        file.write(
            "SALES OVERVIEW\n"
        )

        file.write(
            "-" * 40 + "\n\n"
        )

        file.write(
            f"Total Units Sold:\n"
        )

        file.write(
            f"{total_units}\n\n"
        )

        file.write(
            f"Best Selling Product:\n"
        )

        file.write(
            f"{best_product}\n\n"
        )

        file.write(
            f"Worst Selling Product:\n"
        )

        file.write(
            f"{worst_product}\n\n"
        )

        file.write(
            "-" * 40 + "\n"
        )

        file.write(
            "FORECAST OVERVIEW\n"
        )

        file.write(
            "-" * 40 + "\n\n"
        )

        for product, demand in forecast_results.items():

            file.write(
                f"{product}: {demand} units\n"
            )

        file.write("\n")

        file.write(
            "-" * 40 + "\n"
        )

        file.write(
            "HIGH RISK PRODUCTS\n"
        )

        file.write(
            "-" * 40 + "\n\n"
        )

        for product, data in risk_report.items():

            if data["Status"] == "CRITICAL":

                file.write(
                    f"{product}\n"
                )

        file.write("\n")

        file.write(
            "-" * 40 + "\n"
        )

        file.write(
            "PURCHASE ORDERS REQUIRED\n"
        )

        file.write(
            "-" * 40 + "\n\n"
        )

        for product, data in risk_report.items():

            if data["Shortage"] > 0:

                file.write(
                    f"{product}: "
                    f"{data['Shortage']} units\n"
                )

        file.write("\n")

        file.write(
            "-" * 40 + "\n"
        )

        file.write(
            "SYSTEM STATUS\n"
        )

        file.write(
            "-" * 40 + "\n\n"
        )

        file.write(
            "Sales Analysis Completed\n"
        )

        file.write(
            "Forecasting Completed\n"
        )

        file.write(
            "Risk Analysis Completed\n"
        )

        file.write(
            "Reports Generated\n\n"
        )

        file.write(
            "=" * 40 + "\n"
        )

        file.write(
            "END OF REPORT\n"
        )

        file.write(
            "=" * 40 + "\n"
        )

    print(
        "\nExecutive Summary Generated!"
    )