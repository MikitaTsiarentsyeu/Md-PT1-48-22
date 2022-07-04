import bl

def check_user():
    bl.create_cart()
    while True:
        operation = input("""Enter who are you?
1. Admin
2. Customer
0. Exit
""")
        if operation == '0':
            break
        elif operation == '1':
            if bl.check_admin():
                admin_menu()
            else:
                print("You are not Admin!")
        elif operation == '2':
            menu_customer()

def admin_menu():
    while True:
        operation = input("""Admin menu:
1. Create product
2. Delete product
0. Exit
""")
        if operation == '0':
            break
        elif operation == '1':
            print(bl.create_product())
        elif operation == '2':
            print(bl.get_products())
            id = input("Enter id product for delete it, 0 if you change your mind: ")
            if id == "0":
                continue
            else:
                print(bl.delete_product(id))
   

def menu_customer():
    while True:
        operation = input("""What would you like?
1. View the products by categories
2. View products in cart
3. Place your order
0. Exit
""")
        if operation == '0':
            break
        elif operation == '1':
            print(bl.view_category())
            category_id = input("Enter category: ")
            print(bl.get_products(category_id = category_id))
            while True:
                id = input("Add something to the cart? If yes, enter an ID, if no, enter 0.\n")
                if id == '0':
                    break
                else:
                    count = input("Enter count: ")
                    print(bl.add_to_cart(id, count))
        elif operation == '2':
            print(bl.get_products(data_table="cart" ,category_id="all"))
        elif operation == '3':
            print(bl.place_order())
