import bl
import data

def ask(message): 

    return input(f"{message}\n")

def show_category():
    print(bl.get_category())     

def order_add():
    global sku
    global qty
    while True:
        sku = ask("Enter item SKU:")
        if int(data.full_cat.get(sku)[4]) == 0:
            print("This item is out of stock.\n")
            return main_flow
        if not sku.isdigit():
            print('Please, enter digits!')
            continue
        if sku not in data.full_cat.keys():
            print("Please, enter a valid SKU!")
            continue
        else:
            break
    while True:
        qty = ask("Enter item QTY:")
        if not qty.isdigit():
            print('Please, enter digits!')
            continue
        if int(qty) > int(data.full_cat.get(sku)[4]):
            print("Please, enter a valid quantity!")
            continue
        else:
            break
    print(bl.order_add())

def final_order(): 
    print(bl.final_order())

def main_flow():
    while True:
        global operation
        operation = int(input("""Enter the number of operation:
        1 - Wine.
        2 - Whisky.
        3 - Final order.
        0 - Exit.
        """))

        if operation == 0:
            break
        elif operation == 1:
            show_category()
            order_add()
        elif operation == 2:
            show_category()
            order_add()
        elif operation == 3:
            final_order()
            