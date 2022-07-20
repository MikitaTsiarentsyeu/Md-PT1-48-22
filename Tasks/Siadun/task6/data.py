repo = [{"name": "Ballpoint pen, 'Erich Krause'",
    "number": 100, 
    "price": 0.79, 
    "count_in_stock": 11, 
    "product_category": "Writing utensils"},
{"name": "Ballpoint pen, 'Erich Krause'",
    "number": 101,
    "price": 0.89,
    "count_in_stock": 43,
    "product_category": "Writing utensils"},
{"name": "Set of gel pens 'HanzKoger', 3 pcs",
    "number": 102,
    "price": 2.79,
    "count_in_stock": 23,
    "product_category": "Writing utensils"},
{"name": "Pencil set, 'Koh-I-Noor', 6 pcs",
    "number": 103,
    "price": 12.99,
    "count_in_stock": 0,
    "product_category": "Writing utensils"},
{"name": "Notebook, 'Unipress'",
    "number": 104,
    "price": 9.99,
    "count_in_stock": 2,
    "product_category": "Notebooks, notepads, paper"},
{"name":"Book of accounting, 'Viola', 96 l",
    "number": 105,
    "price": 14.99,
    "count_in_stock": 3,
    "product_category": "Notebooks, notepads, paper"},
{"name": "Educational game, 'Huada', Sticks and balls, 100 pcs",
    "number": 106,
    "price": 13.66,
    "count_in_stock": 4,
    "product_category": "Table games"},
{"name": "Toy, 'Battleship'",
    "number": 107,
    "price": 18.89,
    "count_in_stock": 1,
    "product_category": "Table games"}]

def get_all_products_repo():
    return repo

def product_category(number):
    for products in repo:
        if products['number'] == number:
            return products
        elif products == None:
            return False
shopping_basket = []
final_price = 0

def number_products(number, quantity):
    number_products = product_category(number)
    if number_products == None:
        return False
    number_products['quantity'] = quantity
    if number_products ['quantity'] <= number_products['count_in_stock']:
        number_products ['count_in_stock'] -= quantity
        shopping_basket.append(number_products)
        return shopping_basket
    else:
        return False

def bascet():
    return f' Your items in the cart: {len(shopping_basket)}'

def get_an_invoice():
    return shopping_basket

def remove_product(number):
    for products in shopping_basket:
        if products['number'] == number:
            return f'Deleted: {shopping_basket.pop(shopping_basket.index(products))}'
        else:
            return 'Еhere is no such id in the porridge basket'

def empty_trash():
    shopping_basket.clear()
    return('Basket cleaning')