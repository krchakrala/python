# Program to division of two integer values
#Example of try block with multiple exception types with except block
try:
    n1=int(input("Enter first integer "))
    n2=int(input("Enter second integer "))
    n3=n1/n2
    print(f'division of {n1}/{n2}={n3:.2f}')
except (ValueError,TypeError):
    print("input value must be integer")
except ZeroDivisionError:
    print("cannot divide number with zero")

#Example of username and password error handling
users={'naresh':'nit123',
       'suresh':'s321',
       'ramesh':'r678'}

uname=input("UserName :")  
password=input("Password :")
try:
    if users[uname]==password:
        print(f'{uname} welcome')
    else:
        print("invalid password")
except KeyError:
    print("invalid user name ")
finally:
    print("Hello I am Finally block")

#Print statement execute in all blocks
print("inside program")
try:
    print("inside try block")
    a=int(input("enter first number "))
    b=int(input("enter second number "))
    c=a/b
    print(c)
except ValueError:
    print("inside except block of ValueError")
finally:
    print("inside finally block")
print("continue....")

#Excetption handling by using function example
def div(n1,n2):
    try:
        return n1/n2
    except ZeroDivisionError:
        print("inside except block")
    finally:
        print("inside finally block")

res1=div(4,2)
print(res1)
#res2=div("abc",2)
#print(res2)

#Example for raise a exception with "raise" Keyword
def multiply(a,b):
    if a==0 or b==0:
        raise ValueError()
    else:
        return a*b
try:
    num1=int(input("Enter first integer "))
    num2=int(input("Enter second integer "))
    num3=multiply(num1,num2)
    print(f'product of {num1}*{num2}={num3}')
except ValueError:
    print("cannot multiply number with zero")
