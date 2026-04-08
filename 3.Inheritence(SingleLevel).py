# Task 3: Inheritance ( Single Level)

class Product:
    def __init__(self, name, price, category):
        self.name= name
        self.price= price
        self.category= category 

    def get_info(self):
        print(f"Product Name:{self.name}")
        print(f"Price of the product: {self.price}")
        print(f"Category of the product:{self.category}")

# Subclass inherit Base Class
class ElectronicProduct(Product):
    def __init__(self,name,price, category, warranty_years):
        super().__init__(name,price, category)
        self.warranty_years= warranty_years

    # Overriding Method

    def get_info(self):
        print(f" Product Name: {self.name}")
        print(f" Price of the product: {self.price}")
        print(f" Category of the product:{self.category}")
        print(f" Warranty years of the product: {self.warranty_years}")

# Creating Objects

ep = ElectronicProduct("Laptop" , 48000, "Electronics", 2)

# Calling Method 
ep.get_info()
        



