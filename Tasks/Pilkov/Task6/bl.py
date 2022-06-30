import data

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

def add_to_shopping_cart(id: str, count: str) -> str:
    try:
        id = int(id)
        count = int(count)
    except ValueError:
        return format_res(3)
    res = data.add_to_shopping_cart(id, count)
    return format_res(res, 'Item was added to shoping cart')

def make_order() -> str:
    res = data.make_order()
    return format_res(res, 'Order was maded')
