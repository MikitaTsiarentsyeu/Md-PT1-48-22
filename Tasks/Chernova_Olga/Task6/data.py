import json

def available(inform): 
    '''If the books are not in stock, the function outputs "Out of stock".'''
    for v in inform.values():
        if v[3][1] == 0:
            v[3][1] = 'Out of stock'

def reading(file_name:str): 
    '''Reads data from a database file.\n
    file_name - name of database'''
    with open(f'{file_name}.json') as f:
        inform = json.load(f)
        return inform

def record(change,file_name): 
    '''Writes data to a database file.'''
    with open(f'{file_name}.json','w') as f:
        json.dump(change, f)

def show_books(): 
    '''The function transmits data about all available books.'''
    inform = reading('catalog')
    available(inform)
    return inform.items()

def show_books_val():
    '''The function transmits data about all available books.'''
    inform = reading('catalog')
    available(inform)
    return inform
    
def calc_of_quantity(article:int,quantity:int): 
    '''The function counts the number of books remaining in stock.\n
    article - article of the book in the data.\n
    quantity - the number of books ordered.'''
    inform = reading('catalog')
    inform[article][3][1] = inform[article][3][1] - quantity
    record(inform,'catalog')
    

def control_count(article:str,quantity:int): 
    '''If there are fewer books in stock than ordered, the function returns an error.\n
    article - article of the book in the data.\n
    quantity - the number of books ordered.'''
    inform = reading('catalog')
    if (int(inform[article][3][1]) is False) or (int(inform[article][3][1]) < quantity):
        return False
    else:
        calc_of_quantity(article,quantity)
        return True

def control_art(article:int):  
    '''The function checks whether the specified article exists.\n
    article - article of the book in the data.'''
    if article in reading('catalog'):
        return True
    else:
        return False

def add_books(article:int,quantity:int): 
    '''The function adds the books selected by the article to the cart.\n
    article - article of the book in the data.\n
    quantity - the number of books ordered.'''
    try:
        inform = reading('catalog')
        buyer_cart = reading('cart')
        new_add = (article,inform[article][0],inform[article][2],[inform[article][3][0],quantity])   
        for i in range(1, len(buyer_cart)+2):
            if str(i) not in buyer_cart:
                buyer_cart[i] = new_add
                record(buyer_cart,'cart')
                break
        return True
    except:
        return False

def show_cart():
    '''The function transmits data about orders in the shopping cart.'''
    buyer_cart = reading('cart')
    if buyer_cart == {}:
        return '-1'
    else:
        return buyer_cart.items()

def control_remove(num:int): 
    '''The function checks whether the specified number exists in the shopping cart.\n
    num - the number of the book in the cart.'''
    buyer_cart = reading('cart')
    if num in buyer_cart:
        return True
    else:
        return False

def control_count_cart(num:int,count:int): 
    '''The function checks whether there are enough books to edit the order.\n
    num - the number of the book in the cart.\n
    count - the number of books ordered.'''
    inform = reading('catalog')
    buyer_cart = reading('cart')
    article = buyer_cart[num][0] 
    if inform[article][3][1] + buyer_cart[num][3][1] < count:
        return False
    else:
        return True

def back_count(num:int): 
    '''The function restores the number of copies of books to the database after the order is canceled one order.\n
    num - the number of the book in the cart.'''
    inform = reading('catalog')
    buyer_cart = reading('cart')
    count = buyer_cart[num][3][1]
    if type(inform[buyer_cart[num][0]][3][1]) is not int:
        inform[buyer_cart[num][0]][3][1] = 0
    inform[buyer_cart[num][0]][3][1] = inform[buyer_cart[num][0]][3][1] + count
    record(inform,'catalog')

def remove_books(number:int): 
    '''The function removes one selected book from the order.\n
    number - the number of the book in the cart.'''
    buyer_cart = reading('cart')
    back_count(number)
    for k in buyer_cart:
        if k == number:
            del buyer_cart[k]
            record(buyer_cart,'cart')
            return True
    return False

def cleaning(): 
    '''The function clears the cart.'''
    buyer_cart = reading('cart')
    buyer_cart.clear()
    record(buyer_cart,'cart')
    

def cleanind_and_return(): 
    '''The function restores the number of copies of books to the database after the order is canceled.'''
    buyer_cart = reading('cart')
    for k in buyer_cart.keys():
        back_count(k)
    cleaning()
    return True

def place_order(): 
    '''The function transmits information about orders in the shopping cart.'''
    buyer_cart = reading('cart')
    return buyer_cart.values()

def redact_order(num:int,count:int): 
    '''The function changes the number of books in the selected order line number.\n
    num - num - the number of the book in the cart.\n
    count - the number of books ordered.'''
    try:
        inform = reading('catalog')
        buyer_cart = reading('cart')
        article = buyer_cart[num][0]
        inform[article][3][1] = inform[article][3][1] + buyer_cart[num][3][1]
        record(inform,'catalog')
        buyer_cart[num][3][1] = count
        calc_of_quantity(article,count)
        record(buyer_cart,'cart')
        return True
    except:
        return False