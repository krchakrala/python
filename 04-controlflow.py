#syntax: if else condition
#if condition1:
# Code to execute if condition1 is True
#elif condition2:
# Code to execute if condition2 is True
#else:
# Code to execute if all conditions are False


from unittest import case


# age = int(input("Enter your age: "))
# if age <18:
#    print("You are a minor.")
#    print("You are an adult.")  
# elif age ==18:
#    print("You just became an adult!")
# else:
#    print("You are an adult.")

#syntax: match case condition
#match value:
#case pattern1:
# Code to execute if value matches pattern1
#case pattern2:
# Code to execute if value matches pattern2
#case_:
# Default case (if no patterns match)

status =int(input("Enter your Status: "))
match status:
  case 100:
    print("Success! 100")
  case 200:
      print("Success! 200")
  case 300:
      print("Success! 300")
  case 400:
    print("Not Found")
  case _:
    print("Unknown Status")

weekdays=input("Enter the weekdays: ")

match weekdays:
  case 'Monday':
    print("Monday!")
  case 'Tuesday':
      print("Tuesday!")
  case 'Wednesday':
      print("Wednesday!")
  case 'Thursday':
      print("Thursday!")
  case 'Friday':
      print("Friday!")
  case 'Saturday':
    print("Saturday!")
  case 'Sunday':
    print("Sunday!")
  case _:
    print("There is no such weekday!")