import data

def get_all_products():
    all_products = data.get_all_products_repo()
    return ''.join([f'Name - {d["name"]}: Number - {d["number"]}: Price - {d["price"]}BYN: Stock - {d["count_in_stock"]}: Category - {d["product_category"]}\n' for d in all_products])

def add_product(number, quantity):
    return data.number_products(number, quantity)

def open_cart():
    return data.bascet()

def remove_product(number):
    return data.remove_product(number)

def final_order():
    invoice = data.get_an_invoice()
    view = '\n'.join([f'\n Name - {d["name"]}: \n Price - {d["price"]} (BYN) * { d["quantity"]} = {d["price"]*d["quantity"]} BYN ' for d in invoice])
    total = [i['price']*i['quantity'] for i in invoice]
    return f'{view}\n Total: {round(sum(total), 2)} BYN'

def clean():
    return data.empty_trash()