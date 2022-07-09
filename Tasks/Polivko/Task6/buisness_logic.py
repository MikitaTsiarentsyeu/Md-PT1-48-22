import data

def get_all():
    products = data.get_all_products()
    return "\n".join([f"Name - {i[0]} \nCategory - {i[1]} \nCode - {i[2]} \nPrice - {i[3]}\n" for i in products])

def order():
    goods = data.get_order()
    summ = data.final_sum()
    print(f"Invoice: total price - {summ}")
    return "\n".join([f"Name - {i[0]} - {i[3]}" for i in goods])

def show():
    goods = data.get_order()
    print("Your current order:")
    return "\n".join([f"{i[0]} with price - {i[3]} --product code - {i[2]}--" for i in goods])


def add_goods(code):
    res = data.add_product(code)
    if res:
        return "The product added to basket"
    else:
        return "Something went wrong"

def del_product(code):
    res = data.remove_product(code)
    if res:
        return "The product remove from the basket"
    else:
        return "Something went wrong"
