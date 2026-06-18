def stock_risk_analysis(
    inventory_data,
    forecast_data
):

    report = {}

    for product in forecast_data:

        current_stock = inventory_data.get(
            product,
            0
        )

        predicted_demand = forecast_data[
            product
        ]

        shortage = (
            predicted_demand -
            current_stock
        )

        if shortage <= 0:

            status = "SAFE"

        elif shortage <= 100:

            status = "WARNING"

        else:

            status = "CRITICAL"

        report[product] = {

            "Current Stock":
                current_stock,

            "Predicted Demand":
                predicted_demand,

            "Shortage":
                shortage,

            "Status":
                status
        }

    return report