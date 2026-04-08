# Task 7: Mini Project - Simple Inventory System 

# Product Class
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - {self.price}"

    # __add__ method
    def __add__(self, other):
        return self.price + other.price


# Inventory Class
class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        print(f"Product added: {product}")

    def show_summary(self):
        print("\nProduct List:")
        for p in self.products:
            print(p)


# Store Class
class Store:
    def __init__(self):
        self.inventory = Inventory()
        print("Store object created")


# ----------- Testing the System -----------

# 1. Creating a Store Object
store = Store()

# 2. Adding 3 Products
p1 = Product("Laptop", 50000)
p2 = Product("Phone", 20000)
p3 = Product("Shoes", 3000)

store.inventory.add_product(p1)
store.inventory.add_product(p2)
store.inventory.add_product(p3)

# 3. Showing Summary
store.inventory.show_summary()

# 4. Using __add__ to combine prices
print("\nCombining prices of Laptop and Phone")
total = p1 + p2
print("Combined Price:", total)



