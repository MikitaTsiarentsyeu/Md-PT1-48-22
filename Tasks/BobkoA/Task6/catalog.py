import product_dao


def show_category(category):
    return product_dao.find_by_category(category)


def name_by_id(product_id):
    return product_dao.find_by_id(product_id).name


def price_by_id(product_id):
    return product_dao.find_by_id(product_id).price
