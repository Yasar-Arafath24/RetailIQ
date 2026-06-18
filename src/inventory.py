inventory = {
    "Milk": 500,
    "Bread": 100,
    "Rice": 700
}
minimum_stock = {
    "Milk": 200,
    "Bread": 150,
    "Rice": 300
}
def get_inventory():

    return inventory
def check_inventory_status():

    report = {}

    for product in inventory:

        current_stock = inventory[product]
        min_stock = minimum_stock[product]

        if current_stock <= min_stock:
            status = "LOW STOCK"
        else:
            status = "SAFE"

        report[product] = {
            "Current Stock": current_stock,
            "Minimum Stock": min_stock,
            "Status": status
        }

    return report

def calculate_reorder_quantity():

    reorder_report = {}

    for product in inventory:

        current_stock = inventory[product]
        min_stock = minimum_stock[product]

        if current_stock <= min_stock:

            reorder_qty = (min_stock * 2) - current_stock

            reorder_report[product] = reorder_qty

    return reorder_report

