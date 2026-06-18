import pandas as pd
from prophet import Prophet

def forecast_product(df, product_name, days=30):

    product_df = df[df["Product"] == product_name]

    prophet_df = product_df[["Date", "Units_Sold"]].copy()

    prophet_df.columns = ["ds", "y"]

    prophet_df["ds"] = pd.to_datetime(prophet_df["ds"])

    model = Prophet()

    model.fit(prophet_df)

    future = model.make_future_dataframe(periods=days)

    forecast = model.predict(future)

    return forecast
def predicted_demand(forecast, days=30):

    future_predictions = forecast.tail(days)

    return round(future_predictions["yhat"].sum())