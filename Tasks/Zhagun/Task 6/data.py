repo=[{'id':101, 'name' :'bodysuit','category':'baby clothes','price' : 25, 'available':20},
    {'id':102, 'name' :'snowsuit','category':'baby clothes','price' : 10, 'available':15},
    {'id':103, 'name' :'romper','category':'baby clothes','price' : 45,'available':10},
    {'id':104, 'name' :'dress ','category':'womens clothing','price' : 50,'available':22},
    {'id':105, 'name' :'cardigan','category':'womens clothing','price' : 40,'available':7},
    {'id':106, 'name' :'cocktail dress','category':'womens clothing','price' : 70,'available':11},
    {'id':107, 'name' :'suit','category':'mens clothing','price' : 150,'available':18},
    {'id':108, 'name' :'shirt ','category':'mens clothing','price' : 50,'available':9},
    {'id':109, 'name' :'sweater ','category':'mens clothing','price' : 45,'available':13}]

def get_all_repo():
    return repo

def  show_clothes(id):
    for items in repo:
        if items['id']==id:
            return items
basket=[]
total_price=0
def add_item(id,quantity):
    id_items = show_clothes(id)
    id_items['quantity'] = quantity
    if id_items['quantity']<=id_items['available']:
        id_items['available']-=quantity
        basket.append(id_items)
        return basket
    else:
        return f'Expected no more than {id_items["available"]}items'
def len_bascet():
    return f'{len(basket)} items'
def get_receipt():
   return basket.copy()
def remove_item(id):
    for items in basket:
        if items['id']==id:
            return f' Deleted:{basket.pop(basket.index(items))}'
        else:    
            return 'No id in the basket' 

def clean_basket():
    basket.clear()
    return('Basket is empty')