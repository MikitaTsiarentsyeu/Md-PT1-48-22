import bl
def show_all_products():
    print(bl.get_all_products())

def add_shoping(number, quantity):
    products = (bl.add_product(number, quantity))
    if products == False:
        print ('\n You have entered an incorrect item or quantity.')
    else:
        print ('\n'.join([f'\n Name - {c["name"]}: \n Number - {c["number"]}: \n Price - {c["price"]}BYN: \n Stock - {c["count_in_stock"]}: \n Category - {c["product_category"]}\n' for c in products]))

def show_cart():
    print(bl.open_cart())

def checkout():
    print(bl.final_order())

def remove_cart(number):
    print(bl.remove_product(number))

def clean():
    print(bl.clean())

def main_flow():
    while True:

        action = input("""
        1. All goods
        2. Add to cart
        3. Show item in cart
        4. Checkout
        5. Empty cart
        0. Exit
        \n Select the desired operation:
        """)
        
        if action == '1':
            show_all_products()
        elif action == '2':
            number = int(input('Enter the number of the required product:'))
            quantity = int(input('Enter the required quantity of goods:'))
            add_shoping(number, quantity)
        elif action == '3':
            show_cart()
        elif action == '4':
            checkout()
        elif action == '5':
            clean()
        elif action == '0':
            print ("Sorry if we couldn't help you.")
            break
        else:
            print('Invalid operation')


