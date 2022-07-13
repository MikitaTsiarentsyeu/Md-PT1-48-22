import bl


def displayed_data(header, product, message=""):
    """Function displays information on the screen"""

    print(message)
    print(*header) if header else None
    if product:
        for i in product:
            print(*i)


def show_all():
    """function displays all data from the database"""

    header, product = bl.get_all_from_bd("show_all")
    displayed_data(header, product)


def show_types():
    """function displays all product types from the database"""

    types = bl.get_product_types()
    displayed_types = [f"{i + 1}-{item}" for i, item in enumerate(types)]
    print(f"Available product types: {', '.join(displayed_types)}")
    while True:
        choice = input("""
        Product from which type do you want to display?
        (press enter to the exit to main menu)\n""")
        if choice == "":
            break
        else:
            header, product = bl.get_all_from_bd(choice, types)
            displayed_data(header, product)
            break


def add_product():
    """the function adds the selected product to the cart"""

    name = input("Enter the name of the product, which you want to add to shopping cart: ")
    amount = input("Enter quantity: ")
    header, product, message = bl.add_product_to_shopping_cart(name, amount)

    displayed_data(header, product, message)


def delete_product():
    """the function removes the selected product from the cart"""

    name = input("Enter the name of the product, which you want to delete from shopping cart: ")
    header, product, message = bl.delete_product_from_shopping_cart(name)

    displayed_data(header, product, message)


def change_product():
    """the function changes the quantity of the product in the cart"""

    name = input("Enter the name of the product, for which you want to change the quantity: ")
    amount = input("Enter quantity: ")
    header, product, message = bl.change_product_amount(name, amount)

    displayed_data(header, product, message)


def show_shopping_cart():
    """the function displays all products from the cart"""

    header, product, message = bl.show_product_from_shopping_cart()

    displayed_data(header, product, message)


def place_order():
    print(bl.create_place_order())


def main():
    while True:
        operation = input("""Menu:
        1 - Show all catalog
        2 - Show all available product types
        3 - Add product in shopping cart
        4 - Change product amount in shopping cart
        5 - Delete product from shopping cart
        6 - Show product in shopping cart
        7 - Place an order
        8 - Exit
        """)
        match operation:
            case "1":
                show_all()
            case "2":
                show_types()
            case "3":
                add_product()
            case "4":
                change_product()
            case "5":
                delete_product()
            case "6":
                show_shopping_cart()
            case "7":
                place_order()
            case "8":
                print("Thanks for using our application")
                break


if __name__ == '__main__':
    main()
