def greet():
    print("Hello, World!")

greet() # Output: Hello, World!

def greet_with_return():
    return "Hello, Python!"

print(greet_with_return()) # Output: Hello, Python!

def greet_with_name(name):
    return f"Hello, {name}!"

print(greet_with_name("Koteswar")) # Output: Hello, Koteswar!

def greet_with_name(name):
    print(f"Hello, {name}!")

greet_with_name("Koteswar") # Output: Hello, Koteswar!

def greet_with_age(age):
    print(f"Hello, you are {age} years old!")

greet_with_age(25) # Output: Hello, you are 25 years old!
greet_with_age(45) # Output: Hello, you are 45 years old!
greet_with_age(85) # Output: Hello, you are 85 years old!

def greet_with_name_and_age(name, age):
    print(f"Hello, {name}! You are {age} years old.")   

greet_with_name_and_age("Koteswar", 26) # Output: Hello, Koteswar! You are 26 years old.

def greet_with_name_and_age(name, age):
    return f"Hello, {name}! You are {age} years old."   

print(greet_with_name_and_age("Koteswar", 27)) # Output: Hello, Koteswar! You are 27 years old.

def greet_with_name_and_age(name, age):
    return f"Hello, {name}! You are {age} years old."  

name_age = greet_with_name_and_age("Koteswar", 28)
print(name_age) # Output: Hello, Koteswar! You are 28 years old.

def greet_with_name_and_age(age):
    return age

age_value1 = greet_with_name_and_age(29)
print(type(age_value1))
print(age_value1) # Output: 29

age_value2 = str(greet_with_name_and_age(29))
print(type(age_value2))
print(age_value2) # Output: 29

def student(name, age):
  print(f"Name: {name}, Age: {age}")

student(age=20, name="Bob") #named arguments

student("Koteswar", 20) 