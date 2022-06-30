data = {
    #id: [name, category, price, number of items]
    1: ['Name1', 'Category1', 13, 10],
    2: ['Name2', 'Category1', 20, 2],
    3: ['Name3', 'Category2', 10, 7],
}
# contains item (id, amount)
shoping_card = []

def get_all_categories() -> set:
    categories = set()
    for v in data.values():
        categories.add(v[1])
    return categories


def get_all_in_category(category_name: str) -> list:
    res_list = []
    for k, v in data.items():
        if v[1] == category_name:
            res_list.append((k, *v))
    return res_list


def add_to_shopping_cart(id: int, count: int) -> int:
    try:
        required_data = data[id]
    except KeyError:
        return 1
    
    if required_data[3] < count:
        return 2
    else:
        shoping_card.append((id, count))
        return 0

def make_order() -> int:
    global shoping_card
    if len(shoping_card) == 0:
        return 4
    for id, count in shoping_card:
        if data[id][3] < count:
            shoping_card = []
            return 2
        else:
            data[id][3] -= count
    shoping_card = []
    return 0
    
