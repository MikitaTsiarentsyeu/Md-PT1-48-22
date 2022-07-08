import os
import re
import data


def prepatate_str(st):
    if isinstance(st, list):
        st = st[0][0]
        return st.split('/')[-2]
    return st.split('/')[-2]


def get_pretty():
    print(f'\n{"*" * 35}')


def clear():
    try:
        return os.system("clear")
    except:
        return os.system("cls")


def get_first_page():
    return data.use_database()


def get_second_page(number, tag=False):
    qi_tuple = {}
    links_dict = {}
    lst = data.use_database(number)
    for ide, title, link in lst:
        qi_tuple[ide] = title
        links_dict[ide] = link
    if tag: return links_dict
    return qi_tuple.items()


def get_third_page(previousN, currentN, info=None):
    links_dict = (get_second_page(previousN, True))
    table_name = prepatate_str(links_dict[currentN])

    short_info_dict = {}
    full_info_dict = {}
    query_result = data.use_database(currentN, table_name)
    for id, name, art, price in query_result:
        short_info_dict[id] = name
        full_info_dict[id] = name, art, price

    if not info:
        return short_info_dict.items()
    else:
        return full_info_dict[info]


def get_format_info(info: tuple) -> str:
    if isinstance(info, tuple):
        name, art, price = info
        return f"Название продукта: {name}\n{art}\nЦена: {replace_price(price):3} руб./шт"


def add_user_item(item: tuple):
    name, art, price = item
    price = replace_price(price)
    item = (name, art, price)
    data.write_user_cart((name, art, price))


def replace_price(price):
    new_price = re.search("^[\d\.]*", price)
    return float(new_price.group(0))


def get_price():
    result = float(data.read_cart_price()[0][0])
    return round(result, 2)


def check_cart_info():
    query_result = data.read_user_cart()

    art_default = [c.split()[-1] for a, b, c, d in query_result]
    art_counte = []
    for num, name, art, price in query_result:
        articul = art.split()[-1]
        count_items = art_default.count(articul)
        if art not in art_counte:
            print(
                f"Продукт №{num}",
                f"Название:   {name}",
                f"Артикул:    {articul}",
                f"Цена:       {float(price) * count_items} руб.",
                f"Количество: {count_items} ед.",
                sep="\n"
            )
            print('--' * 10)

        art_counte.append(art)


def get_cart_data():
    while True:
        try:
            clear()
            print("SHOPPING CART")
            get_pretty()
            query_result = data.read_user_cart()
            check_cart_info()
            print(f'Shopping Cart Total Price is {get_price()} BYN.\n')
            print("*" * 35)
            user_inp = int(
                input("1. to pay all items\n2. to delete one or all items\n3. to close the cart\nPress to continue: "))

            if user_inp == 3:
                break
            elif user_inp == 1:
                clear()
                print("You have successfully paid your order! ")
                data.delete_all_items()
                get_pretty()
                user_inp = (input("Enter to continue: "))
            elif user_inp == 2:
                deletion_section()

        except TypeError:
            ent = input("Your Cart is empty, to continue shopping press enter: ")
            break
        except ValueError:
            ent = input("Please, enter correct value and try again: ")
            get_cart_data()



def deletion_section():
    clear()
    print(f"DELETE section")
    get_pretty()
    check_cart_info()
    get_pretty()
    user_del = input(
        "Type number of item which you want to delete,\nType 'all' to delete all entries,\nEnter to go back,"
        "\nChoose to continue: ")
    clear()
    if user_del == 'all':
        data.delete_all_items()
    elif user_del == "":
        return None
    elif user_del.isdigit():

        result = data.delete_user_item(int(user_del))
        if result:
            clear()
            result_message = input(f'Item {user_del} was successfully deleted!\n\nPress to continue: ')
        else:
            result_message = input(f'Please, choose exists number of item!\n\nPress to continue: ')
            deletion_section()
    else:
        clear()
        error_output = input("Please enter correct number!\n\nEnter to continue: ")
        deletion_section()
