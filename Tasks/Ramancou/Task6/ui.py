import bl


def clear_terminal():
    return bl.clear()

def show_first_category_page():
    return bl.get_first_page()


def show_second_category_page(number, opt=None):
    return bl.get_second_page(number)


def show_third_category_page(number1, number2):
    return bl.get_third_page(number1, number2)


def show_product_info(number1, number2, number3):
    return bl.get_third_page(number1, number2, number3)
    

def format_info(info_tuple):
    return bl.get_format_info(info_tuple)


def add_product(item: tuple):
    bl.add_user_item(item)


def show_cart():
    bl.get_cart_data()


def pretty_stars()->str:
    bl.get_pretty()
 

def main_page():
    try:
        while True:
            clear_terminal()
            print(
            "Welcome to the shop!",
            "Enter the number of operation:",
            " 1.Show whole catalog",
            " 2.Show your cart",
            " 3.Exit",
            " 4.Information",sep='\n')
            operation = int(input("Enter number: "))

            if operation == 1:
                show_first_catalog_page()

            elif operation == 2:
                try:
                    show_cart()
                except:
                    ent = input("Your Cart is empty to continue shopping press enter: ")

            elif operation == 3:
                clear_terminal()
                print("Have a nice day!")
                break 

            elif operation == 4:
                show_information_about_script()

    except ValueError:
        main_page()


def show_first_catalog_page():
    try:
        while True:
            clear_terminal()
            [print(*i) for i in show_first_category_page()]
            pretty_stars()
            user_input_1 = input("Press enter to come back\nChoose the category: ")
            if user_input_1 == "": break
            else: view_second_category_page(int(user_input_1))

    except (IndexError,KeyError):
        clear_terminal()
        inp = input(
            "Please select a category from the suggested range!\n\nPress enter to continue: ")

    except ValueError:
        clear_terminal()
        inp = input(
            "Please, choose the correct number!\n\nPress to continue: ")
        show_first_catalog_page()


def view_second_category_page(user_input_1:int)->None:

    while True:
        second_page_list = show_second_category_page(user_input_1)
        clear_terminal()
        [print(*i) for i in second_page_list]
        pretty_stars()
        user_input_2 = input("Press enter to come back\nChoose the category: ")
        if user_input_2 == "": break
        else: view_last_page(int(user_input_1),int(user_input_2))


def view_last_page(user_input_1:int,user_input_2:int)->None:

    while True:
        clear_terminal()
        result = show_third_category_page(user_input_1, user_input_2)
        if result:
           [print(*i) for i in result]
           pretty_stars()
           user_input_3 = input("Press Enter to come back\nChoose a product: ")
           if user_input_3 == "": break
           show_full_information_about_product(user_input_1, user_input_2, int(user_input_3))
        else:
           print("Sorry this category temporary is not exists\n")
           user_input_3 = input("Press enter to continue: ")
           break


def show_full_information_about_product(user_input_1:int, user_input_2:int, user_input_3:int)->None:
    while True:
        clear_terminal()
        full_prod_info = show_product_info(user_input_1, user_input_2, user_input_3)
        print(format_info(full_prod_info))
        pretty_stars()
        print("Press 1 to add items to the shopping cart\nPress 2 to view shopping cart\nEnter to go back")
        user_input_4 = input("Choose to continue: ")

        if user_input_4 == "": break

        elif int(user_input_4) == 1:
            clear_terminal()
            add_product(full_prod_info)
            print("You successfully add new item in your cart!")
            pretty_stars()
            user_input_5 = input("Press 2 to view shopping cart\nEnter to continue: ")
            
            if user_input_5 == '': break
        
            elif int(user_input_5) == 2:
                show_cart()

        elif int(user_input_4) == 2:
            show_cart()


def show_information_about_script():
    
    clear_terminal()
    print(
        f"Information:\n"
        f"\nThe database of this project was obtained from the gastronomia.by website using web-scraping on 28/06/2022"
        f"\n\nlink - https://gastronomia.by/")
    pretty_stars()
    inp = input("Press Enter to continue: ")

                
if __name__ == "__main__":
    main_page()
