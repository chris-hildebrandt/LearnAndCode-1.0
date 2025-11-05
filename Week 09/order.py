# order.py handles order items and discounts
class Order:
    def __init__(self, order_id: int, customer_name: str):
        self.order_id = order_id
        self.customer_name = customer_name
        self.items = []
        self.discount = 0.0

    def add_item(self, name: str, price: float, quantity: int):
        self.items.append({"name": name, "price": price, "quantity": quantity})

    def set_discount(self, discount: float):
        self.discount = discount

    def calculate_total(self) -> float:
        total = sum(item["price"] * item["quantity"] for item in self.items)
        return total - self.discount
