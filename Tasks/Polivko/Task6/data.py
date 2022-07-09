# Реализовать каталог товаров, основанный на шаблоне 3-х слойной архитектуры.
# Пользователь должен иметь возможность просматривать товары из определённой
# категории, добавлять некоторое количество товаров в корзину и делать окончательный заказ.
# Минимальный набор характеристик товара: название, категория, товарный код, цена, (количество на складе).
repo = {1: ("Adidas Forum 84 Low", "sneakers", "101", "400 BLR"),
        2: ("Adidas Ventice Climacool", "sneakers", "102", "400 BLR"),
        3: ("Adidas Astir", "sneakers", "103", "350 BLR"),
        4: ("Adidas Galaxy 5", "sneakers", "104", "400 BLR"),
        5: ("Adidas Adilette Bonega", "sneakers", "105", "500 BLR"),
        6: ("Adidas Crazychaos 2.0", "sneakers", "106", "550 BLR")
        }
basket = {}

def get_all_products():
        return repo.values()

def add_product(code):
        for i in range(1, len(repo.keys()) + 1):
                if code == repo.get(i)[2]:
                        basket[i] = repo.get(i)
        return basket

def remove_product(code): 
        for k,v in list(basket.items()):
                if code == v[2]:       
                        return basket.pop(k)
        

def get_order():

        return basket.values()

def final_sum():
        final_sum = 0
        for i in basket.values():
                final_sum += int(i[-1].split()[0])
        return final_sum
