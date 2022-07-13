import bl
import random as rd

def data_entry(massage:str,num=1):
    '''Function for user input of values.\n
    massage - the message that is displayed to the user.\n
    num - 1 (the entered value will be reduced to int) or 2 (the entered value will be str).'''
    if num == 1:
        return int(input(f'\n{massage}\n'))
    elif num == 2:
        return input(f'\n{massage}\n')

def massage_mistake(num:int): 
    '''The function outputs an error message.\n
    If num is 1 - the user specifies an invalid value.\n
    If num is 2 - the user does not use numbers.\n
    If num is 3 - no data was found for the entered query.'''
    if num == 1:
        print("\nUnfortunately, you made a mistake and entered an invalid value. Try again.")
    elif num == 2:
        print('\nUnfortunately, you made a mistake. You have to enter only numbers.')
    elif num == 3:
        print('\nUnfortunately, nothing was found for the entered query.')

def look_all_books(): 
    '''The function sends a request to output the entire catalog of books.''' 
    print(bl.show_books())

def found_elements(index:int): 
    '''Request to check whether the entered data is in the catalog.\n
    index - index in data.'''
    return bl.found(index)

def found_name(list_name:list,choise:str): 
    '''The function for the part of the name is looking for the full.\n
    list_name - the list in which the search will take place.\n
    choise - data entered by the user for the search.'''
    for elem in range(len(list_name)):
        if choise.lower() in list_name[elem].lower():
            return list_name[elem]
        else:
            continue
    return False

def searching(index:int, massage:str): 
    '''Search for information on the user's request.\n
    index - index in data.\n
    massage - the message that is displayed to the user.'''
    list_name = list(found_elements(index))
    while True:
        choise = data_entry(massage,2)
        name = found_name(list_name,choise)
        if name is False:
            massage_mistake(3)
            continue
        break
    return name    

def look_book_by_name(value): 
    '''The function sends a request to display data about a specific book'''
    print(bl.show_book_by_name(value))

def look_authors_of_books(value: str): 
    '''The function sends a request to display all books written by the selected author.''' 
    print(bl.show_author(value))

def look_series_of_book(value: str): 
    '''The function sends a request to display all books from the same series.'''
    print(bl.show_series(value))

def add_books(): 
    '''The function sends a request toadd a book to cart.''' 
    try:
        article = data_entry('What is the article of the selected book?',2)
        quantity = data_entry('How many books do you want to order?')
        print(bl.add_books(article,quantity))
    except:
        massage_mistake(2)
    
def look_of_cart(): 
    """The function sends a request to display all books available in the cart."""
    print(bl.show_cart())

def remove_books(): 
    '''The function sends a request to delete the selected book from the cart.'''
    try:
        number = data_entry('Which book number in the cart do you want to delete?',2)
        print(bl.remove_books(number))
    except:
        massage_mistake(2)

def clean_of_cart(): 
    '''The function of sending a request to clear the cart.'''
    print(bl.cleaning())

def place_order(): 
    '''The function sends a request to place an order.'''
    print(bl.place_order())

def redact_order(): 
    '''The function sends a request to change the number of books in the cart.'''
    try:
        number = data_entry('Which book number in the cart do you want to redact?',2)
        count = data_entry('What is the correct number of books?')
        print(bl.redact_order(number, count))
    except:
        massage_mistake(2)

def number_of_order(): 
    '''The function generates the order number.'''
    print(rd.randint(100000, 1000000))

    """"""


def choise_of_buyer(): 
    while True:
        choise_buyer = data_entry('''
        You can choise:
        0. Exit
        1. Viewing all books
        2. Viewing the names of all authors or the titles of all book series
        3. Search for books by name
        4. Search for books by author 
        5. Search for books by series
        6. Add books to the cart
        7. Viewing books in the cart
        8. Delete books from the cart
        9. Place or redact you order
        ''', 2)
        if choise_buyer == '0':
            break
        elif choise_buyer == '1':
            look_all_books()
        elif choise_buyer == '3':
            look_book_by_name(searching(2,'Enter the full title of the book or part of it:'))
        elif choise_buyer == '2':
            while True:
                choise = data_entry('''
                1. Viewing the names of all authors
                2. Viewing the titles of all book series
                3. Cancel
                ''', 2)
                if choise not in ['1','2','3']:
                    massage_mistake(1)
                    continue
                break
            if choise == '1':
                print (", ".join(found_elements(0)))
            elif choise == '2':
                print(", ".join(found_elements(1)))
            elif choise == '3':
                continue
        elif choise_buyer == '4':
            look_authors_of_books(searching(0,'Enter the full name of author or part of it:'))  
        elif choise_buyer == '5':
            look_series_of_book(searching(1,'Enter the full name of the title of book series or part of it:'))
        elif choise_buyer == '6':
            add_books()
        elif choise_buyer == '7':
            look_of_cart()
        elif choise_buyer == '8':
            while True:
                choise = data_entry('''
                1. Delete one book from the cart
                2. Clean of cart
                3. Cancel
                ''', 2)
                if choise not in ['1','2','3']:
                    massage_mistake(1)
                    continue
                break
            if choise == '1':
                remove_books()
            elif choise == '2':
                clean_of_cart()
            elif choise == '3':
                continue
        elif choise_buyer == '9':
            while True:
                choise = data_entry('''
                1. Placing an order
                2. Changing an order
                3. Cancel
                ''', 2)
                if choise not in ['1','2','3']:
                    massage_mistake(1)
                    continue
                break
            if choise == '1':
                while True:
                    confirm = data_entry('''
                    1. Confirm the order 
                    2. Cancel  
                    ''', 2)
                    if confirm not in ['1','2']:
                        massage_mistake(1)
                        continue
                    break
                if confirm == '1':
                    place_order()
                    print('\nYour order has been successfully placed. Payment upon receipt. Your order number is: ')
                    number_of_order()
                elif confirm == '2':
                    continue
            elif choise == '2':
                redact_order()
            elif choise == '3':
                continue
        else:
            massage_mistake(1)