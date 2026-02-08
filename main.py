# creare instanta, produse albitrare, afisare produse si valoare totala

from product import Product
from product_manager import ProductManager

pm = ProductManager()
pm.add_product(Product("Mere", 1356, 5))
pm.add_product(Product("Iepuri", 194, 10))
pm.add_product(Product("Sarmale", 231, 7))

pm.display_products()
pm.total_inventory_value()

pm.remove_product("Iepuri")
pm.display_products()