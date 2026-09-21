#static method example
class Employee:
     
   @staticmethod
   def company_policy():        
        print("Company policy: All employees must adhere to the code of conduct.")

Employee.company_policy()  # Output: Company policy: All employees must adhere to the code of conduct.

#Employee class with static method to check if an employee is eligible for promotion based on years of experience
class Employee:
    @staticmethod
    def is_valid_age(age):
        if age >= 18:
            return True
        else:
            return False

print(Employee.is_valid_age(20))  # Output: True
print(Employee.is_valid_age(17))  # Output: False

#staticmethods are used when we want to define a method that doesn't depend on the instance of the class. They can be called directly on the class without creating an instance.
class Bank:
    @staticmethod
    def calculate_interest(principal, rate, time):
        interest = (principal * rate * time) / 100
        return interest

interest=Bank.calculate_interest(1000, 5, 2)
print("Interest: ", interest)  # Output: Interest: 100.0

#@classmethod example
class Employee:
    company_name = "ABC Corp"

    @classmethod
    def get_company_name(cls):
        return cls.company_name

print(Employee.get_company_name())  # Output: ABC Corp

#classmethods are used when we want to define a method that operates on the class itself rather than on instances of the class. They can access and modify class-level attributes and can be called directly on the class without creating an instance.
#set and get class-level attributes using class methods
class Employee:
    company_name = "ABC Corp"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

    @classmethod
    def set_company_name(cls, name):
        cls.company_name = name

    @classmethod
    def get_company_name(cls):
        return cls.company_name

emp1 = Employee("Alice", 30)
emp1.display_info()  # Output: Name: Alice, Age: 30
print(Employee.get_company_name())  # Output: ABC Corp
Employee.set_company_name("XYZ Inc")
print(Employee.get_company_name())  # Output: XYZ Inc

emp2 = Employee("Bob", 25)
emp2.display_info()  # Output: Name: Bob, Age: 25
print(Employee.get_company_name())  # Output: XYZ Inc

#@staticmethod and @classmethod can be used together in a class to provide both instance-level and class-level functionality. Here's an example:
class Employee:
    company_name = "ABC Corp"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

    @staticmethod
    def is_valid_age(age):
        if age >= 18:
            return True
        else:
            return False

    @classmethod
    def get_company_name(cls):
        return cls.company_name

emp1 = Employee("Alice", 30)
emp1.display_info()  # Output: Name: Alice, Age: 30
print(Employee.is_valid_age(20))  # Output: True
print(Employee.get_company_name())  # Output: ABC Corp

emp2 = Employee("Bob", 25)
emp2.display_info()  # Output: Name: Bob, Age: 25   
print(Employee.is_valid_age(17))  # Output: False
print(Employee.get_company_name())  # Output: ABC Corp