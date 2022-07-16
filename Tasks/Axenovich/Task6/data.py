import json
import os

cart_json = os.path.join(os.getcwd(), "Tasks", "Axenovich", "Task6", "cart.json")
catalog_json = os.path.join(os.getcwd(), "Tasks", "Axenovich", "Task6", "catalog.json")

def get_data(option="products"):
    data = {}
    if option == "cart":
        open_file = cart_json
    else:
        open_file = catalog_json
    with open(open_file, "r+") as f:
        try:
            data = json.load(f)
        except json.decoder.JSONDecodeError:
            data = {}
        if option == "cart":
            return data
        elif option == "products":
            data_return = data["products"]
        else:
            data_return = data["category"]
    return data_return

def create_cart():
    open(cart_json, 'w').close()

def check_data(f, c):
    try:
        data = json.load(f)
    except json.decoder.JSONDecodeError:
        data = {}
    try:
        cart = json.load(c)
    except json.decoder.JSONDecodeError:
        cart = {}
    return data, cart

def add_product_in_cart(id, count):
    with open(catalog_json, "r+") as f:
        with open(cart_json, "r+") as c:
            data, cart = check_data(f, c)
            new_product = data["products"][f"{id}"]
            print(int(new_product['count_in_stock']))
            print(int(data["products"][f"{id}"]['count_in_stock']))
            if 0 < int(count) <= int(data["products"][f"{id}"]['count_in_stock']):
                new_product['count_in_stock'] = str(count)
                cart[f"{id}"] = new_product
                c.seek(0)
                json.dump(cart, c, indent = 2)
                return True
            else:
                return False

def check_admin(login, password):
    if login == 'admin' and password == "123":
        return True
    else: False

def clear_file():  # I don't know, but without this line my json destroyed
    open(catalog_json, 'w').close()

def add_product(name, category, article, price, count_in_stock):
    with open(catalog_json, "r+") as f:
        data = json.load(f)
        products = data["products"]
        new_data = {"name": name, 
                    "category": category, 
                    "article": article, 
                    "price": price, 
                    "count_in_stock": count_in_stock
                    }
        try:
            for i in range(1, len(products)+2):
                if str(i) not in products:
                    data["products"][f"{i}"] = new_data
                    clear_file()
                    f.seek(0)
                    json.dump(data, f, indent = 3)
                    break
            return True
        except:
            return False

def delete_product(id):
    with open(catalog_json, "r+") as f:
        data = json.load(f)
        products = data["products"]
        try:
            for i in products:
                if i == id:
                    del products[f"{id}"]
                    data["products"] = products
                    break
            clear_file()
            f.seek(0)
            json.dump(data, f, indent = 4)
            return True
        except:
            return False

def place_order():
    with open(catalog_json, "r+") as f:
        with open(cart_json, "r+") as c:
            data, cart = check_data(f, c)
            if cart != {}:
                for key, values in cart.items():
                    if key in data["products"]:
                        data["products"][key]["count_in_stock"] = str(int(data["products"][key]["count_in_stock"])
                        - int(values["count_in_stock"]))
                clear_file()
                f.seek(0)
                json.dump(data, f, indent = 5)
                create_cart()
                return True
            else:
                return False
