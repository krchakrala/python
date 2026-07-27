# In Python, variables are used to store data that can be used and manipulated throughout a program. A variable is created the moment you assign a value to it using the assignment operator (=).

age = 34 # integer
name = "Koteswar" # string
cgpa = 4.55 # float

# Rule of defining a variable in Python  
# Variable names must start with a letter (a-z, A-Z) or an underscore (_).
# They can contain letters, numbers, and underscores.
# Variable names are case-sensitive (age and Age are different).
# Avoid using Python keywords (e.g., if, for, while) as variable names.

# 34age = 4 # Invalid because variable cannot start with a number
age = 32 # Valid because variable can start with a number 
# a$$ge = 45 # Invlaid because variables cannot contain special characters other than _
__age = 34
__nice_45 = 34
a_b_c_7 = "Sam"

# Python supports several built-in data types:
#     Integers (int): Whole numbers (e.g., 10, -5).
#     Floats (float): Decimal numbers (e.g., 3.14, -0.001).
#     Strings (str): Text data enclosed in quotes (e.g., "Hello", 'Python').
#     Booleans (bool): Represents True or False.
#     Lists: Ordered, mutable collections (e.g., [1, 2, 3]).
#     Tuples: Ordered, immutable collections (e.g., (1, 2, 3)).
#     Sets: Unordered collections of unique elements (e.g., {1, 2, 3}).
#     Dictionaries: Key-value pairs (e.g., {"name": "Alice", "age": 25}).

age = 3 
print(age)
print(type(age))

cgpa = 8.2
print(cgpa)
print(type(cgpa))

name = "Harry"
print(name)
print(type(name))

is_completed = True # can also be False
print(is_completed)
print(type(is_completed))


name="koteswar"
print("Hello ",name)

_num12=24
print("My age is ",  _num12)

name= input("Enter your name: ")
print("Hello ", name)

age= input("Enter your age: ")
print("You are ", age, " years old.")

name = input("Please enter your name: ")
city = input("Please enter your city: ")
age = input("Please enter your age: ")
print(f"{name} is from {city} and aged {int(age) + 10}")

print("type casting is used to convert one data type to another. For example, you can convert a string to an integer or a float to a string.")
a = 34 
b = "34"
d = 223


print("a value is: ", a)
print(type(a))

print("b value is: ", b)
print(type(b))

# Convert b to an integer
c = int(b)
print("c value is: ", c)
print(type(c))

e = str(d)
print("e value is: ", e)
print(type(e))

# a = input("Enter first number") 
# a = int(a) # convert a to int version of a
# print(a + 3)

a = int(input("Enter first number: "))
# a = int(a)
b = int(input("Enter second number: "))
# b = int(b)

print("a and b value is: ", a + b)

