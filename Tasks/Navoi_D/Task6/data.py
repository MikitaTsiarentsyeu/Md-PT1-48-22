import json

# read catalog of products from json file
with open("Catalog.json", 'r') as f:
    products = json.load(f)

# create shopping basket
shopping_basket = {}    

# a function wich shows all catalog    
def get_all_catalog():
    product_dict = json.dumps(products, indent = 2, sort_keys = True)
    return product_dict


# a function wich shows product categories 
def get_product_categories():
    categories  = []
    [categories.append(key) for key in products]
    return  categories

# a function which shows products names in entering (choosing) category    
def get_list_product_name(choose_category):
    for i in get_product_categories() :    
        if i == choose_category:
            list_products_name = [x['product_name'] for x in products[i]]
            return  list_products_name


# a function  which shows the price for unit and trade code of a product depending on the entered product name
def get_product_price(choose_category, product_name):
    for i in products[choose_category]:
        if i["product_name"] == product_name:
            price = i["product_price"]
            code = i["product_code"]
            unut = i["unit_weight(kg)"]
            return f'{product_name}(trade code: {code}) price: {price} Br (for {unut} kg)'


# a function which can get quantity products in stock
def get_quantity(choose_category, product_name):
    for i in products[choose_category]:
        if i["product_name"] == product_name:
            n = i["product_quantity(kg)"]
            return n

# a function which add quantity product to basket 
def add_quantity_product_to_basket(choose_category, product_name, need_quantity):
    for i in products[choose_category]:
        if i["product_name"] == product_name:
           shopping_basket["product_name"] = product_name 
           shopping_basket["product_quantity(kg)"] = need_quantity
           shopping_basket["product_price"] = i["product_price"]
           return shopping_basket
    
# a function which compare need quantity and current quantity in stock and change quantity product in Catalog
def compare_quantities(choose_category, product_name, need_quantity):
    for i in products[choose_category]:
        if i["product_name"] == product_name:
            if need_quantity<=int(i["product_quantity(kg)"]):
                for num in range(len(i)):
                    current_quantity_in_stock = products[choose_category][num]["product_quantity(kg)"]
                    current_quantity_in_stock = current_quantity_in_stock - need_quantity
                    products.get(choose_category)[num]["product_quantity(kg)"] = current_quantity_in_stock
                    with open("Catalog.json", 'w') as f:
                        json.dump(products, f)
                    break 
                return current_quantity_in_stock

# a function which remove quantity product from basket
def remove_quantity_product_from_basket(product_name, removed_quantity):
    if shopping_basket["product_name"] == product_name:
        shopping_basket["product_quantity(kg)"]  = shopping_basket["product_quantity(kg)"] -  removed_quantity 
        return shopping_basket
          
# a function which return total shopping basket with total cost for quantity of product        
def total_basket_and_cost():
    shopping_basket["product_price"] = shopping_basket["product_quantity(kg)"]*shopping_basket["product_price"]   
    return shopping_basket



