import bl

def ask(message) -> str:
    return input(f"{message}:\n")

def show_all_categories() -> None:
    print(bl.get_all_categories())

def show_all_in_category() -> None:
    category = ask('Type category name')
    print(bl.get_all_in_category(category))

def add_to_shopping_cart() -> None:
    product_id = ask('Type product id(int)')
    count = ask('Type product count(int)')
    print(bl.add_to_shopping_cart(product_id, count))

def make_order() -> None:
    print(bl.make_order())

def main_flow() -> None:
    while True:
        operation = input("""Enter the number of operation:
        0. Exit
        1. Show all categories
        2. Show all product in category
        3. Add to shopping cart
        4. Make order
        """)
        if operation == '0':
            break
        elif operation == '1':
            show_all_categories()
        elif operation == '2':
            show_all_in_category()
        elif operation == '3':
            add_to_shopping_cart()
        elif operation == '4':
            make_order()
