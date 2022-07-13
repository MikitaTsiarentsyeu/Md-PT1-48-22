import ui
cat_wine = {
    "480":["Riesling", "wine", "480", "25.9", "5"],
    "450":["Sauvignon", "wine", "450", "30.2", "10"],
    "460":["Chardonnay", "wine", "460", "35.3", "15"],
    "470":["Cabernet", "wine", "470", "28.8", "20"]
    }

cat_whisky = {
    "390":["Jameson", "whisky", "390", "80.3", "21"],
    "360":["Chivas", "whisky", "360", "95.4", "14"],
    "370":["Auchentoshan", "whisky", "370", "150.8", "18"],
    "380":["Dalmore", "whisky", "380", "208.9", "15"]
}

full_cat = cat_wine | cat_whisky 

order = {}   

def category():
    if ui.operation == 1:
        return cat_wine.values()
    elif ui.operation == 2:
        return cat_whisky.values()


def order_add():
    new_qty = ui.qty
    k = ui.sku
    if k not in order.keys():
        order[k] = int(new_qty)
        full_cat[k][4] =int(full_cat.get(k)[4]) - int(new_qty)
        return order
    else:
        order[k] += int(new_qty)
        full_cat[k][4] =int(full_cat.get(k)[4]) - int(new_qty)
        return order