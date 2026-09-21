def my_decorator(func):
    def wrapper():
        print("Before the function is called.")
        func()
        print("After the function is called.")
    return wrapper


def say_hello():
    print("Hello!") 

say_hello = my_decorator(say_hello)
say_hello()  # Output: Before the function is called. Hello! After the function is called.

@my_decorator
def say_hello1():
    print("Hello! say_hello1") 

say_hello1()  # Output: Before the function is called.
              #         Hello! say_hello1
                 #         After the function is called.



def my_authorization_required(func):
    def authorization_check():
        print("Authorization check is performed before calling the function.")
        func()
    return authorization_check

@my_authorization_required
def inbox_action():
    print("Hello! I am inbox_action") 

@my_authorization_required
def sent_action():
    print("Hello! I am sent_action") 

@my_authorization_required
def draft_action():
    print("Hello! I am draft_action") 

inbox_action()  # Output: Authorization check is performed before calling the function.
                #         Hello! I am inbox_action

sent_action()  # Output: Authorization check is performed before calling the function.
               #         Hello! I am sent_action

draft_action()  # Output: Authorization check is performed before calling the function.
                #         Hello! I am draft_action

#Decorators with arguments
def my_decorator_with_params(func):
    def wrapper(name):
        print("Before the function is called.")
        func(name)
        print("After the function is called.")
    return wrapper   

@my_decorator_with_params
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")

# Decorators with arbitrary arguments
def my_decorator_with_arbitrary_args(func):
    def wrapper(*args, **kwargs):
        print("Before the function is called.")
        func(*args, **kwargs)
        print("After the function is called.")
    return wrapper

@my_decorator_with_arbitrary_args
def add_numbers(a, b):
    print(f"The sum of {a} and {b} is {a + b}")

add_numbers(5, 10)


#Decorator with timer measurement
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("Execution time:", end - start)
        return result
    return wrapper

@timer
def calculate_sum(n):
    total = 0
    for i in range(n):
        total += i
    return total

result= calculate_sum(1000000)  # Output: Execution time: <time taken to execute the function>
print("Result:", result)  # Output: Result: 499999500000

#Decorators with validation amount
def validate_amount(func):
    def wrapper(amount):
        if amount < 0:
            raise ValueError("Amount cannot be negative.")
        return func(amount)
    return wrapper

@validate_amount
def process_payment(amount):
    print(f"Processing payment of ${amount}")

process_payment(100)  # Output: Processing payment of $100
process_payment(500)  # Output: Processing payment of $500
#process_payment(-50)  # Raises ValueError: Amount cannot be negative.
            
#Decorator with repeatition
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(10)
def say_hello_repeat():
    print("Hello!") 

say_hello_repeat()  # Output: Hello! Hello! Hello!

#Decorator with functiontools.wraps
import functools

def my_wrapped_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Before the function is called.")
        func(*args, **kwargs)
        print("After the function is called.")
    return wrapper  

@my_wrapped_decorator
def say_hello_wrapped():
    """This function says hello."""
    print("Hello!")

print(say_hello_wrapped.__name__)  # Output: say_hello_wrapped
print(say_hello_wrapped.__doc__)   # Output: This function says hello.

#Multiple decorators
def decorator1(func):
    def wrapper():
        print("Decorator 1 - Before")
        func()
        print("Decorator 1 - After")
    return wrapper

def decorator2(func):
    def wrapper():
        print("Decorator 2 - Before")
        func()
        print("Decorator 2 - After")
    return wrapper

@decorator1
@decorator2
def say_hello_multiple():
    print("Hello!")

say_hello_multiple()  # Output: Decorator 1 - Before
                      #         Decorator 2 - Before
                      #         Hello!
                      #         Decorator 2 - After
                      #         Decorator 1 - After

#Python's Built-in Decorators
class Employee:

    company="ABC Corp"

    @staticmethod
    def company_policy():
        print("All employees must adhere to the company's code of conduct.")
    @classmethod
    def company_info(cls):
        print(f"Company Name: {cls.company}")

Employee.company_policy()  # Output: All employees must adhere to the company's code of conduct.
Employee.company_info()   # Output: Company Name: ABC Corp
