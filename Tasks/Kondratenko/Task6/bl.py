import db
import datetime

available_products = []
order_counter = 1


def get_all_from_bd(*option):
    """function get all data from the database"""

    global available_products
    available_products = db.get_data()

    if option[0] == "show_all":
        return product_parser(available_products)
    else:
        return product_parser(available_products, *option)


def product_parser(products, choise_type="", type_list=None):
    """the function generates a list of products according to the input data for correct display"""

    if type_list is None:
        type_list = []

    # Clear old list before read a new data
    products_list = []

    if choise_type == "":
        for i in products:
            products_list.append(list(i.values()))
    else:
        type_menu = {str(k + 1): v for k, v in enumerate(type_list)}

        try:
            for i in products:
                if i["Type"] == type_menu[choise_type]:
                    products_list.append(list(i.values()))
                else:
                    continue
        except:
            print("Wrong type selected. Please select correct type")
            return

    if products:
        header = list(products[0].keys())
        return justify(header, products_list)
    else:
        header = products_list = []
        return header, products_list


def justify(header, products):
    """Justify header and products elements for nice console output"""

    header = [header[i].center(43 if i == 0 else 25) for i in range(len(header))]

    for index, element in enumerate(products):
        products[index] = [element[j].center(43 if j == 0 else 25) for j in range(len(element))]

    return header, products


def get_product_types():
    """A function from the entire list of products determines all existing types of equipment.
    The output is in the form of a list"""

    lst = db.get_data()
    types = []

    for i in lst:
        if i["Type"] in types:
            continue
        else:
            types.append(i['Type'])

    return types


def add_product_to_shopping_cart(name, amount: str):
    """the function adds the selected product to the shopping cart"""

    global available_products

    if amount.isdigit():
        for product in available_products:
            if product["Name"] == name:
                select_product = product.copy()
                select_product["Amount"] = amount
                shopping_cart, message = db.work_with_shopping_cart("add", select_product)
                return *product_parser(shopping_cart), message
        else:
            message = "Product was not found in catalog"
            shopping_cart = db.work_with_shopping_cart("show")
            return *product_parser(shopping_cart), message
    else:
        message = "Amount is incorrect"
        shopping_cart = db.work_with_shopping_cart("show")
        return *product_parser(shopping_cart), message


def change_product_amount(name, amount):
    """the function changes the quantity of the product in the cart"""

    shopping_cart = db.work_with_shopping_cart("show")

    if amount.isdigit():
        for product in shopping_cart:
            if product["Name"] == name:
                if int(amount) <= 0:
                    message = "Amount is incorrect"
                else:
                    product["Amount"] = amount
                    shopping_cart, message = db.work_with_shopping_cart("change", product)
                break
        else:
            message = "Product was not found in shopping cart"

        return *product_parser(shopping_cart), message
    else:
        message = "Amount is incorrect"
    return *product_parser(shopping_cart), message


def delete_product_from_shopping_cart(name):
    """the function removes the selected product from the shopping cart"""

    shopping_cart = db.work_with_shopping_cart("show")

    for product in shopping_cart:
        if product["Name"] == name:
            shopping_cart, message = db.work_with_shopping_cart("delete", product)
            break
    else:
        message = "Product was not found in shopping cart"

    return *product_parser(shopping_cart), message


def show_product_from_shopping_cart():
    """the function get all products from the shopping cart"""

    shopping_cart = db.work_with_shopping_cart("show")
    message = "Your current shopping cart"

    return *product_parser(shopping_cart), message


def create_place_order():
    """the function generates the name of the order file
    and generates a task to create a file"""
    global order_counter
    shopping_cart = db.work_with_shopping_cart("show")

    today = datetime.datetime.today()
    order_name = f"{today:%Y%m%d}-{str(order_counter).zfill(5)}"
    order_counter += 1
    message_1 = db.create_file_for_place_order(order_name)

    for product in available_products:
        for order_product in shopping_cart:
            if product["Name"] == order_product["Name"]:
                if int(product["Amount"]) > int(order_product["Amount"]):
                    product["Amount"] = str(int(product["Amount"]) - int(order_product["Amount"]))
                else:
                    product["Amount"] = "0"

    message_2 = db.upgrade_data_in_file(available_products)

    return message_1 + "\n" + message_2


if __name__ == '__main__':
    get_all_from_bd()
    # get_product_types()
