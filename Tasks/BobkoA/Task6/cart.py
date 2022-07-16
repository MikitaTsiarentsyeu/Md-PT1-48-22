class Cart:
    def __init__(self):
        self.products = {}

    def add(self, product_id, amount):
        current = self.products.get(product_id, 0)
        self.products[product_id] = current + amount if current + amount >= 0 else 0
        if current + amount <=0:
            del self.products[product_id]
