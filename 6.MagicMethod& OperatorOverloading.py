# Task 6: Magic Method and Operator Overloading 

class Product:
    
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    # __str__ method
    def __str__(self):
        return f"Product({self.name}, {self.price}, {self.category})"

    # Operator Overloading (+)
    def __add__(self, other):
        return self.price + other.price

# Creating objects
product1 = Product("Laptop", 50000, "Electronics")
product2 = Product("Phone", 20000, "Electronics")

# Testing __str__
print(product1)
print(product2)

# Testing +
total = product1 + product2
print("Total Price:", total)



