# main.py coordinates the other classes
from inventory import Inventory
from order import Order
from invoice import InvoiceGenerator

if __name__ == "__main__":
    inventory = Inventory()
    order = Order(1, "John Doe")

    for name, price, qty in [("apple", 1.0, 5), ("banana", 0.5, 3)]:
        if inventory.is_available(name, qty):
            order.add_item(name, price, qty)
            inventory.reduce_stock(name, qty)
        else:
            print(f"Not enough {name} in stock")

    order.set_discount(2.0)
    print(InvoiceGenerator.generate(order))
    print("Inventory Status:")
    print(inventory.get_status())
