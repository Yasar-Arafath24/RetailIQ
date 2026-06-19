from src.pdf_report import generate_pdf


sales = {
    "Product": [
        "Milk",
        "Bread"
    ],

    "Units": [
        500,
        300
    ]
}


import pandas as pd


sales_df = pd.DataFrame(
    sales
)


inventory = {

    "Milk":
    {
        "Current Stock":500,
        "Status":"SAFE"
    },

    "Bread":
    {
        "Current Stock":100,
        "Status":"LOW STOCK"
    }

}


forecast = {

    "Milk":1087,
    "Bread":840

}



generate_pdf(
    "RetailIQ_Report.pdf",
    sales_df,
    inventory,
    forecast
)


print(
    "PDF Generated"
)