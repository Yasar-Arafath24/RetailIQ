from src.recommendation import generate_recommendation



result = generate_recommendation(

    "Milk",

    500,

    1087,

    "LOW STOCK"

)



for r in result:

    print(r)