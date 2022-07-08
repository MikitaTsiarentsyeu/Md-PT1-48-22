from os import system

import prettytable
from prettytable.colortable import ColorTable, Themes

import bl

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

orders_table_params = {'No': 'c', 'Date': 'l'}


def authorize() -> str:
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


def ask_choice(message: str, is_exists: str | None = None) -> int:
    while True:
        inp = input(f'{message}\n')
        if not bl.is_number(inp):
            print('Input must be an non-negative number.')
            continue
        inp = int(inp)
        if is_exists and not bl.is_exists(inp, is_exists):
            print("Selected item doesn't exist.")
            continue
        return inp


def create_table(rows: list[tuple], params: dict) -> ColorTable:
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
    menu = bl.get_menu(menu)
    table = create_table(menu, menu_table_params)
    print(table)


def show_all() -> None:
    meters = bl.get_all()
    table = create_table(meters, meters_table_params)
    print(table)


def show_category(id: int) -> None:
    meters = bl.get_category(id)
    table = create_table(meters, meters_table_params)
    print(table)


def show_categories() -> tuple:
    categories = bl.get_categories()
    table = create_table(categories, categories_table_params)
    print(table)


def add_to_cart() -> None:
    while True:
        meter_id = ask_choice(
            "Enter meter's id to add it to cart or 0 to return:", 'stock')
        if meter_id == 0:
            break
        amount = ask_choice('Enter the amount of selected meters:')
        if bl.is_in_stock(meter_id, amount):
            bl.add_to_cart((meter_id, amount))
            print(f'{amount} item(s) with id: {meter_id} '
                  f'was(were) successfully added.')
        else:
            print("There aren't enough devices in stock.")
            continue


def show_cart() -> None:
    meters = bl.get_cart()
    if meters == -1:
        print('The cart is empty yet.')
    else:
        table = create_table(meters, meters_table_params)
        print(table)


def show_orders(user: str) -> bool:
    orders = bl.get_orders(user)
    if orders:
        table = create_table(orders, orders_table_params)
        print(table)
    else:
        print("You didn't place any orders.")


def clear_cart() -> None:
    bl.clear_cart()


def remove_from_cart() -> None:
    while True:
        meter_id = ask_choice(
            "Enter meter's id to remove it from cart or 0 to return:", 'cart')
        if meter_id == 0:
            return
        break
    bl.remove_from_cart(meter_id)


def confirm_order(user: str) -> None:
    if bl.confirm_order(user):
        print('The order was placed. Thank you!')
    else:
        print('Something is wrong, sorry. Try again, please.')


def show_order(id: int) -> None:
    meters = bl.get_order(id)
    table = create_table(meters, meters_table_params)
    print(table)


def user_flow(user: str) -> None:
    while True:
        system('clear')
        print(f'{user}, you are welcome!')
        show_menu('main')
        operation = ask_choice('Enter the number of operation:', 'stock')
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
            category = ask_choice(
                'Enter the number of category to show or 0 to return:',
                'stock')
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
                operation = ask_choice('Enter the number of operation:',
                                       'stock')
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
            order = ask_choice('Enter number of order to show or 0 to return:',
                               'stock')
            if order == 0:
                continue
            system('clear')
            show_order(order)
            ask_choice('Enter any number to return:')


def admin_flow() -> None:
    print('Admin UI')


def main_flow():
    while True:
        user = authorize()
        if not user:
            print('Programm was fifnished')
            break
        elif user == 'admin':
            admin_flow()
        else:
            user_flow(user)
