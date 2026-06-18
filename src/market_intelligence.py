def compare_prices():

    store_prices = {

        "Milk": 55,
        "Bread": 40,
        "Rice": 75

    }

    competitor_prices = {

        "Milk": 50,
        "Bread": 42,
        "Rice": 70

    }

    for product in store_prices:

        store_price = (
            store_prices[
                product
            ]
        )

        competitor_price = (
            competitor_prices[
                product
            ]
        )

        print(
            f"\n{product}"
        )

        print(
            f"Your Store: ₹{store_price}"
        )

        print(
            f"Competitor: ₹{competitor_price}"
        )

        if competitor_price < store_price:

            print(
                "Recommendation: "
                "Review pricing strategy."
            )

        else:

            print(
                "Pricing competitive."
            )