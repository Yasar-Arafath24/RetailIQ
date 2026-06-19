from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle
)

from reportlab.lib.styles import getSampleStyleSheet

import os



def generate_pdf(
        filename,
        sales_data,
        inventory_data,
        forecast_data
):


    # create reports folder

    os.makedirs(
        "reports",
        exist_ok=True
    )


    path = os.path.join(
        "reports",
        filename
    )


    pdf = SimpleDocTemplate(
        path
    )


    styles = getSampleStyleSheet()


    content = []


    # ======================
    # TITLE
    # ======================

    title = Paragraph(
        "RetailIQ AI Inventory Report",
        styles["Title"]
    )


    content.append(
        title
    )


    content.append(
        Spacer(1,20)
    )


    # ======================
    # SALES SECTION
    # ======================


    content.append(
        Paragraph(
            "Sales Analytics",
            styles["Heading2"]
        )
    )


    sales_table = []


    sales_table.append(
        [
            "Product",
            "Units Sold"
        ]
    )


    for index,row in sales_data.iterrows():

        sales_table.append(
            [
                row.iloc[0],
                row.iloc[1]
            ]
        )


    table = Table(
        sales_table
    )


    table.setStyle(
        TableStyle(
            [
                ("GRID",(0,0),(-1,-1),1,None)
            ]
        )
    )


    content.append(
        table
    )


    content.append(
        Spacer(1,20)
    )



    # ======================
    # INVENTORY SECTION
    # ======================


    content.append(
        Paragraph(
            "Inventory Status",
            styles["Heading2"]
        )
    )


    inventory_table = []


    inventory_table.append(
        [
            "Product",
            "Stock",
            "Status"
        ]
    )


    for product,data in inventory_data.items():

        inventory_table.append(
            [
                product,
                data["Current Stock"],
                data["Status"]
            ]
        )


    table2 = Table(
        inventory_table
    )


    table2.setStyle(
        TableStyle(
            [
                ("GRID",(0,0),(-1,-1),1,None)
            ]
        )
    )


    content.append(
        table2
    )


    content.append(
        Spacer(1,20)
    )


    # ======================
    # FORECAST
    # ======================


    content.append(
        Paragraph(
            "Demand Forecast",
            styles["Heading2"]
        )
    )


    for product,demand in forecast_data.items():

        content.append(

            Paragraph(
                f"{product} : {demand} units predicted",
                styles["Normal"]
            )

        )


    pdf.build(
        content
    )


    return path