def generate_recommendation(
        product,
        current_stock,
        predicted_demand,
        status
):


    recommendations = []



    # Stock Risk

    if current_stock < predicted_demand:


        recommendations.append(

            f"{product} stock may become insufficient."

        )


        order_qty = (

            predicted_demand
            -
            current_stock

        )


        recommendations.append(

            f"Order approximately {order_qty} units."

        )



    else:


        recommendations.append(

            f"{product} inventory level is healthy."

        )



    # Status Check


    if status != "SAFE":


        recommendations.append(

            "Priority restocking required."

        )



    else:


        recommendations.append(

            "Continue monitoring."

        )



    return recommendations