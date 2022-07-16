import data
# a function wich shows all catalog    
def get_all_catalog():
    catalog = data.get_all_catalog()
    return catalog
# a function wich shows product categories 
def get_product_categories():
    m = data.get_product_categories()
    n = ', '.join([str(elem) for elem in m])
    return print(f"we have categories: {n}")

# a function which shows products names in entering (choosing) category 
def get_list_product_name(choose_category):
    m = data.get_list_product_name(choose_category)
    n = ', '.join([str(elem) for elem in m])
    return n
  
# a function  which shows the price for unit and trade code of a product depending on the entered product name   
def get_product_price(choose_category, product_name):
    m = data.get_product_price(choose_category, product_name)
    return print(m)

# a function which can get quantity products in stock
def get_quantity(choose_category, product_name):
    m = data.get_quantity(choose_category, product_name)
    return print(f'{m} kg products in stock')

# a function which add quantity product to shopping basket  
def add_quantity_product_to_basket(choose_category, product_name, need_quantity):
        m = data.add_quantity_product_to_basket(choose_category, product_name, need_quantity)
        product_name = m['product_name']
        product_quantity = m['product_quantity(kg)']
        return print(f'In the basket is {product_name}:  {product_quantity} kg')
    
# a function which compare need quantity and current quantity in stock and change quantity product in Catalog
def compare_quantities(choose_category, product_name, need_quantity):
    if data.compare_quantities(choose_category, product_name, need_quantity) != None:
        return add_quantity_product_to_basket(choose_category, product_name, need_quantity)
    else:
       return print("Your entered quantity more than we have in stock") 
  
# a function which remove quantity product from shopping basket         
def remove_quantity_product_from_basket(product_name, removed_quantity):
            m = data.remove_quantity_product_from_basket(product_name, removed_quantity)
            product_name = m['product_name']
            product_quantity = m['product_quantity(kg)'] 
            if product_quantity > 0:
                return print(f'In the basket is {product_name}:  {product_quantity} kg')
            else:
                return print("quantity more than is in stock")

# a function which return total shopping basket with total cost for quantity of product   
def total_basket_and_cost():
    m = data.total_basket_and_cost()
    product_name = m['product_name']
    need_quantity = m['product_quantity(kg)'] 
    total_cost = m['product_price']
    return print(f'In the basket is {product_name}:  {need_quantity} kg, total cost: {total_cost} Br')
    
  
    
  

