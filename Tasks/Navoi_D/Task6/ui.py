import bl
import data

def ask(message):
    return input(f"{message}:\n").lower() 

# a function wich shows all catalog    
def show_all_catalog():
    return print(bl.get_all_catalog())

# a function wich shows product categories 
def get_product_categories():
    return bl.get_product_categories()

# a function which ask product category
def get_product_category():
    choose_category = ask("enter category")
    return choose_category 

# a function which shows products names in entering (choosing) category 
def get_list_product_name():
    choose_category = get_product_category()
    m = bl.get_list_product_name(choose_category)
    return print(f"we have next products in your category: {m}")

# a function which ask product name
def get_product_name():
    product_name = ask("enter name product")
    return product_name

# a function  which shows the price for unit and trade code of a product depending on the entered product name
def get_product_price():
    choose_category = get_product_category()
    product_name = get_product_name()
    return bl.get_product_price(choose_category, product_name)

# a function which can get quantity products in stock
def get_quantity():
    choose_category = get_product_category()
    product_name = get_product_name()
    return bl.get_quantity(choose_category, product_name)

# a function which ask the desired quantity of products for adding to shopping basket
def need_quantities():
    need_quantity = int(input("Enter the desired quantity of products:\n"))
    return need_quantity

# a function which ask the desired remove quantity of products from shopping basket
def removed_quantity1():
    removed_quantity = int(input("Enter the desired remove quantity of products:\n"))
    return removed_quantity 

# a function which add quantity product to shopping basket  
def add_quantity_product_to_basket():
    choose_category = get_product_category()
    product_name = get_product_name()
    need_quantity = need_quantities()
    return bl.compare_quantities(choose_category, product_name, need_quantity)

# a function which remove quantity product from shopping basket
def remove_quantity_product_from_basket():
    product_name = get_product_name()
    removed_quantity = removed_quantity1()
    return bl.remove_quantity_product_from_basket(product_name, removed_quantity)


def total_basket_and_cost():
    return bl.total_basket_and_cost()

def main_flow():
    while True:
        operation = input("""Enter options:
        0. Exit 
        1. Show all catalog
        2. Get products from category
        3. Get product price, code, unit by name product
        4. Get quantity product in stock 
        5. Add quantity product to basket
        6. Remove any quantity product from basket
        7. View total cost product in basket
                """)
        if operation == '0':
            break
        elif operation == '1':
            show_all_catalog()
        elif operation == '2':
            get_list_product_name()
        elif operation == '3':
            get_product_price()
        elif operation == '4':
            get_quantity()
        elif operation == '5':
            add_quantity_product_to_basket()
        elif operation == '6':      
            remove_quantity_product_from_basket()
        elif operation == '7': 
            total_basket_and_cost()    
            





    
