#string representation of an object
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} - {self.age}"

student1 = Student("Alice", 20)
print(str(student1))  # Output: Alice - 20

student2 = Student("Bob", 30)
student2.__init__("Bob", 25)
print(str(student2))    # Output: Bob - 25

print(student1.__str__())  # Output: Bob - 25


class Student_New:
    def __new__(cls, name, age):
        instance = super().__new__(cls)
        instance.name = name
        instance.age = age
        return instance
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

student3 = Student_New("Charlie", 22)
print(student3.name)  # Output: Charlie
print(student3.age)   # Output: 22

class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Employee(name={self.name}, age={self.age})"

employee1 = Employee("David", 28)
print(repr(employee1))  # Output: Employee(name=David, age=28)

#__str__ and __repr__ methods are used to provide string representations of objects. The __str__ method is used for creating a user-friendly string representation, while the __repr__ method is used for creating an unambiguous string representation that can be used for debugging and development purposes.
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - ${self.price}"

    def __repr__(self):
        return f"Product(name={self.name}, price={self.price})"

product1 = Product("Laptop", 1000)
print(product1)  # Output: Laptop - $1000
print(repr(product1))  # Output: Product(name=Laptop, price=1000)

#__len__ method is used to define the behavior of the built-in len() function for an object. It allows you to specify how the length of an object should be calculated.
class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def __len__(self):
        return len(self.items)

cart = ShoppingCart()
cart.add_item("Laptop")
cart.add_item("Mouse")
print(len(cart))  # Output: 2   

#arithmetic operations can be overloaded using magic methods like __add__, __sub__, __mul__, etc. This allows you to define custom behavior for arithmetic operations on objects of a class.
class Number:

    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Number(self.value + other.value)

    def __sub__(self, other):
        return Number(self.value - other.value)

    def __mul__(self, other):
        return Number(self.value * other.value)

    def __str__(self):
        return str(self.value)

num1 = Number(10)
num2 = Number(5)

result_add = num1 + num2
print(result_add)  # Output: 15 

result_sub = num1 - num2
print(result_sub)  # Output: 5

result_mul = num1 * num2
print(result_mul)  # Output: 50

##comparison operations can be overloaded using magic methods like __eq__, __ne__, __lt__, __gt__, etc. This allows you to define custom behavior for comparison operations on objects of a class.
class Employee:

    def __init__(self, salary):
        self.salary = salary

    def __eq__(self, other):
        return self.salary == other.salary

    def __lt__(self, other):
        return self.salary < other.salary

e1 = Employee(50000)
e2 = Employee(50000)

print(e1 == e2)

print(e1 < e2)
print(e1.__lt__(e2))  # Output: False

##In summary, magic methods in Python allow you to define custom behavior for built-in operations and functions. They provide a way to customize the behavior of objects and make them behave like built-in types. By implementing magic methods, you can create classes that are more intuitive and easier to use.
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"Employee(name={self.name}, salary={self.salary})"

    def __repr__(self):
        return f"Employee(name={self.name}, salary={self.salary})"

    def __len__(self):
        return len(self.name)

    def __add__(self, other):
        return Employee(self.name + " & " + other.name, self.salary + other.salary)

    def __eq__(self, other):
        return self.salary == other.salary

e1 = Employee("Alice", 50000)
e2 = Employee("Bob", 60000)
e3 = Employee("Charlie", 50000)
e4 = Employee("David", 70000)
result_add = e1 + e2
print(result_add)  # Output: Employee(name=Alice & Bob, salary=110000)
result_eq = e1 == e3
print(result_eq)  # Output: True
result_len = len(e1)
print(result_len)  # Output: 5
result_repr = repr(e1)
print(result_repr)  # Output: Employee(name=Alice, salary=50000)
result_str = str(e1)
print(result_str)  # Output: Employee(name=Alice, salary=50000)


#__()iter() and __next__() methods are used to define the behavior of an object when it is used in an iteration context, such as in a for loop. The __iter__() method returns an iterator object, and the __next__() method returns the next value from the iterator.
class MyIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.data):
            value = self.data[self.index]
            self.index += 1
            return value
        else:
            raise StopIteration

my_iter = MyIterator([1, 2, 3, 4, 5])
for item in my_iter:
    print(item)  # Output: 1 2 3 4 5    

