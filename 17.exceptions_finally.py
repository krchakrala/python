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

#Custom Exception handling by using class
class ZeroMultiplyError(Exception):
    pass

def multiply(a,b):
    if a==0 or b==0:
        raise ZeroMultiplyError()
    else:
        return a*b

try:
    num1=int(input("Enter first integer "))
    num2=int(input("Enter second integer "))
    num3=multiply(num1,num2)
    print(f'product of {num1}*{num2}={num3}')
except ZeroMultiplyError:
    print("cannot multiply number with zero")
except ValueError:
    print("input value must be integer type ")
	
	
#Exception handling by using custom LoginError
users={'naresh':'n123',
       'kishore':'k321',
       'ramesh':'r567'}

class LoginError(Exception):
    def __init__(self,msg="invalid username or password"):
        self.__msg=msg
    def getMessage(self):
        return self.__msg

def login(user,pwd):
    if user in users and users[user]==pwd:
        print(f'{user} welcome')
    else:
        raise LoginError()


def main():
    try:
        uname=input("UserName :")
        password=input("Password :")
        login(uname,password)
    except LoginError as obj:
        print(obj.getMessage())

main()


#Exception handling with nested try except block
print("inside program")
try:
    print("inside outer try block try block")
    n1=int(input("Enter first number "))
    try:
        n2=int(input("Enter second number "))
        print("inside inner try block")
        n3=n1/n2
        print(f'division of {n1}/{n2} is {n3}')
    except ZeroDivisionError:
        print("inside inner except block")
        print("cannot divide number with zero")
    except ValueError:
        print("inside inner except block")
        print("Input values must be integer ")
except ValueError:
    print("inside outer except block")
    print("Input values must be integer ")
	
#Example of assert statement   
value=input("enter integer value ")
assert value.isdigit(),"not integer value" #AssertionError: not integer value
value=int(value)
print(value)



