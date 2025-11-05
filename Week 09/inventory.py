# inventory.py manages item availability and updates
class Inventory:
    def __init__(self):
        self.stock = {"apple": 100, "banana": 50}

    def is_available(self, item: str, quantity: int) -> bool:
        return self.stock.get(item, 0) >= quantity

    def reduce_stock(self, item: str, quantity: int):
        if self.is_available(item, quantity):
            self.stock[item] -= quantity

    def get_status(self) -> str:
        return "\n".join(f"{item}: {qty} remaining" for item, qty in self.stock.items())
