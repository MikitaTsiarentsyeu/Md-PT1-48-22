import buisness_logic as bl


def ask(massage):
    return input(f"{massage}:\n")


def show_all():
    print(bl.get_all())


def add_product():
    code = ask("Enter the product code")
    print(bl.add_goods(code))


def remove_product():
    code = ask("Enter the product code")
    print(bl.del_product(code))

def show_order():
    print(bl.order())

def show_current_order():
    print(bl.show())


def main_flow():
    while True:
        operation = input("""Enter the number of operation:
        0. Exit
        1. Show all products
        2. Add product to shopping cart
        3. Remove a product from the shopping cart
        4. Show order
        5. Place an order
        """)
        if operation == "0":
            break
        elif operation == "1":
            show_all()
        elif operation == "2":
            add_product()
        elif operation == "3":
            remove_product()
        elif operation == "4":
            show_current_order()
        elif operation == "5":
            show_order()
            break
