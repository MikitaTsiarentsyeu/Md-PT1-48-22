import product_dao


def purchase(product_cart):
    products = product_dao.load()

    for product_id in product_cart.products:
        if products[product_id].amount < product_cart.products[product_id]:
            print("not enough products on store: " + products[product_id].name +
                  ". Only " + str(products[product_id].amount) + " left when required " + str(
                product_cart.products[product_id]))
            return False
    for product_id in product_cart.products:
        products[product_id].amount = products[product_id].amount - product_cart.products[product_id]
        product_dao.save(products)

    print("===BUOGHT===")
    for product_id in product_cart.products:
        print(products[product_id].name, '->', product_cart.products[product_id])
    return True
