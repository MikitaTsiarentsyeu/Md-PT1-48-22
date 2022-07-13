
import decimal

category_of_product = {1 : 'fruits_and_vegetables', 2: 'snacks', 3: 'milk'}
products = [
{'name' : 'banan', 'category' : 1, 'code' : 11, 'price_usd' : decimal.Decimal('1.21')},
{'name' : 'tomato', 'category' : 1, 'code' : 12, 'price_usd' : decimal.Decimal('2.05')},
{'name' : 'chips', 'category' : 2, 'code' : 21, 'price_usd' : decimal.Decimal('0.98')},
{'name' : 'nuts', 'category' : 2, 'code' : 22, 'price_usd' : decimal.Decimal('2.58')},
{'name' : 'butter', 'category' : 3, 'code' : 31, 'price_usd' : decimal.Decimal('1.33')},
{'name' : 'cheese', 'category' : 3, 'code' : 32, 'price_usd' : decimal.Decimal('1.78')}]
basket = []

def get_categories():
    return category_of_product
def get_products(number_of_category):
    return list(filter(lambda product: number_of_category == product['category'], products))

def add_product_to_basket(code, quantity):
    for item in basket:
        if code == item[0]['code']:
            item[1]+=quantity
            return True      
    for product in products:
        if code == product['code']:
            basket.append([product, quantity])
            return True
    return False
    
def get_check():
    return basket