# creare instanta, produse albitrare, afisare produse si valoare totala

from product import Product
from product_manager import ProductManager
from cart import Cart
import random


pm = ProductManager()
pm.add_product(Product("Mere", 1356, 5))
pm.add_product(Product("Iepuri", 194, 10))
pm.add_product(Product("Sarmale", 231, 7))
pm.add_product(Product("Cizme", 3123, 41))

pm.display_products()
pm.total_inventory_value()

pm.remove_product("Iepuri")
pm.display_products()

cart = Cart()

selected_products = random.sample(pm.products, 3)
for p in selected_products:
    cart.add_to_cart(p)


cart.display_cart()
cart.total_cart_value()
