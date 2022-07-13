import data
from getpass import getpass
import re

def format_res(res, message):
    if res:
        return f"{message}\n"
    else:
        return "Something went wrong"

def check_admin():
    login = input("Login: ")
    password = getpass("Password: ")
    check = data.check_admin(login, password)
    return check

def create_product():
    name = validate_input('name')
    category = validate_input('category')
    article = validate_input('article')
    price = validate_input('price')
    count_in_stock = validate_input('count in stock')
    res = data.add_product(name, category, article, price, count_in_stock)
    return format_res(res, 'Good job, product was created!')

def delete_product(id):
    res = data.delete_product(id)
    return format_res(res, f'Product with ID {id} was delete')

def view_category():
    res = data.get_data("category")
    category = ""
    for k,v in res.items():
        category += f"{k}. {v}\n"
    return category

def add_to_cart(id, count):
    res = data.add_product_in_cart(id, count)
    return format_res(res, f'Add product in your cart successful')

def create_cart():
    data.create_cart()

def total_price():
    total_price = 0
    products = data.get_data("cart")
    for key, values in products.items():
        total_price += float(values["price"]) * float(values["count_in_stock"])
    return round(total_price, 3)

def get_products(data_table="products" ,category_id="all"):
    products = data.get_data(data_table)
    line = "#" * 180 + "\n"
    res = line
    header = {1:"Name", 2:"Category", 3:"Article", 4:"Price", 5:"Count in stock"}
    
    def fixed_length(text, length):
        if len(text) > length:
            text = text[:length]
        elif len(text) < length:
            text = (text + " " * length)[:length]
        return text
    
    def add_item_in_table(res, key, values):
        res += f"# {fixed_length(key, 25)}  #  "
        for k, v in values.items():
            if k == "category":
                res += f"{fixed_length(data.get_data(k)[v], 25)}  #  "
            elif k == "price":
                res += f"{fixed_length(str(round(float(v), 3)), 25)}  #  "
            else:
                res += f"{fixed_length(v, 25)}  #  "
        res += "\n"
        return res

    res = add_item_in_table(res, "ID", header) + line

    for key, values in products.items():
        if category_id == "all":
            res = add_item_in_table(res, key, values)
        elif values["category"] == category_id:
            res = add_item_in_table(res, key, values)
    else:
        if data_table != "cart":
            res += line
        else:
            res += f"{line}\nTotal price: {total_price()}\n"
    return res

def place_order():
    tp = total_price()
    res = data.place_order()
    return format_res(res, f"Your order for {tp} has been placed, thank you for choosing us!")

def validate_input(check_value:str):
    checking_value = {
        "name":             r"[^a-zA-Z 0-9\-]",
        "category":         r"[^0-9]",
        "article":          r"[^a-zA-Z 0-9]",
        "price":            r"[^0-9\.]",
        "count in stock":   r"[^0-9]"
     }
    while True:
        validate_value = input(f"{f'{view_category()}' if check_value=='category' else ''}Enter {check_value}:")
        if re.findall(checking_value[check_value] , validate_value) != []:
                print("Incorrect input, try again")
                continue
        if check_value == "category":
            if validate_value not in data.get_data("category"):
                print("Incorrect value for category, try again")
                continue
        if check_value == "count in stock":
            if int(validate_value) <= 0:
                print("Incorrect value for count in stock, try again")
                continue
        break
    return validate_value