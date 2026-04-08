#Task 1: Basic Class and Object Creation 

class Products:
    def __init__(self,name, price, category,):
        self.name = name
        self.price= price
        self.category= category 
        
    ## method creation 
    def get_info(self):
        print(f" Product Name: {self.name}")
        print(f" Price of the product: {self.price}")
        print(f" Category of the product:{self.category}")
        
    def apply_discount(self,percent):
        discount_price = self.price - (self.price * percent/100)
        return discount_price

        
## Creating Objects of the class
product1 = Products("ToyCar", 4500, "Toys")
product2 = Products("Charger", 2500, "Electronics")

## Calling Methods
product1.get_info()
print()

product2.get_info()
print()

## Optional Part: Applying Discount 
discounted_price = product1.apply_discount(10)
print("\n Discounted Price of ToyCar :", discounted_price)



