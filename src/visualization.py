import matplotlib.pyplot as plt

def plot_product_sales(df):

    sales = df.groupby("Product")["Units_Sold"].sum()

    plt.figure(figsize=(8, 5))

    sales.plot(kind="bar")

    plt.title("Total Sales by Product")
    plt.xlabel("Product")
    plt.ylabel("Units Sold")

    plt.tight_layout()

    plt.savefig("reports/product_sales.png")

    plt.close()
    
def plot_daily_sales(df):

    daily_sales = df.groupby("Date")["Units_Sold"].sum()

    plt.figure(figsize=(10, 5))

    daily_sales.plot(kind="line", marker="o")

    plt.title("Daily Sales Trend")
    plt.xlabel("Date")
    plt.ylabel("Units Sold")

    plt.xticks(rotation=45)

    plt.tight_layout()

    plt.savefig("reports/daily_sales.png")

    plt.close()
def plot_product_share(df):

    sales = df.groupby("Product")["Units_Sold"].sum()

    plt.figure(figsize=(6, 6))

    sales.plot(kind="pie", autopct="%1.1f%%")

    plt.ylabel("")

    plt.title("Sales Distribution")

    plt.tight_layout()

    plt.savefig("reports/product_share.png")

    plt.close()