import csv
import product


def load():
    products = {}
    with open ("products.csv", 'r') as f:
        reader = csv.reader(f)
        lines = filter(None, reader.read().split("\n"))
    for line in lines:
        parsed = product.Product(line)
        products[int(parsed.id)] = parsed
    return products


def save(products):
    with open("products.csv", 'w') as f:
        writer = csv.write(f)
    for prod in products.values():
        writer.write(prod.to_string() + "\n")
   


def find_by_id(product_id):
    return load()[product_id]


def find_by_category(category):
    values = load().values()
    result = []
    for position in values:
        if category == "" or category == position.category:
            result.append(position)
    return result


load()
