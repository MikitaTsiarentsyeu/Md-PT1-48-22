import cart
import catalog
import purchase_service


def main():
    user_cart = cart.Cart()
    print("hello dear user. Type 'help' to get command list")
    while True:
        line = input()
        args = list(filter(None, line.split(" ")))
        command = args[0] if len(args) > 0 else "blank"
        if command == 'list':
            category = args[1] if len(args) == 2 else ""
            print("Product list:")
            print("ID".ljust(10) + "NAME".ljust(20) + "CATEGORY".ljust(20) + "PRICE")
            print("=======================================================")
            for p in catalog.show_category(category):
                print(str(p.id).ljust(10) + p.name.ljust(20) + p.category.ljust(20) + str(p.price))
            continue
        if command == 'cart':
            if len(user_cart.products) == 0:
                print("Cart is empty")
                continue
            print("Product in cart:")
            print("ID".ljust(10) + "NAME".ljust(20) + "AMOUNT".ljust(20) + "PRICE".ljust(20) + "TOTAL")
            print("====================================")
            total_price = 0
            for product_id in user_cart.products:
                price_for_position = catalog.price_by_id(product_id) * user_cart.products[product_id]
                print(str(product_id).ljust(10) + catalog.name_by_id(product_id).ljust(20) +
                      str(user_cart.products[product_id]).ljust(20) +
                      str(catalog.price_by_id(product_id)).ljust(20) + str(price_for_position))
                total_price += price_for_position
            print("====================================")
            print("                           TOTAL: " + str(total_price))
            continue

        if command == 'add':
            if len(args) != 3:
                print("add <product_id> <product_amount>")
                continue
            else:
                user_cart.add(int(args[1]), int(args[2]))
                continue
        if command == 'remove':
            if len(args) != 3:
                print("remove <product_id> <product_amount>")
                continue
            else:
                user_cart.add(int(args[1]), -int(args[2]))
                continue
        if command == 'buy':
            if purchase_service.purchase(user_cart):
                user_cart = cart.Cart()
                continue
        if command == 'blank':
            continue
        if command == 'exit':
            break
        else:
            print("Commands:")
            print("          list [category]                     : - show products")
            print("          add <product_id> <product_amount>   : - add products")
            print("          remove <product_id> <product_amount>: - remove products")
            print("          buy                                 : - release cart and order products")
            print("          cart                                : - show items in cart")
            print("          exit                                : - stop shopping")
