#Basic function without args and kwargs
def add(a, b):
    return a + b

print("Result of addition: ", add(10, 20))

#function with args
def add(*args):
    total = 0
    for value in args:
        total += value

    return total

print(add(10, 20))
print(add(10, 20, 30))
print(add(10, 20, 30, 40))

#Function with employee name and skills using args
def employee_skills(name,email, *skills):
    print("Employee:", name)
    print("Email:", email)

    for skill in skills:
        print("Skill:", skill)

employee_skills(
    "Koteswar",
    "koteswar@example.com",
    "C#",
    ".NET",
    "Azure",
    "Python"
)

#Function with kwargs
def employee(**kwargs):
    print(kwargs)

employee(
    name="Koteswar",
    experience=9,
    technology=".NET",
    location="Hyderabad"
)

#Function with employee name and experience using kwargs
def employee(**kwargs):
    print("Name:", kwargs["name"])
    print("Experience:", kwargs["experience"])

employee(name="Koteswar", experience=9)

#Function with employee name,experience and technology using kwargs
def employee(**kwargs):

    for key, value in kwargs.items():
        print(key, ":", value)

employee(
    name="Koteswar",
    experience=9,
    technology=".NET"
)

#Function with arguments and keyword arguments
def demo(*args, **kwargs):
    print("args:", args)
    print("kwargs:", kwargs)

demo(
    10,
    20,
    30,
    name="Koteswar",
    city="Hyderabad"
)

#function with all types of arguments
def example(a, b, *args, **kwargs):

    print("a =", a)
    print("b =", b)
    print("args =", args)
    print("kwargs =", kwargs)

example(
    10,
    20,
    30,
    40,
    50,
    name="Ravi",
    city="Hyderabad"
)