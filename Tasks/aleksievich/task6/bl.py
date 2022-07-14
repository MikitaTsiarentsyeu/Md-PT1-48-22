import data

def get_all():
    autoparts = data.get_all_price()
    return '\n'.join([f'| {d["category"]:>38} | {d["fits to"]:>43} | {d["OE"]:>11} | {d["article"]:>14} | {d["price Eur"]:>9} |'for d in autoparts])
def category_autoparts(category_name):
    autoparts_by_category = data.get_category_price(category_name)
    res_list = []
    for product in autoparts_by_category:
        if product["category"] == category_name:
            res_list.append(product)
    return '\n'.join([f'| {d["category"]:>38} | {d["fits to"]:>43} | {d["OE"]:>11} | {d["article"]:>14} | {d["price Eur"]:>9} |' for d in res_list])

def add_product(article, quantity:int):
    res = data.add_product_to_basket(article, quantity)
    return res

def show_cart():
    goods = data.get_cart()
    print("Your current cart:")
    return "\n".join([f"{i[0]} with price - {i[1]}Eur and quantity - {i[2]}pcs" for i in goods])

def print_order():
    order = data.print_order()
    print("""                       INVOICE
---------------------------------------------------------    
|  ARTICLE  |  PRICE, Eur  | QUANTITY,pcs | AMOUNT, Eur |
---------------------------------------------------------""")
    return "\n".join([f"| {i[0]:>9} | {i[1]:>12} | {i[2]:>12} | {int((float(i[1])*i[2])*100)/100:>11} |" for i in order])
#Thanks for buying 