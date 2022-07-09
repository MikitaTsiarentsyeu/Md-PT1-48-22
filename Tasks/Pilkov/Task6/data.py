import csv
from os import path as os_path, replace as os_replace
from typing import Generator

DATA_FILE = 'data_file.csv'
DATA_PATH = os_path.join(os_path.dirname(__file__), DATA_FILE)

def generate_products_data() -> Generator:
    with open(DATA_PATH, 'r') as csv_file:
        data = csv.DictReader(csv_file)
        for line in data:
            yield line


def get_all_categories() -> set:
    categories = set()
    data = generate_products_data()
    for product in data:
        categories.add(product['category'])
    return categories


def get_all_in_category(category_name: str) -> list:
    res_list = []
    data = generate_products_data()
    for product in data:
        if product['category'] == category_name:
            res_list.append(list(product.values()))
    return res_list

def check_is_product_enouth(product_id: int, count: int) -> int:
    data = generate_products_data()
    required_data = None
    for product in data:
        if int(product['id']) == product_id:
            required_data = product
    
    if required_data is None:
        return 1
    elif int(required_data['items']) < count:
        return 2
    else:
        return 0


def make_order(products_to_order: dict) -> int:
    if not products_to_order:
        return 4

    TMP_PATH = os_path.join(os_path.dirname(__file__), 'tmp.csv')

    with open(DATA_PATH, 'r') as csv_data_file:
        data = csv.DictReader(csv_data_file)
        header = data.fieldnames
        with open(TMP_PATH, 'w') as csv_new_file:
            writer = csv.DictWriter(csv_new_file, header)
            writer.writeheader()

            for data_file_line in data:
                product_id = int(data_file_line['id'])
                if product_id in products_to_order:
                    total_count = int(data_file_line['items']) - products_to_order[product_id]
                    if total_count < 0:
                        return 5
                    else:
                        data_file_line['items'] = str(total_count)

                writer.writerow(data_file_line)
    os_replace(TMP_PATH, DATA_PATH)
    return 0
    
