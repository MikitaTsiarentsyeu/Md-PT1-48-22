import bl
import data

def show_all():
    print(bl.get_all())
def show_by_category(id):
    print(bl.category_clothes(id))
       
def add_shopping_cart(id,quantity):
    print( bl.add_products(id,quantity))
def show_shopping_cart():
    print(bl.show_cart())
def confirm_order():
    print(bl.get_order())
def remove_cart(id): 
    print(bl.remove_items(id))
def clean_cart():
    print(bl.clean())

def main_flow():
    while True:
        chosed_action = input("""Enter the number of your operation:
        0. Exit
        1. Show all 
        2. Search by id
        3. Add to shopping cart
        4. show quantity in cart
        5. Confirm the order
        6. Remove from shoping cart
        7.Clear the cart
        """)
        if chosed_action == '0':
            print('Thanks for shopping. Goodbye !')
            break
        elif chosed_action == '1':
            show_all()
        elif chosed_action == '2':
            id=int(input('Please,enter id of the item:'))
            show_by_category(id)
        elif chosed_action == '3':
            id=int(input('Please,enter id of the item:'))
            quantity = int(input('Please,enter quantity of items: '))
            add_shopping_cart(id,quantity)
        elif chosed_action == '4':
            show_shopping_cart() 
        elif chosed_action == '5':
            confirm_order()
        elif chosed_action == '6':
            id = int(input('Please,enter id of the item: '))
            remove_cart(id)  
        elif chosed_action == '7':
            clean_cart()
        else:
            print('Operation not found ')  
    