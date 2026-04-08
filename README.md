# GenAI-Assignment7-OOps Concepts 
## Overview ##
This repository contains 7 Python tasks demonstrating Object-Oriented Programming (OOP) concepts including abstraction, inheritance, operator overloading, encapsulation, and a mini project implementation.
Each task is implemented with classes, methods, and testing examples. Suitable for learning, practice, and exam preparation.

✅ Task Summary

🔹Task 1: Basic Class & Object Creation
Created a Product class with attributes:
name
price
category
Implemented method:
get_info() → Displays product details
Created two product objects and displayed their information
Added optional method:
apply_discount(percent) → Returns discounted price

🔹 Task 2: Constructor & Encapsulation
Modified Product class:
Made price a private attribute (__price)
Implemented:
get_price() → Getter method
set_price(new_price) → Setter with validation (new_price > 0)
Demonstrated updating price using setter

🔹 Task 3: Inheritance
Created subclass ElectronicProduct inheriting from Product
Added new attribute:
warranty_years
Overrode:
get_info() method to include warranty details
Demonstrated inheritance and method overriding

🔹 Task 4: Polymorphism
Created two subclasses:
Laptop
Mobile
Both override:
get_info() method with different output styles
Used a loop to call get_info() on different objects
Demonstrated polymorphism (same method, different behavior)

🔹Task 5: Abstraction
Learn abstract classes using abc module.
Key concepts: Abstract Base Class (ABC), @abstractmethod
Example: Payment abstract class with subclasses CreditCardPayment and UPIPayment.

🔹Task 6: Operator Overloading
Learn magic methods and how to overload operators.
Key concepts: __str__, __add__
Example: Product class with __add__ to combine prices.

🔹Task 7: Mini Project – Simple Inventory System
Build a small inventory system using OOP concepts.
Classes:
Product → stores name, price, supports __add__
Inventory → add, remove, show products
Store → contains Inventory, main interface
Testing Points:
Create store object
Add 3 products
Show product summary
Use __add__ to combine prices


💡 Key Takeaways
Learned core OOP concepts: Encapsulation, Abstraction, Inheritance, Polymorphism
Learned operator overloading for objects
Built a mini inventory system combining all learned concepts

🛠 How to Run Python Files
1. Running .py files in VS Code
Open VS Code and install Python extension.
Open the folder containing the .py file.
Open the file, then click Run (▶️) in the top right or press F5.
Output will appear in the terminal.
2. Running .ipynb files in VS Code
Open VS Code and install Python & Jupyter extensions.
Open the .ipynb file.
Click Run Cell (▶️) for each cell.
Output appears below each cell.
3. Running Jupyter Notebook
Install Jupyter Notebook:
Bash
pip install notebook
Open terminal and run:
Bash
jupyter notebook
Your browser opens. Navigate to the .ipynb file and run cells.
