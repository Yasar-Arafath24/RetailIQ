import pandas as pd

def load_sales_data():
    df = pd.read_csv("data/sales.csv")
    return df