import data
 
def get_all():
    all=data.get_all_repo()
    return '\n'.join([f'Id: {d["id"]}\nName: {d["name"]}\nCategory: {d["category"]} \nPrice: {d["price"]} BYN\nAvailable: {d["available"]} \n' for d in all])
def category_clothes(id):
    res = data.show_clothes(id)
    if res:
        return '\n'.join([f' {k.capitalize()} : {v}' for k,v in res.items()])
    else:
        return 'There is no items with this category',id
def add_products(id,quantity):
    return data.add_item(id,quantity)
def show_cart():
    return data.len_bascet()
def remove_items(id):
    return data.remove_item(id)

def get_order():
 receipt = data.get_receipt()
 view = '\n'.join([f' Name: {d["name"]} {d["price"]}BYN*{d["quantity"]} ={d["price"]*d["quantity"]} BYN ' for d in receipt])
 total = [i['price']*i['quantity'] for i in receipt]
 return f'{view}\n Total: {sum(total)} BYN'

def clean():
   return data.clean_basket()