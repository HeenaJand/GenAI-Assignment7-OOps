# Task 4: Polymorphism 

class Product:

    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def get_info(self):
        print("Product:", self.name)


class Laptop(Product):
    def get_info(self):
        print("Laptop Name:", self.name)
        print("Price:", self.price)
        print("Category:", self.category)


class Mobile(Product):
    def get_info(self):
        print("Mobile Name:", self.name)
        print("Price:", self.price)
        print("Category:", self.category)


# Creating objects
l1 = Laptop("Dell XPS", 90000, "Electronics")
m1 = Mobile("iPhone", 80000, "Electronics")

# Polymorphism using loop
products = [l1, m1]

for item in products:
    item.get_info()
    print()



