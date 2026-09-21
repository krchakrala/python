# Program to division of two integer values
#Example of try block with one except block

n1=int(input("enter first integer value "))
n2=int(input("enter second integer value "))
try:
    n3=n1/n2
    print(f'division of {n1}/{n2}={n3}')
except ZeroDivisionError:
    print("cannot divide number with zero, try again...")
    
print("continue...")


# Program to division of two integer values
#Example of try block with multiple except blocks
try:
    n1=int(input("enter first integer value "))
    n2=int(input("enter second integer value "))
    n3=n1/n2
    print(f'division of {n1}/{n2}={n3}')
except ZeroDivisionError:
    print("cannot divide number with zero, try again...")
except ValueError:
    print("input only integer values...")
    
print("continue...")

# Program to division of two integer values
#Example of holding error objet by except block.
try:
    n1=int(input("enter first integer value "))
    n2=int(input("enter second integer value "))
    n3=n1/n2
    print(f'division of {n1}/{n2}={n3}')
except ZeroDivisionError as z:
    print("cannot divide number with zero, try again...")
    print(z)
except ValueError as a:
    print("input only integer values...")
    print(a)
    print(type(a))
    print(repr(a))

print("continue...")


# Program to division of two integer values
#Example handling multiple errors using one except block (except block without type)
import sys
try:
    n1=int(input("enter first integer value "))
    n2=int(input("enter second integer value "))
    n3=n1/n2
    print(f'division of {n1}/{n2}={n3}')
except:
    t=sys.exc_info()
    print(t[0])
    if isinstance(t[1],ZeroDivisionError):
        print("cannot divide number with zero")
    elif isinstance(t[1],ValueError):
        print("input value must be integer")


# Program to division of two integer values
#Example of except block with base type, which is able to handle any subtype error
import sys
try:
    n1=int(input("enter first integer value "))
    n2=int(input("enter second integer value "))
    n3=n1/n2
    print(f'division of {n1}/{n2}={n3}')
    
except Exception:
    t=sys.exc_info()
    print(t[0],t[1])
    if isinstance(t[1],ZeroDivisionError):
        print("cannot divide number with zero")
    elif isinstance(t[1],ValueError):
        print("input value must be integer")




