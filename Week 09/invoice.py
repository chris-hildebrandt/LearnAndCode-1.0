# invoice.py responsible for creating the invoice
class InvoiceGenerator:
    @staticmethod
    def generate(order: Order) -> str:
        invoice = f"Invoice for Order #{order.order_id}\n"
        invoice += f"Customer: {order.customer_name}\nItems:\n"
        for item in order.items:
            item_total = item["price"] * item["quantity"]
            invoice += f"{item['name']} - {item['quantity']} x ${item['price']:.2f} = ${item_total:.2f}\n"
        invoice += f"Discount: ${order.discount:.2f}\n"
        invoice += f"Total: ${order.calculate_total():.2f}\n"
        return invoice
