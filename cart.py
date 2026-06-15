class ShoppingCart:
    def __init__(self, user_id):
        self.user_id = user_id
        self.items = {}
        self.discount_code = None

    def add_item(self, product_id, name, price, quantity=1):
        if product_id in self.items:
            self.items[product_id]["quantity"] += quantity
        else:
            self.items[product_id] = {"name": name, "price": price, "quantity": quantity}

    def get_total(self):
        return sum(i["price"] * i["quantity"] for i in self.items.values())

    def clear(self):
        self.items = {}
