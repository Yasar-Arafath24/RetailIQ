def compare_price(
        your_price,
        competitor_price
):


    difference = (
        your_price -
        competitor_price
    )


    if difference > 0:


        recommendation = (

            "Your price is higher. "
            "Consider discount strategy."

        )


    elif difference < 0:


        recommendation = (

            "Your price is competitive."

        )


    else:


        recommendation = (

            "Price matches market."

        )



    return {

        "Difference":
        difference,

        "Recommendation":
        recommendation

    }