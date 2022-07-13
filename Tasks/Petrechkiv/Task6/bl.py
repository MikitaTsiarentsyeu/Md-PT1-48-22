import datab


def get_categories():
    res = datab.get_categories()
    categories_from_catalog = "\n".join([f"{x}" for x in res])
    return f"This are categories from our catalogue:\n{categories_from_catalog}"


def products(choose_category):
    try:
        res = datab.get_products(choose_category)
        products_from_category = "\n".join(
            [f"{x}: product key = {res[x][0]}, price = {res[x][1]}, quantity = {res[x][2]}" for x in res])
        return f"This are products from category {choose_category}:\n{products_from_category}"
    except NameError as err:
        return str(err)


def get_basket():
    if not datab.get_basket():
        return "Your basket "
    else:
        res = datab.get_basket()
        products_in_basket = "\n".join([f"{x}: total price = {res[x][0]}, quantity = {res[x][1]}" for x in res])
        return f"Your basket:\n{products_in_basket}"


def add_to_basket(choose_category, choose_product, choose_quantity):
    try:
        choose_quantity_valid(choose_quantity)
    except ValueError:
        return "The quantity must consist of digits"
    except RuntimeError as err:
        return str(err)
    try:
        datab.add_to_basket(choose_category, choose_product, choose_quantity)
        return "The product was added to your basket"
    except NameError as err:
        return str(err)
    except RuntimeError as err:
        return str(err)


def remove_from_basket(choose_product, choose_quantity):
    try:
        choose_quantity_valid(choose_quantity)
    except ValueError:
        return "The quantity must consist of digits"
    except RuntimeError as err:
        return str(err)
    try:
        datab.remove_from_basket(choose_product, choose_quantity)
        return "The product was removed from your basket"
    except NameError as err:
        return str(err)
    except RuntimeError as err:
        return str(err)


def final_buy():
    try:
        datab.final_buy()
        return "Your purchase is complete"
    except RuntimeError as err:
        return str(err)


def choose_quantity_valid(n):
    n = int(n)
    if n <= 0:
        raise RuntimeError("The quantity must be positive value")
