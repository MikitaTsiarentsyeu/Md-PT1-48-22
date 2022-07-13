import data

def get_category():
    cat = data.category()
    return '\n'.join([f"Category: {i[1]} - {i[0]}; SKU - {i[2]}; Price - {i[3]} BYN; Qty - {i[4]}" for i in cat])

def order_add():
    res = data.order_add()
    for k,v in res.items():
        for s,t in data.full_cat.items():
            if k == s:
                result = f"{t[0]} - QTY: {v} - Price per item: {t[3]} BYN.\nItem ordered.\n"
    return result

def final_order():
    final_price = 0
    for k,v in data.order.items():
        price = float(data.full_cat[k][3]) * v
        final_order = f"{data.full_cat[k][0]} - qty: {v} - {price:3.2f} BYN"
        final_price += price 
        print(final_order)
    return f'\nTotal price: {final_price:3.2f} BYN.\n'