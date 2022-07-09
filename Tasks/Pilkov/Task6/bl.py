import data

console_cookie = {'shoping_card': {} }

def format_res(res: int, message = 'OK') -> str:
    if res == 0:
        return f"{message}\n"
    elif res == 1:
        return "Product not found"
    elif res == 2:
        return "Selected item not enouth"
    elif res == 3:
        return "Not supported input type"
    elif res == 4:
        return "There is nothing in your shoping card"
    elif res == 5:
        return "Not correct number of items in shoping card"
    else:
        return "Something went wrong"


def get_all_in_category(category_name: str) -> str:
    products = data.get_all_in_category(category_name)
    if len(products) == 0:
        return 'Category not found'
    
    formated_products = []
    formated_products.append(f'|  Id | {" "*8}Name{" "*8} |  Category  |   Cost  | Items |')
    formated_products.append(f'{"-"*61}')

    for product in products:
        formated_products.append(f'| {product[0]:>3} | {product[1]:>20} | {product[2]:>10} | {product[3]:>7} | {product[4]:>5} |')
    return '\n'.join(formated_products)

def get_all_categories() -> str:
    categories = data.get_all_categories()
    return '\n'.join(categories)

def add_to_shopping_cart(product_id: str, count: str) -> str:
    try:
        product_id = int(product_id)
        count = int(count)
    except ValueError:
        return format_res(3)
    
    # chech is product already in shoping card
    try:
        count += console_cookie['shoping_card'][product_id]
    except KeyError:
        pass

    res = data.check_is_product_enouth(product_id, count)
    if res == 0:
        console_cookie['shoping_card'][product_id] = count
    return format_res(res, 'Item was added to shoping cart')

def make_order() -> str:
    res = data.make_order(console_cookie['shoping_card'])
    console_cookie['shoping_card'] = {}
    return format_res(res, 'Order was maded')
