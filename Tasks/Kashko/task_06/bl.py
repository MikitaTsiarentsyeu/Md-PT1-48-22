import re
import data
import pickle


# User cart
cart = dict()

# Buffer for last displayed menu ot table
last_displayed = dict()


def is_admin(login: str) -> bool:
    """Checks is user an admin.

    Args:
        login (str): username

    Returns:
        bool: True or False
    """
    if login == data.ADMIN_LOGIN:
        return True


def check_admin_password(password: str) -> bool:
    """Checks password if user is admin.

    Args:
        password (str): admin password

    Returns:
        bool: True or False
    """
    if password == data.ADMIN_PASSWORD:
        return True


def get_menu(menu: str) -> list[tuple]:
    """Returns items for menu generating.

    Args:
        menu (str): 'main', 'cart' or 'admin' menu type.

    Returns:
        list[tuple]: items for menu
    """
    main = [(0, 'Exit'), (1, 'Show all meters'), (2, 'Show categories'),
            (3, 'Show cart'), (4, 'Show my orders')]
    cart = [(0, 'Return'), (1, 'Clear the cart'), (2, 'Delete item'),
            (3, 'Confirm order')]
    admin = [(0, 'Exit'), (1, 'Add meter'), (2, 'Add category'),
             (3, 'Show orders')]
    if menu == 'main':
        menu = main
    elif menu == 'cart':
        menu = cart
    elif menu == 'admin':
        menu = admin
    global last_displayed
    last_displayed = {item[0]: None for item in menu}
    return menu


def is_number(s: str) -> bool:
    """Checks is a string number.

    Args:
        s (str): string to check.

    Returns:
        bool: True or False.
    """
    if re.match(r'(\d+(?:\.\d+)?)', s):
        return True


def is_exists(id: int, where: str) -> bool:
    """Checks does id exist in stock or cart.

    Args:
        id (int): item id.
        where (str): 'stock' or 'cart'.

    Returns:
        bool: True or False.
    """
    if where == 'stock':
        place_to_check = last_displayed
    if where == 'cart':
        place_to_check = cart
    if id == 0 or id in place_to_check:
        return True


def is_in_stock(id: int, amount: int) -> bool:
    """Checks amount of meters available for order.

    Args:
        id (int): meter id.
        amount (int): amount to check.

    Returns:
        bool: True or False
    """
    max_amount = last_displayed[id] - cart.get(id, 0)
    if amount <= max_amount:
        return True


def get_all() -> list[tuple]:
    """Returns data for filling table with all meters in stock.

    Returns:
        list[tuple]: meters.
    """
    meters = data.get_all_meters()
    global last_displayed
    last_displayed = {meter[0]: meter[5] for meter in meters}
    return meters


def get_categories() -> list[tuple]:
    """Returns data for filling table with all existing categories.

    Returns:
        list[tuple]: categories.
    """
    categories = data.get_categories()
    global last_displayed
    last_displayed = {category[0]: 1 for category in categories}
    return categories


def get_category(id: int) -> list[tuple]:
    """Returns data for filling table with meters in one category in stock.

    Args:
        id (int): category id.

    Returns:
        list[tuple]: meters.
    """
    meters = data.get_category(id)
    global last_displayed
    last_displayed = {meter[0]: meter[5] for meter in meters}
    return meters


def get_orders(user: str) -> list[tuple]:
    """Returns data for filling table with all orders made by user.

    Args:
        user (str): username.

    Returns:
        list[tuple]: orders.
    """
    orders = data.get_orders(user)
    global last_displayed
    last_displayed = {order[0]: 1 for order in orders}
    return orders


def add_to_cart(to_cart: tuple) -> None:
    """Adds to cart selected meter.

    Args:
        to_cart (tuple): meter_id and amount.
    """
    id, quantity = to_cart
    cart[id] = cart.get(id, 0) + quantity


def get_cart() -> list[list] | int:
    """Returns data for filling a table with meters in the cart,
    calculates total price and amount of selected meters.
    Returns -1 if cart is empty.

    Returns:
        list[list] | int: meters or -1
    """
    if not cart:
        return -1
    ids = tuple(key for key in cart.keys())
    meters = data.get_meters_by_ids(ids)
    meters = list(map(list, meters))
    for meter in meters:
        meter.append(cart[meter[0]])
    amount = sum(map(lambda x: x[5], meters))
    total_price = sum(map(lambda x: x[4] * x[5], meters))
    meters.append(['Total:', '', '', '', total_price, amount])
    return meters


def clear_cart() -> None:
    """Deletes all items from cart.
    """
    cart.clear()


def remove_from_cart(id: int) -> None:
    """Removes meter from cart by id.

    Args:
        id (int): meter id.
    """
    del (cart[id])


def confirm_order(user: str) -> bool:
    """Serializes cart data to binary data
    and places it to database.

    Args:
        user (str): username

    Returns:
        bool: True or False
    """
    if cart:
        content = pickle.dumps(cart)
        if data.place_order(user, content):
            return True


def get_order(id: int) -> list[list]:
    """Returns data for filling a table with meters in the order,
    calculates total price and amount of ordered meters.

    Args:
        id (int): order id.

    Returns:
        list[list]: meters.
    """
    content = data.get_order(id)[0][0]
    content = pickle.loads(content)
    ids = tuple(key for key in content.keys())
    meters = data.get_meters_by_ids(ids)
    meters = list(map(list, meters))
    for meter in meters:
        meter.append(content[meter[0]])
    amount = sum(map(lambda x: x[5], meters))
    total_price = sum(map(lambda x: x[4] * x[5], meters))
    meters.append(['Total:', '', '', '', total_price, amount])
    return meters


# Admin functions
def add_item(meter: tuple) -> bool:
    """Inserts a new meter in database and returns the operation result.

    Args:
        meter (tuple): meter data.

    Returns:
        bool: True or False.
    """
    if data.insert_meter(meter):
        return True


def add_category(name: str) -> bool:
    """Inserts a new category in database and returns the operation result.

    Args:
        meter (tuple): category.

    Returns:
        bool: True or False.
    """
    if data.insert_category(name):
        return True


def get_all_orders() -> list[tuple]:
    """Returns a list of all user orders for filling a table with orders.

    Returns:
        list[tuple]: orders list.
    """
    orders = data.get_all_orders()
    global last_displayed
    last_displayed = {order[0]: 1 for order in orders}
    return orders
