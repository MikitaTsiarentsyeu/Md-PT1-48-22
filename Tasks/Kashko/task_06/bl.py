import data
import pickle

cart = dict()
last_displayed = dict()


def is_admin(login: str) -> bool:
    if login == data.ADMIN_LOGIN:
        return True


def check_admin_password(password: str) -> bool:
    if password == data.ADMIN_PASSWORD:
        return True


def get_menu(menu: str) -> list[tuple]:
    main = [(0, 'Exit'), (1, 'Show all meters'), (2, 'Show categories'),
            (3, 'Show cart'), (4, 'Show my orders')]
    cart = [(0, 'Return'), (1, 'Clear the cart'), (2, 'Delete item'),
            (3, 'Confirm order')]
    if menu == 'main':
        menu = main
    elif menu == 'cart':
        menu = cart
    global last_displayed
    last_displayed = {item[0]: None for item in menu}
    return menu


def is_number(s: str) -> bool:
    if s.isdecimal():
        return True


def is_exists(id: int, where: str) -> bool:
    if where == 'stock':
        place_to_check = last_displayed
    if where == 'cart':
        place_to_check = cart
    if id == 0 or id in place_to_check:
        return True


def is_in_stock(id: int, amount: int) -> bool:
    max_amount = last_displayed[id] - cart.get(id, 0)
    if amount <= max_amount:
        return True


def get_all() -> list[tuple]:
    meters = data.get_all_meters()
    global last_displayed
    last_displayed = {meter[0]: meter[5] for meter in meters}
    return meters


def get_categories() -> list[tuple]:
    categories = data.get_categories()
    global last_displayed
    last_displayed = {category[0]: 1 for category in categories}
    return categories


def get_category(id: int) -> list[tuple]:
    meters = data.get_category(id)
    global last_displayed
    last_displayed = {meter[0]: meter[5] for meter in meters}
    return meters


def get_orders(user: str) -> list[tuple]:
    orders = data.get_orders(user)
    global last_displayed
    last_displayed = {order[0]: 1 for order in orders}
    return orders


def add_to_cart(to_cart: tuple) -> None:
    id, quantity = to_cart
    cart[id] = cart.get(id, 0) + quantity


def get_cart() -> list[list] | int:
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
    cart.clear()


def remove_from_cart(id: int) -> None:
    del (cart[id])


def confirm_order(user: str) -> bool:
    if cart:
        content = pickle.dumps(cart)
        data.place_order(user, content)
        return True


def get_order(id: int) -> list[list]:
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
