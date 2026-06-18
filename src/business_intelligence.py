def classify_products(df):

    product_sales = (
        df.groupby("Product")
        ["Units_Sold"]
        .sum()
    )

    average_sales = (
        product_sales.mean()
    )

    fast_moving = []

    slow_moving = []

    for product, sales in product_sales.items():

        if sales >= average_sales:

            fast_moving.append(product)

        else:

            slow_moving.append(product)

    return (
        fast_moving,
        slow_moving
    )
    
#high demand products
def high_demand_products(
    forecast_results
):

    average_demand = (
        sum(
            forecast_results.values()
        )
        /
        len(
            forecast_results
        )
    )

    high_demand = []

    for product, demand in (
        forecast_results.items()
    ):

        if demand >= average_demand:

            high_demand.append(
                product
            )

    return high_demand
#high risk products
def high_risk_products(
    risk_report
):

    risky = []

    for product, data in (
        risk_report.items()
    ):

        if (
            data["Status"]
            == "CRITICAL"
        ):

            risky.append(
                product
            )

    return risky
#ai recommendations
def generate_recommendations(
    forecast_results,
    risk_report
):

    recommendations = []

    for product in forecast_results:

        demand = (
            forecast_results[
                product
            ]
        )

        status = (
            risk_report[
                product
            ]["Status"]
        )

        if status == "CRITICAL":

            recommendations.append(

                f"{product}: "
                f"Increase inventory "
                f"immediately."

            )

        elif status == "WARNING":

            recommendations.append(

                f"{product}: "
                f"Monitor stock closely."

            )

        else:

            recommendations.append(

                f"{product}: "
                f"Inventory level healthy."

            )

    return recommendations
