# lista produce, adaugare si afisare produce, afisare valoare totala produse

from product import Product

class ProductManager:
   def __init__(self):
        self.products = []

   def add_product(self, product):
        self.products.append(product)

   def display_products(self):
        for product in self.products:
            product.display_info()

   def total_inventory_value(self):
        total = sum(product.price * product.quantity for product in self.products)
        print(f"Valoarea totală a inventarului: {total}")



   def remove_product(self, product_name):
       for product in self.products:
           if product.name == product_name:
               self.products.remove(product)
               print(f"Removed product: {product_name}")
               return
       print(f"Product {product_name} not found.")