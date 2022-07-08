import csv
import os

shopping_cart = []


def get_data():
    """Function reads data from a csv-file and return a list of dictionaries with product characteristics"""

    with open("PLC.csv", "r", encoding="utf-8") as csv_table:
        reader = csv.DictReader(csv_table)
        product_list = []

        for i in reader:
            product_list.append(i)
        return product_list


def work_with_shopping_cart(action, product=None):
    """Function adds, removes and displays items in the shopping cart"""

    global shopping_cart

    match action:
        case "add":
            shopping_cart.append(product)
            message = "Operation complete. Product was added to shopping cart"
            return shopping_cart, message
        case "change":
            message = "Operation complete. Product amount was changed"
            return shopping_cart, message
        case "delete":
            shopping_cart.remove(product)
            message = "Operation complete. Product was deleted from shopping cart"
            return shopping_cart, message
        case "show":
            return shopping_cart


def create_file_for_place_order(order_number):
    global shopping_cart
    with open(f"{order_number}.csv", "w", encoding="utf-8", newline="") as csv_order_table:
        writer = csv.DictWriter(csv_order_table, fieldnames=shopping_cart[0].keys())
        writer.writeheader()
        writer.writerows(shopping_cart)

    if os.path.exists(f"{order_number}.csv"):
        message = f"Order with № {order_number} has been successfully placed"
        shopping_cart.clear()
    else:
        message = "An error occurred while placing an order"

    return message


if __name__ == '__main__':
    get_data()
