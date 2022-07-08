import BL

def list_of_products():
    print(BL.show_categories())
    number_of_category = int(input("Enter the number of category:"))
    print(BL.show_products(number_of_category))

def add_product():
    item = int(input("Enter the code of product "))
    quantity = int(input("Enter the quantity of product "))
    print(BL.add_product(item, quantity))

def make_order():
    print(BL.get_final_check())

def main_flow():
    while True:
        operation = input("""Enter the number of operation:
        0. Exit
        1. List of products
        2. Add product to basket
        3. Make a final order
        """)
        if operation == '0':
            break
        elif operation == '1':
            list_of_products()
        elif operation == '2':
            add_product()
        elif operation == '3':
            make_order()

