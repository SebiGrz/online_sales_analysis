from product import Product

class Cart:
    def __init__(self):
        self.cart_items = []

    def add_to_cart(self, product):
        self.cart_items.append(product)
        print(f"Added {product.name} to cart.")

    def total_cart_value(self):
        total = sum(p.price * p.quantity for p in self.cart_items)
        print(f"Total cart value: {total}")
        return total

    def display_cart(self):
        if not self.cart_items:
            print("Cart is empty.")
        for product in self.cart_items:
            print(f"{product.name} - Price: {product.price}, Quantity: {product.quantity}")