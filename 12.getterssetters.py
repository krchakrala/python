class Person:
    def __init__(self, name1, age1):
        self._name = name1
        self._age = age1

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string.")
        self._name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Age must be a non-negative integer.")
        self._age = value

person = Person("Alice", 30)
print(person.name)  # Output: Alice
print(person.age)  # Output: 30
person.age = 31
print(person.age)  # Output: 31
person.name = "Bob"
print(person.name)  # Output: Bob
