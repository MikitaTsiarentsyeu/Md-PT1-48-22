import Data


def show_categories():
    list_of_categories = Data.get_categories()
    return '\n'.join([f"{code}: {name}" for code, name in list_of_categories.items()])

def show_products(number_of_category):
    list_of_products = Data.get_products(number_of_category)
    return '\n'.join([f"{product['code']}: {product['name']}: {product['price_usd']}" for product in list_of_products])

def get_final_check():
    strings=[]
    total_price = 0
    basket = Data.get_check()
    for product, quantity in basket:
        strings.append(f"{product['name']}, {quantity}, cost {product['price_usd']*quantity}")
        total_price += product['price_usd']*quantity
    strings.append(f"Total price is {total_price}, $")
    return '\n'.join(strings)
    
        

def format_res(res, message):
    if res:
        return f"{message}\n{get_final_check()}"
    else:
        return "ERROR!"


def add_product(code, quantity):
    res = Data.add_product_to_basket(code, quantity)
    return format_res(res, "Product added to basket :p")