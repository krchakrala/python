#Polymorphism - "One thing, many forms."
#The same method/operator can behave differently depending on the object or data being used.
#Polymorphism - 1).Method Overriding 2).Operator Overloading

class Animal:   #parent class
    def make_sound(self):
        print("Animal makes a sound")

class Dog(Animal): #Child class
    def make_sound(self):
        print("Dog says: Woof")

class Cat(Animal): #Child class
    def make_sound(self):
        print("Cat says: Meow")

my_dog = Dog()
my_cat = Cat()
my_dog.make_sound()  # Output: Dog says: Woof
my_cat.make_sound()  # Output: Cat says: Meow

animals=[Dog(), Cat()]
for animal in animals:
    animal.make_sound() # Output: Dog says: Woof
                         #         Cat says: Meow

#Payment processing example
class Payment:
    def pay(self):
        print("Making payment")

class CreditCard(Payment):
    def pay(self):
        print("Payment using Credit Card")

class UPI(Payment):
    def pay(self):
        print("Payment using UPI")

class PayPal(Payment):
    def pay(self):
        print("Payment using PayPal")

payments = [CreditCard(), UPI(), PayPal()]
for payment in payments:
    payment.pay() # Output: Payment using Credit Card
                  #         Payment using UPI
                  #         Payment using PayPal

#Method Overriding
class Parent:
    def show(self):
        print("Parent")

class Child1(Parent):
    def show(self):
        print("Child1")

class Child2(Parent):
    def show(self):
        super().show()  # Call the parent class method
        print("Child2")

parent=Parent()
parent.show() # Output: Parent

obj1 = Child1()
obj1.show() # Output: Child1    

obj2 = Child2()
obj2.show() # Output: Parent
            #         Child2

#Operator Overloading
class Employee:
    def __init__(self, salary):
        self.salary = salary
    def __add__(self, other):
        return self.salary + other.salary
    def __sub__(self, other):
        return self.salary - other.salary
    def __mul__(self, other):
        return self.salary * other.salary
    def __truediv__(self, other):
        return self.salary / other.salary
    def __ne__(self, other):
        return self.salary != other.salary
    def __eq__(self, other):
        return self.salary == other.salary
    

emp1 = Employee(15000)
emp2 = Employee(6000)
total_salary = emp1 + emp2  # Calls the __add__ method
print(total_salary)  # Output: 21000

total_salary = emp1 - emp2  # Calls the __sub__ method
print(total_salary)  # Output: 9000

total_salary = emp1 * emp2  # Calls the __mul__ method
print(total_salary)  # Output: 90000000

total_salary = emp1 / emp2  # Calls the __truediv__ method
print(total_salary)  # Output: 2.5

total_salary = emp1 != emp2  # Calls the __ne__ method
print(total_salary)  # Output: True

total_salary = emp1 == emp2  # Calls the __eq__ method
print(total_salary)  # Output: False