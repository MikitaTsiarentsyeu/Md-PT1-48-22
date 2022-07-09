import decimal

category_of_product = {1 : 'Apple products', 2: 'Microsoft products', 3: 'XIAOMI products'}
products = [
{'name' : 'Apple Iphone', 'category' : 1, 'code' : 1, 'price_usd' : decimal.Decimal('1100.10')},
{'name' : 'Apple AirPods', 'category' : 1, 'code' : 2, 'price_usd' : decimal.Decimal('50.05')},
{'name' : 'Windows phone', 'category' : 2, 'code' : 3, 'price_usd' : decimal.Decimal('100.1')},
{'name' : 'Windows notebook', 'category' : 2, 'code' : 4, 'price_usd' : decimal.Decimal('777.77')},
{'name' : 'Xiaomi Redmi', 'category' : 3, 'code' : 5, 'price_usd' : decimal.Decimal('199.99')},
{'name' : 'Xiaomi charger', 'category' : 3, 'code' : 6, 'price_usd' : decimal.Decimal('9.99')}]
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