from os import system

import prettytable
from prettytable.colortable import ColorTable, Themes

import bl


# Dictionaries with column names and align types for tables
menu_table_params = {'No': 'c', 'Item': 'l'}

meters_table_params = {
    'Meter ID': 'c',
    'Meter Name': 'l',
    'Meter Type': 'c',
    'Category': 'l',
    'Price, $': 'r',
    'Amount': 'r'
}

categories_table_params = {'No': 'c', 'Category': 'l'}

orders_table_params = {'No': 'c', 'Date': 'c'}

admin_table_params = {'No': 'c', 'Date': 'c', 'User': 'l'}


# Common functions
def authorize() -> str:
    """Returns username as string and checks password for admin.

    Returns:
        str: username.
    """
    while True:
        login = input('Enter your login to authorize or nothing to exit:\n')
        if not bl.is_admin(login):
            return login
        else:
            attempts = 3
            while True:
                password = input(f'Enter the correct password, please.'
                                 f'You have {attempts} attempts.\n')
                attempts -= 1
                if attempts == 0:
                    print("Sorry, you aren't an administrator. ")
                    break
                elif not bl.check_admin_password(password):
                    continue
                else:
                    return 'admin'


def ask_number(message: str,
               n_type: str = 'int',
               is_exists: str | None = None) -> int | float:
    """Returns valited integer or float number from user
    and checks it exists in stock or cart.

    Args:
        message (str): text message.
        n_type (str, optional): 'int' or 'float'. Defaults to 'int'.
        is_exists (str | None, optional): 'stock' or 'cart'. Defaults to None.

    Returns:
        int | float: integer or float number.
    """
    while True:
        inp = input(f'{message}\n')
        if not bl.is_number(inp):
            print('Input must be a non-negative number.')
            continue
        if n_type == 'int':
            inp = int(inp)
        elif n_type == 'float':
            inp = float(inp)
        if is_exists and not bl.is_exists(inp, is_exists):
            print("Selected item doesn't exist.")
            continue
        return inp


def ask(message: str) -> str:
    """Returns non-empty string from user.

    Args:
        message (str): text message.

    Returns:
        str: string.
    """
    while True:
        inp = input(f'{message}\n')
        if not inp:
            print('Enter non-empty string.')
            continue
        return inp


def create_table(rows: list[tuple], params: dict) -> ColorTable:
    """Returns ColorTable object filled with data.

    Args:
        rows (list[tuple]): data for filling.
        params (dict): column names and align parametres.

    Returns:
        ColorTable: ColorTable object.
    """
    table = ColorTable(theme=Themes.OCEAN)
    table.field_names = params
    table.add_rows(rows)
    for k, v in params.items():
        table.align[k] = v
    table.float_format = ".2"
    table.hrules = prettytable.FRAME
    table.vrules = prettytable.NONE
    return table


def show_menu(menu: str) -> None:
    """Prints menu

    Args:
        menu (str): 'main', 'cart' or 'admin' menu type.
    """
    menu = bl.get_menu(menu)
    table = create_table(menu, menu_table_params)
    print(table)


# User functions
def show_all() -> None:
    """Prints table with all meters in stock.
    """
    meters = bl.get_all()
    table = create_table(meters, meters_table_params)
    print(table)


def show_category(id: int) -> None:
    """Prints table with one category of meters in stock.
    """
    meters = bl.get_category(id)
    table = create_table(meters, meters_table_params)
    print(table)


def show_categories() -> tuple:
    """Prints table with all existing categories.
    """
    categories = bl.get_categories()
    table = create_table(categories, categories_table_params)
    print(table)


def add_to_cart() -> None:
    """Adds selected by user meters to cart.
    """
    while True:
        meter_id = ask_number(
            "Enter meter's id to add it to cart or 0 to return:",
            is_exists='stock')
        if meter_id == 0:
            break
        amount = ask_number('Enter the amount of selected meters:')
        if bl.is_in_stock(meter_id, amount):
            bl.add_to_cart((meter_id, amount))
            print(f'{amount} item(s) with id: {meter_id} '
                  f'was(were) successfully added.')
        else:
            print("There aren't enough devices in stock.")
            continue


def show_cart() -> None:
    """Prints meters were added to cart by user/
    """
    meters = bl.get_cart()
    if meters == -1:
        print('The cart is empty yet.')
    else:
        table = create_table(meters, meters_table_params)
        print(table)


def show_orders(user: str) -> None:
    """Prints all orders made by user.

    Args:
        user (str): username.
    """
    orders = bl.get_orders(user)
    if orders:
        table = create_table(orders, orders_table_params)
        print(table)
    else:
        print("You didn't place any orders.")


def clear_cart() -> None:
    """Removes all meters from cart.
    """
    bl.clear_cart()


def remove_from_cart() -> None:
    """Removes meter selected by user from cart.
    """
    while True:
        meter_id = ask_number(
            "Enter meter's id to remove it from cart or 0 to return:",
            is_exists='cart')
        if meter_id == 0:
            return
        break
    bl.remove_from_cart(meter_id)


def confirm_order(user: str) -> None:
    """Places order to database.

    Args:
        user (str): username.
    """
    if bl.confirm_order(user):
        print('The order was placed. Thank you!')
    else:
        print('Something is wrong, sorry. Try again, please.')


def show_order(id: int) -> None:
    """Prints an order selected by user.

    Args:
        id (int): order id.
    """
    meters = bl.get_order(id)
    table = create_table(meters, meters_table_params)
    print(table)


# Admin functions
def add_item() -> None:
    """Adds new item in database.
    """
    name = ask('Enter a meter name:')
    type = ask('Enter a meter type:')
    category = ask('Enter a category name:')
    price = ask_number('Enter a price:', 'float')
    amount = ask_number('Enter an amount in stock:')
    if bl.add_item((name, type, category, price, amount)):
        print(f'The item {name} {type} was added.')
    else:
        print('Something is wrong, sorry. Try again, please.')


def add_category() -> None:
    """Adds a new category to database.
    """
    category = ask('Enter a name of new category:')
    if bl.add_category(category):
        print(f'The category {category} was added.')
    else:
        print('Something is wrong, sorry. Try again, please.')


def show_all_orders() -> None:
    """Prints all order made by all users.
    """
    orders = bl.get_all_orders()
    table = create_table(orders, admin_table_params)
    print(table)


# User TUI
def user_flow(user: str) -> None:
    while True:
        system('clear')
        print(f'{user}, you are welcome!')
        show_menu('main')
        operation = ask_number('Enter the number of operation:',
                               is_exists='stock')
        if operation == 0:
            clear_cart()
            system('clear')
            print(f'Goodbye, {user}!')
            break
        elif operation == 1:
            system('clear')
            show_all()
            add_to_cart()
        elif operation == 2:
            system('clear')
            show_categories()
            category = ask_number(
                'Enter the number of category to show or 0 to return:',
                is_exists='stock')
            if category == 0:
                continue
            else:
                system('clear')
                show_category(category)
                add_to_cart()
                continue
        elif operation == 3:
            system('clear')
            while True:
                show_cart()
                show_menu('cart')
                operation = ask_number('Enter the number of operation:',
                                       is_exists='stock')
                if operation == 0:
                    system('clear')
                    break
                elif operation == 1:
                    clear_cart()
                    system('clear')
                    continue
                elif operation == 2:
                    remove_from_cart()
                elif operation == 3:
                    system('clear')
                    confirm_order(user)
                    clear_cart()
        elif operation == 4:
            system('clear')
            show_orders(user)
            order = ask_number('Enter number of order to show or 0 to return:',
                               is_exists='stock')
            if order == 0:
                continue
            system('clear')
            show_order(order)
            ask_number('Enter any number to return:')


# Admin TUI
def admin_flow(user: str) -> None:
    system('clear')
    print(f'{user}, you are welcome!')
    while True:
        show_menu('admin')
        operation = ask_number('Enter the number of operation:',
                               is_exists='stock')
        if operation == 0:
            system('clear')
            print(f'Goodbye, {user}!')
            break
        elif operation == 1:
            system('clear')
            add_item()
        elif operation == 2:
            system('clear')
            add_category()
        elif operation == 3:
            system('clear')
            show_all_orders()
            order = ask_number('Enter number of order to show or 0 to return:',
                               is_exists='stock')
            if order == 0:
                continue
            system('clear')
            show_order(order)
            ask_number('Enter any number to return:')


# Start TUI
def main_flow():
    system('clear')
    while True:
        user = authorize()
        if not user:
            print('Programm was fifnished')
            break
        elif user == 'admin':
            admin_flow(user)
        else:
            user_flow(user)
