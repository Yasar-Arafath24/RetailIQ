import streamlit as st
import plotly.express as px


# ====================================
# IMPORT RETAILIQ MODULES
# ====================================

from src.load_data import load_sales_data

from src.analytics import (
    total_units_sold,
    best_selling_product,
    worst_selling_product,
    total_sales_per_product,
    daily_sales
)
from src.inventory import (
    check_inventory_status
)
from src.forecast import (
    forecast_product,
    predicted_demand
)
from src.inventory import (
    calculate_reorder_quantity
)
from src.email_alert import (
    send_stock_alert
)
from src.whatsapp_alert import (
    send_whatsapp_alert
)
from src.whatsapp_alert import (
    send_whatsapp_alert
)

from src.pdf_report import (
    generate_pdf
)
from src.price_analysis import (
    compare_price
)
from src.recommendation import (
    generate_recommendation
)
# ====================================
# PAGE CONFIG
# ====================================

st.set_page_config(
    page_title="RetailIQ",
    page_icon="📦",
    layout="wide"
)
from src.risk_analysis import (
    analyze_risk
)
# ====================================
# LOAD DATA
# ====================================

df = load_sales_data()

# ====================================
# CALCULATE METRICS
# ====================================

total_units = total_units_sold(df)

best_product, best_units = best_selling_product(df)

worst_product, worst_units = worst_selling_product(df)

total_products = df["Product"].nunique()

sales_summary = total_sales_per_product(df)

daily_sales_data = daily_sales(df)

# ====================================
# AUTO DETECT COLUMN NAMES
# ====================================

# Debug: Check what types we're getting
# st.write(f"sales_summary type: {type(sales_summary)}")
# st.write(f"daily_sales_data type: {type(daily_sales_data)}")

# Handle both Series and DataFrames
if hasattr(sales_summary, 'columns'):
    # It's a DataFrame
    sales_col1 = sales_summary.columns[0]
    sales_col2 = sales_summary.columns[1]
else:
    # It's a Series - convert to DataFrame
    sales_summary = sales_summary.reset_index()
    sales_summary.columns = ['Product', 'Units_Sold']
    sales_col1 = sales_summary.columns[0]
    sales_col2 = sales_summary.columns[1]

if hasattr(daily_sales_data, 'columns'):
    # It's a DataFrame
    daily_col1 = daily_sales_data.columns[0]
    daily_col2 = daily_sales_data.columns[1]
else:
    # It's a Series - convert to DataFrame
    daily_sales_data = daily_sales_data.reset_index()
    daily_sales_data.columns = ['Date', 'Units_Sold']
    daily_col1 = daily_sales_data.columns[0]
    daily_col2 = daily_sales_data.columns[1]

# ====================================
# SIDEBAR
# ====================================

st.sidebar.title("📦 RetailIQ")

st.sidebar.success(
    "RetailIQ v1.0"
)

st.sidebar.info(
    "AI-Powered Inventory Intelligence"
)

page = st.sidebar.selectbox(
    "Navigation",
    [
        "Home",
        "Sales Analytics",
        "Inventory",
        "Forecasting",
        "Risk Analysis",
        "Purchase Orders",
        "Business Intelligence",
        "Reports"
    ]
)

# ====================================
# HOME PAGE
# ====================================

if page == "Home":

    st.title("📦 RetailIQ Dashboard")

    st.markdown("""
    ### AI-Powered Inventory Forecasting &
    Business Intelligence System
    """)

    st.divider()

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Products",
            total_products
        )

    with col2:
        st.metric(
            "Units Sold",
            total_units
        )

    with col3:
        st.metric(
            "Best Product",
            best_product
        )

    with col4:
        st.metric(
            "Worst Product",
            worst_product
        )

    st.divider()

    st.subheader("📋 Sales Dataset")

    st.dataframe(
        df,
        use_container_width=True
    )

    st.divider()

    st.subheader("📊 Sales Summary")

    st.dataframe(
        sales_summary,
        use_container_width=True
    )

# ====================================
# SALES ANALYTICS PAGE
# ====================================

elif page == "Sales Analytics":

    st.title(
        "📊 Sales Analytics Dashboard"
    )

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Top Product",
            best_product
        )

    with col2:
        st.metric(
            "Total Units Sold",
            total_units
        )

    st.divider()

    st.subheader(
        "📋 Product Sales Summary"
    )

    st.dataframe(
        sales_summary,
        use_container_width=True
    )

    st.divider()

    # BAR CHART

    st.subheader(
        "📦 Product Sales"
    )

    bar_chart = px.bar(
        sales_summary,
        x=sales_col1,
        y=sales_col2,
        title="Product Sales Analysis"
    )

    st.plotly_chart(
        bar_chart,
        use_container_width=True
    )

    st.divider()

    # PIE CHART

    st.subheader(
        "🥧 Product Share"
    )

    pie_chart = px.pie(
        sales_summary,
        names=sales_col1,
        values=sales_col2,
        title="Product Share"
    )

    st.plotly_chart(
        pie_chart,
        use_container_width=True
    )

    st.divider()

    # LINE CHART

    st.subheader(
        "📈 Daily Sales Trend"
    )

    trend_chart = px.line(
        daily_sales_data,
        x=daily_col1,
        y=daily_col2,
        markers=True,
        title="Daily Sales Trend"
    )

    st.plotly_chart(
        trend_chart,
        use_container_width=True
    )

# ====================================
# INVENTORY PAGE
# ====================================

elif page == "Inventory":

    st.title(
        "📦 Inventory Monitoring Dashboard"
    )

    inventory_report = check_inventory_status()

    import pandas as pd

    inventory_df = pd.DataFrame(
        inventory_report
    ).T

    inventory_df.reset_index(
        inplace=True
    )

    inventory_df.rename(
        columns={
            "index": "Product"
        },
        inplace=True
    )

    # ==========================
    # KPI CARDS
    # ==========================

    total_products_inventory = len(
        inventory_df
    )

    critical_items = len(
        inventory_df[
            inventory_df["Status"] != "SAFE"
        ]
    )

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Products Monitored",
            total_products_inventory
        )

    with col2:
        st.metric(
            "Low Stock Products",
            critical_items
        )

    st.divider()

    # ==========================
    # INVENTORY TABLE
    # ==========================

    st.subheader(
        "📋 Inventory Status"
    )

    st.dataframe(
        inventory_df,
        use_container_width=True
    )

    st.divider()

    # ==========================
    # INVENTORY CHART
    # ==========================

    st.subheader(
        "📊 Current Inventory Levels"
    )

    inventory_chart = px.bar(
        inventory_df,
        x="Product",
        y="Current Stock",
        title="Current Inventory Levels"
    )

    st.plotly_chart(
        inventory_chart,
        use_container_width=True
    )

    st.divider()

    # ==========================
    # STATUS ALERTS
    # ==========================

    st.subheader(
        "🚨 Stock Alerts"
    )

    for _, row in inventory_df.iterrows():

        product = row["Product"]
        status = row["Status"]

        if status == "SAFE":

            st.success(
                f"{product} → {status}"
            )

        elif status == "WARNING":

            st.warning(
                f"{product} → {status}"
            )

        else:

            st.error(
                f"{product} → {status}"
            )

    for _, row in inventory_df.iterrows():

        product = row["Product"]

        status = row["Status"]

        if status == "OK":

            st.success(
                f"{product} → {status}"
            )

        else:

            st.error(
                f"{product} → {status}"
            )

# ====================================
# FORECASTING PAGE
# ====================================

elif page == "Forecasting":

    st.title(
        "📈 AI Demand Forecasting"
    )

    st.markdown(
        """
        Forecast future product demand
        using Machine Learning.
        """
    )

    st.divider()

    products = df["Product"].unique()

    selected_product = st.selectbox(
        "Select Product",
        products
    )

    forecast_days = st.slider(
        "Forecast Days",
        min_value=7,
        max_value=90,
        value=30
    )

    st.divider()

    with st.spinner(
        "Generating Forecast..."
    ):

        forecast = forecast_product(
            df,
            selected_product,
            forecast_days
        )

        demand = predicted_demand(
            forecast
        )

    # ==========================
    # KPI CARD
    # ==========================

    st.metric(
        "Predicted Demand",
        f"{demand} Units"
    )

    st.divider()

    # ==========================
    # FORECAST CHART
    # ==========================

    forecast_chart = px.line(
        forecast,
        x="ds",
        y="yhat",
        title=f"{selected_product} Demand Forecast"
    )

    st.plotly_chart(
        forecast_chart,
        use_container_width=True
    )

    st.divider()

    # ==========================
    # FORECAST TABLE
    # ==========================

    st.subheader(
        "Forecast Data"
    )

    st.dataframe(
        forecast[
            ["ds", "yhat"]
        ].tail(
            forecast_days
        ),
        use_container_width=True
    )

# ====================================
# RISK ANALYSIS PAGE
# ====================================

elif page == "Risk Analysis":

    st.title(
        "⚠️ Inventory Risk Analysis"
    )

    risk_report = analyze_risk(
        df
    )

    import pandas as pd

    risk_df = pd.DataFrame(
        risk_report
    ).T

    risk_df.reset_index(
        inplace=True
    )

    risk_df.rename(
        columns={
            "index":
            "Product"
        },
        inplace=True
    )

    st.dataframe(
        risk_df,
        use_container_width=True
    )

    st.divider()

    for _, row in risk_df.iterrows():

        product = row["Product"]

        risk = row["Risk"]

        if risk == "SAFE":

            st.success(
                f"{product} → SAFE"
            )

        elif risk == "WARNING":

            st.warning(
                f"{product} → WARNING"
            )

        else:

            st.error(
                f"{product} → CRITICAL"
            )

# ====================================
# PURCHASE ORDERS PAGE
# ====================================

elif page == "Purchase Orders":

    st.title(
        "🛒 Smart Purchase Orders"
    )

    orders = calculate_reorder_quantity()

    if len(orders) == 0:

        st.success(
            "No products require reordering."
        )

    else:

        import pandas as pd

        po_df = pd.DataFrame(
            list(orders.items()),
            columns=[
                "Product",
                "Order Quantity"
            ]
        )

        st.dataframe(
            po_df,
            use_container_width=True
        )

        st.divider()

        st.subheader(
            "Generated Purchase Orders"
        )

        for _, row in po_df.iterrows():

            st.warning(
                f"Order {row['Order Quantity']} units of {row['Product']}"
            )

        csv = po_df.to_csv(
            index=False
        )
        po_df.to_csv(
    "reports/purchase_orders.csv",
    index=False
        )


        st.download_button(
            label="⬇ Download Purchase Order CSV",
            data=csv,
            file_name="purchase_orders.csv",
            mime="text/csv"
        )

# ====================================
# BUSINESS INTELLIGENCE PAGE
# ====================================
# ====================================
# BUSINESS INTELLIGENCE PAGE
# ====================================
# ====================================
# BUSINESS INTELLIGENCE PAGE
# ====================================
# ====================================
# BUSINESS INTELLIGENCE PAGE
# ====================================

elif page == "Business Intelligence":


    st.title(
        "🧠 RetailIQ Business Intelligence"
    )


    st.markdown(
        """
        AI Decision System + Competitor Market Analysis
        """
    )


    st.divider()



    # =================================
    # PART 1
    # COMPETITOR PRICE INTELLIGENCE
    # =================================


    st.subheader(
        "💰 Competitor Price Intelligence"
    )


    store_prices = {


        "Milk":55,

        "Bread":40,

        "Rice":70

    }



    competitor_prices = {


        "Milk":50,

        "Bread":45,

        "Rice":70

    }



    selected_product = st.selectbox(

        "Select Product",

        list(store_prices.keys())

    )



    your_price = store_prices[
        selected_product
    ]


    competitor_price = competitor_prices[
        selected_product
    ]



    col1,col2,col3 = st.columns(3)



    with col1:


        st.metric(

            "Your Store Price",

            f"₹{your_price}"

        )



    with col2:


        st.metric(

            "Competitor Price",

            f"₹{competitor_price}"

        )



    with col3:


        difference = (

            your_price -
            competitor_price

        )


        st.metric(

            "Difference",

            f"₹{difference}"

        )



    price_result = compare_price(

        your_price,

        competitor_price

    )



    if difference > 0:


        st.warning(

            price_result["Recommendation"]

        )


    elif difference < 0:


        st.success(

            price_result["Recommendation"]

        )


    else:


        st.info(

            price_result["Recommendation"]

        )



    st.divider()



    # =================================
    # PART 2
    # AI RECOMMENDATION ENGINE
    # =================================



    st.subheader(

        "🤖 AI Inventory Recommendation"

    )



    inventory_report = (
        check_inventory_status()
    )


    products = df["Product"].unique()



    for product in products:



        st.markdown(
            f"### 📦 {product}"
        )



        current_stock = (

            inventory_report
            [product]
            ["Current Stock"]

        )



        status = (

            inventory_report
            [product]
            ["Status"]

        )



        forecast = forecast_product(

            df,

            product,

            30

        )



        predicted = predicted_demand(

            forecast

        )



        c1,c2,c3 = st.columns(3)



        with c1:


            st.metric(

                "Current Stock",

                current_stock

            )



        with c2:


            st.metric(

                "30 Day Demand",

                predicted

            )



        with c3:


            st.metric(

                "Inventory Status",

                status

            )



        recommendations = generate_recommendation(

            product,

            current_stock,

            predicted,

            status

        )



        for rec in recommendations:


            if (
                "Order" in rec
                or
                "Priority" in rec
            ):


                st.warning(rec)


            else:


                st.success(rec)



        st.divider()
# ====================================
# REPORTS PAGE
# ====================================
# ====================================
# REPORTS PAGE
# ====================================

elif page == "Reports":


    st.title(
        "📄 RetailIQ Automation Center"
    )


    st.markdown(
        """
        Manage all RetailIQ automated business actions
        """
    )


    st.divider()



    # ==============================
    # INVENTORY CHECK
    # ==============================


    inventory_report = (
        check_inventory_status()
    )


    alert_message = ""


    for product, data in inventory_report.items():


        if data["Status"] != "SAFE":


            alert_message += f"""

🚨 RetailIQ Stock Alert

Product:
{product}

Current Stock:
{data['Current Stock']}

Minimum Stock:
{data['Minimum Stock']}

Status:
{data['Status']}

Action:
Purchase Order Required


-----------------------

"""



    if alert_message == "":


        alert_message = """

All inventory levels are healthy.

No action required.

"""



    # ==============================
    # FORECAST DATA
    # ==============================


    forecast_results = {}


    products = df["Product"].unique()


    for product in products:


        forecast = forecast_product(
            df,
            product,
            30
        )


        demand = predicted_demand(
            forecast
        )


        forecast_results[product] = demand



    # ==============================
    # OPTION 1 EMAIL
    # ==============================


    st.subheader(
        "📧 Email Alert Automation"
    )


    st.text_area(
        "Email Content",
        alert_message,
        height=200
    )



    if st.button(
        "📧 Send Vendor Email"
    ):


        send_stock_alert(
            alert_message
        )


        st.success(
            "Email sent successfully!"
        )



    st.divider()



    # ==============================
    # OPTION 2 WHATSAPP
    # ==============================


    st.subheader(
        "📱 WhatsApp Alert Automation"
    )



    if st.button(
        "📱 Send WhatsApp Alert"
    ):


        send_whatsapp_alert(
            alert_message
        )


        st.success(
            "WhatsApp message sent successfully!"
        )



    st.divider()



    # ==============================
    # OPTION 3 PDF
    # ==============================


    st.subheader(
        "📄 PDF Business Report"
    )



    if st.button(
        "📄 Generate RetailIQ PDF Report"
    ):


        pdf_path = generate_pdf(

            "RetailIQ_Report.pdf",

            sales_summary,

            inventory_report,

            forecast_results

        )


        st.success(
            "PDF Generated Successfully!"
        )


        with open(
            pdf_path,
            "rb"
        ) as file:


            st.download_button(

                label="⬇️ Download PDF",

                data=file,

                file_name="RetailIQ_Report.pdf",

                mime="application/pdf"

            )