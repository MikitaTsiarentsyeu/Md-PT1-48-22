import UI
import json

# keys are SKUs, SKUs are in values as well


with open("cat_drinks.json", 'r') as f1:
    cat_drinks = json.load(f1)

with open("cat_snacks.json", 'r') as f2:
    cat_snacks = json.load(f2)

with open("cat_chocolate.json", 'r') as f3:
    cat_chocolate = json.load(f3)

full_cat = cat_drinks | cat_snacks | cat_chocolate 

order = {}    # {sku: qty}

def category():
    if UI.operation == 1:
        return cat_drinks.values()
    elif UI.operation == 2:
        return cat_snacks.values()
    elif UI.operation == 3:
        return cat_chocolate.values()

def order_add():
    new_qty = UI.qty
    k = UI.sku
    if k not in order.keys():
        order[k] = int(new_qty)
        full_cat[k][4] =int(full_cat.get(k)[4]) - int(new_qty)
        return order
    else:
        order[k] += int(new_qty)
        full_cat[k][4] =int(full_cat.get(k)[4]) - int(new_qty)
        return order