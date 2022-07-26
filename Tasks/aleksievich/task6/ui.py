import bl

def ask(message):
    return input(f"{message}:\n")

def show_all():
    print(bl.get_all())

def show_by_category():
    category = ask("""In the assortment of online store you will be able to buy
    autoparts of the following categories:
                      ВОЗДУШНЫЙ ФИЛЬТР
                      ДИСК ТОРМОЗНОЙ
                      КОЛОДКИ ТОРМОЗНЫЕ БАРАБАННЫЕ
                      КОЛОДКИ ТОРМОЗНЫЕ ДИСКОВЫЕ
                      НАКОНЕЧНИК РУЛЕВОЙ
                      НАСОС ВОДЯНОЙ
                      НАТЯЖИТЕЛЬ ПОЛИКЛИНОВОГО РЕМНЯ
                      ОБГОННАЯ МУФТА ГЕНЕРАТОРА
                      РОЛИК НАПРАВЛЯЮЩИЙ ПОЛИКЛИНОВОГО РЕМНЯ
                      РОЛИК РЕМНЯ ГРМ
                      САЛОННЫЙ ФИЛЬТР
                      ТЯГА РУЛЕВАЯ
                      ТЯГА СТАБИЛИЗАТОРА
                      ЩЕТКА СТЕКЛООЧИСТИТЕЛЯ

                      Type category name""")
    print(bl.category_autoparts(category))

def add_product():
    article = input("Enter the article of product\n")
    quantity = int(input("Enter the quantity of product\n"))
    print(bl.add_product(article, quantity))

def show_cart():
    print(bl.show_cart())

def print_order():
    print(bl.print_order())

def main_flow():
    while True:
        operation = input("""Enter the number of operation:
        0. Exit
        1. Show all catalog
        2. Show all autoparts in category
        3. Add product to shopping cart
        4. Show order
        5. Place an order
        """)
        if operation == "0":
            break
        elif operation == "1":
            show_all()
        elif operation == "2":
            show_by_category()
        elif operation == "3":
            add_product()
        elif operation == "4":
            show_cart()
        elif operation == "5":
            print_order()
            break