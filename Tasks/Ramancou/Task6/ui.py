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


def pretty_stars():
    bl.get_pretty()
    

def main_flow():
    """
    Home page
    """
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
                try:
                    while True:
                        clear_terminal()
                        
                        [print(*i) for i in show_first_category_page()]
                        pretty_stars()
                        user_input_1 = input("Press enter to come back\nChoose the category: ")
                        if user_input_1 == "": break
                      
                        """
                        Main category selection page.
                        Here the user selects the main direction of the search for the product of interest to him.

                        """

                        while True:
                            
                            second = show_second_category_page(int(user_input_1))
                            
                            clear_terminal()
                            
                            [print(*i) for i in second]
                            
                            pretty_stars()
                            user_input_2 = input("Press enter to come back\nChoose the category: ")

                            """
                            Main catalog subcategory page
                            """

                            if user_input_2 == "": break

                            while True:
                                clear_terminal()
                                result = show_third_category_page(int(user_input_1), int(user_input_2))
                                if result:
                                    [print(*i) for i in result]
                                    pretty_stars()
                                    user_input_3 = input("Press Enter to come back\nChoose a product: ")

                                else:
                                    print("Sorry this category temporary is not exists\n")
                                    user_input_3 = input("Press enter to continue: ")

                                
                                """
                                List of all products in the selected category
                                """
                                if user_input_3 == "": break

                                while True:
                                    clear_terminal()
                                    full_prod_info = (show_product_info(int(user_input_1), int(user_input_2), int(user_input_3)))
                                    print(format_info(full_prod_info))
                                    pretty_stars()
                                    print("Press 1 to add items to the shopping cart\nPress 2 to view shopping cart\nEnter to go back")
                                    user_input_4 = input("Choose to continue: ")

                                    """
                                    The page where the user interacts with the cart

                                    """

                                    if user_input_4 == "": break

                                    elif int(user_input_4) == 1:
                                        clear_terminal()
                                        add_product(full_prod_info)
                                        print("You successfully add new item in your cart!")
                                        pretty_stars()
                                        print("Press 2 to view shopping cart")
                                        user_input_5 = input("Enter to continue: ")
                                        
                                        if user_input_5 == '': break
                                    
                                        elif int(user_input_5) == 2:
                                            show_cart()

                                    elif int(user_input_4) == 2:
                                        show_cart()


                except (IndexError,KeyError):
                    clear_terminal()
                    inp = input(
                        "Please select a category from the suggested range!\n\nPress enter to continue: ")

                except ValueError:
                    inp = input(
                        "Please enter a number or 'q' to return\nPress enter to continue: ")



            elif operation == 2:
                show_cart()

            elif operation == 3:
                print("Have a nice day!")
                break

            elif operation == 4:
                clear_terminal()
                print(
                    f"Information:\n"
                    f"\nThe database of this project was obtained from the gastronomia.by website using web-scraping on 28/06/2022"
                    f"\nlink - https://gastronomia.by/\n")
                inp = input("Press Enter to continue: ")

        
    except ValueError:
        main_flow()



if __name__ == "__main__":
    main_flow()
