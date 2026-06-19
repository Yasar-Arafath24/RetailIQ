from src.inventory import get_inventory
from src.forecast import (
    forecast_product,
    predicted_demand
)

def analyze_risk(df):

    inventory = get_inventory()

    report = {}

    for product in inventory:

        current_stock = inventory[product]

        forecast = forecast_product(
            df,
            product,
            30
        )

        future_demand = predicted_demand(
            forecast
        )

        if current_stock >= future_demand:

            risk = "SAFE"

        elif current_stock >= (
            future_demand * 0.5
        ):

            risk = "WARNING"

        else:

            risk = "CRITICAL"

        report[product] = {

            "Current Stock":
            current_stock,

            "Forecast Demand":
            future_demand,

            "Risk":
            risk

        }

    return report