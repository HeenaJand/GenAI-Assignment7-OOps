#Task 5: Abstraction Using Abstract Base Class

from abc import ABC, abstractmethod

#Abstract Class 
class Payment(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

#Subclass 1

class CreditCardPayment(Payment):

    def process_payment(self, amount):
        print(f"Processing credit card payment of {amount}")

#Subclass 2

class UPIPayment(Payment):

    def process_payment(self, amount):
        print(f"Processing UPI payment of {amount}")

# Object creation 
p1= CreditCardPayment()
p2= UPIPayment()

p1.process_payment(3550)
p2.process_payment(23000)



