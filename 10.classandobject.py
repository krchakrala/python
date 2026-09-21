
#House1 blueprint
#from pyclbr import Class


print("\n House1 blueprint: \n")
class House1:
    def open_door(self):
        print("Door is opened")

    def close_door(self):
        print("Door is closed")

house1 = House1()
house1.open_door()
house1.close_door()

house2 = House1()
house2.open_door()
house2.close_door()

#House2 blueprint
print("\n House2 blueprint: \n")

class House2:

    def __init__(self, color, rooms):
        self.color = color
        self.rooms = rooms

    def open_door(self):
        print("Door is opened")

    def show_details(self):
        print("Color: ", self.color)
        print("Rooms: ", self.rooms)
        print("\n")

house3 = House2("Blue", 3)
house3.open_door()
house3.show_details()

house4 = House2("Green", 2)
house4.open_door()
house4.show_details()

class Mobile:

    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def call(self):
        print("Calling...")

    def take_photo(self):
        print("Taking photo...")

phone1 = Mobile("Samsung", "Black")
phone2 = Mobile("Apple", "White")

phone1.call()
phone1.take_photo()

phone2.call()
phone2.take_photo()


#Inheritance Buildding Upon Existing Classes
class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

class Cat(Animal):
    def speak(self):
        print("Cat meows")

class Bird(Animal):
    def __init__(self, name,wingspan):
        super().__init__(name)
        self.wingspan = wingspan

my_dog = Dog("Buddy")
my_cat = Cat("Whiskers")
my_bird = Bird("Tweety",10)

print(my_dog.name)
print(my_cat.name)
print(my_bird.name)
print(my_bird.wingspan)

my_dog.speak()
my_cat.speak()





