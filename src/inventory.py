# ====================================
# INVENTORY DATA
# ====================================

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

# ====================================
# GET INVENTORY
# ====================================

def get_inventory():

    return inventory


# ====================================
# CHECK INVENTORY STATUS
# ====================================

def check_inventory_status():

    report = {}

    for product in inventory:

        current_stock = inventory[product]

        min_stock = minimum_stock[product]

        # ==========================
        # STOCK CLASSIFICATION
        # ==========================

        if current_stock <= min_stock:

            status = "CRITICAL"

        elif current_stock <= (min_stock * 1.5):

            status = "WARNING"

        else:

            status = "SAFE"

        report[product] = {

            "Current Stock": current_stock,

            "Minimum Stock": min_stock,

            "Status": status

        }

    return report


# ====================================
# REORDER QUANTITY
# ====================================

def calculate_reorder_quantity():

    reorder_report = {}

    for product in inventory:

        current_stock = inventory[product]

        min_stock = minimum_stock[product]

        if current_stock <= (min_stock * 1.5):

            reorder_qty = (min_stock * 2) - current_stock

            if reorder_qty < 0:

                reorder_qty = 0

            reorder_report[product] = reorder_qty

    return reorder_report


# ====================================
# INVENTORY SUMMARY
# ====================================

def inventory_summary():

    total_products = len(inventory)

    critical_count = 0

    warning_count = 0

    safe_count = 0

    report = check_inventory_status()

    for product in report:

        status = report[product]["Status"]

        if status == "CRITICAL":

            critical_count += 1

        elif status == "WARNING":

            warning_count += 1

        else:

            safe_count += 1

    return {

        "Total Products": total_products,

        "Critical Products": critical_count,

        "Warning Products": warning_count,

        "Safe Products": safe_count

    }