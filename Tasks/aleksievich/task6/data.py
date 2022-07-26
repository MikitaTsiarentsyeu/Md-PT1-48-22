import csv

category_title = "category"
fits_to_title = "fits to"
OE_title = "OE"
article_title = "article"
price_title = "price Eur"
headlines = [category_title,fits_to_title,OE_title,article_title,price_title]
price = []
basket = []


with open("data.csv", "r") as f:
    reader = csv.DictReader(f,headlines,delimiter=";")
    for i in reader:
        price.append(i)

def get_all_price():
    return price

def get_category_price(category_name):
    res_list = []
    for product in price:
        if product[category_title] == category_name:
            res_list.append(product)
    return res_list

def add_product_to_basket(code, quantity:int):
    for product in price:
        if code == product[article_title]:
            basket.append([product[article_title],product[price_title], quantity])
            return True
    return False

def get_cart():
    return basket

def print_order():
    return basket
  