z = 3
# Lambda Functions
square = lambda x: x * x
print(square(4)) # Output: 16

add = lambda x, y: x + y
print(add(5, 3)) # Output: 8

def multiply(x, y):              #Functions can also be defined using the def keyword.
    return x * y
print(multiply(5, 3)) # Output: 15

multiply = lambda x, y: x * y    # Lambda functions are anonymous, inline functions.
print(multiply(5, 3)) # Output: 15

numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x * x, numbers))
print(squared_numbers) # Output: [1, 4, 9, 16, 25]  

#Lambda functions with multi comments
square = lambda x: x*x 
'''
As good as writing
def square(x):
    return x*x
'''
sum = lambda x, y: x+y
'''
As good as writing
def sum(x, y):
    return x + y
'''
print(square(3))
print(sum(3, 62))

#Global and Local Variables
def sum(a, b):
    print("Hey I am summing ")
    c = a + b  # c is a local variable
    global z # Please modify global z
    z = 0 # This will refer to global z and not create a local variable
    return c 

print(sum(3, 12))
print("Z global value",z)

#Function scope and lifetime of variables
def sum(a, b):
    # a and b are local variables
    c = a + b 
    z = 1 # It creates a local variable called z which is destroyed after this function returns
    return c

def greet():
    z = 32 # Local variable
    print("Hello")
    
z = 8 # z is a global variable
print(z)
print(sum(4, 6)) 
print(z)

#Function parameters and defatult parameters
def add(a, b, plus=0):
    x = a + b + plus
    return x

c = add(3, 5, 2)
print("C value ",c)
c1 = add(b=5, a=3)
print("C1 value ",c1)

#docstring is printing the documentation of the function
def sum(a, b): 
    '''This will sum two numbers'''
    c = a + b  
    return c

print(sum.__doc__) #syntax of printing docstring of a function is function_name.__doc__

