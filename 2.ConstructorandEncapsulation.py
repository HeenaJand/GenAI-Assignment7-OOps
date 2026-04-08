# Task 2: Constructor & Encapsulation 

class Product:
    def __init__(self, name, price, category):
        self.name= name
        self.__price= price  # PRIVATE ATTRIBUTE 
        self.category= category

    def get_info(self):
        print(f" Product Name: {self.name}")
        print(f" Price of the product: {self.__price}")
        print(f" Category of the product:{self.category}")
    
     # Getter
    def get_price(self):
        return self.__price

    # Setter
    def set_price(self, new_price):
        if new_price>0:
            self.__price = new_price
        else:
            print(" Invalid price! Price must be greater than zero.")

# Creating Objects

product= Product("Smartphone", 35000, " Electronics")

# Display Original Price
product.get_info()

#Modified price using setter
product.set_price(27000)

# Display updated price
print("\n After updating price:")
product.get_info()

# Display output for invalid price
product.set_price(-5000)

        


    



