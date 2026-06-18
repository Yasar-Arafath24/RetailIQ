import pandas as pd

def total_sales_per_product(df):
    return df.groupby("Product")["Units_Sold"].sum()

def best_selling_product(df):
    sales = df.groupby("Product")["Units_Sold"].sum()

    return sales.idxmax(), sales.max()

def worst_selling_product(df):
    sales = df.groupby("Product")["Units_Sold"].sum()

    return sales.idxmin(), sales.min()

def total_units_sold(df):
    return df["Units_Sold"].sum()

def daily_sales(df):
    daily = df.groupby("Date")["Units_Sold"].sum()

    return daily