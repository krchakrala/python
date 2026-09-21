#Creating a list
# numbers=[1,2,3,4,5,6,7,8,9]
# print(numbers)

# mixed = [1, 2.5, "Hello", True, [1, 2, 3], (4, 5), {6, 7}, {"name": "Alice", "age": 25}]
# print(mixed)

# #Common List Operations
# my_list =[1,2,3]
# print("List of elements: ",my_list)
# my_list.append(4) # [1, 2, 3, 4]
# print("After appending 4: ",my_list)
# my_list.insert(5,9) # [1, 2, 3, 4, 9]
# print("After inserting 9 at index 5: ",my_list)
# my_list.remove(2) # [1, 3, 4, 9]
# print("After removing 2: ",my_list)
# my_list.pop() # Removes last element -> [1, 99, 3]
# print("After popping last element: ",my_list)
# my_list.reverse() # [3, 99, 1]
# print("After reversing: ",my_list)
# my_list.sort() # [1, 3, 99]
# print("After sorting: ",my_list)

# #List Comprehensions
# squared_numbers = [x**2 for x in numbers]
# print("Squared numbers: ", squared_numbers)


# # Tuples
# my_tuple = (1, 2, 3, 4, 5)
# print("Tuple: ", my_tuple)

# print("Tuple: ", my_tuple[3]) # Accessing elements in a tuple 4 POSITIONAL INDEXING

# single_element_tuple = (42,)   # Tuple with one element (comma required)
# print("Single element tuple: ", single_element_tuple)

# a,b,e,d,c = my_tuple           #unpacking a tuple into variables
# print("Unpacked values: ", a, b, c, d, e)

# #Count and Index in a tuple
# my_tuple = (1, 2, 3, 4, 5, 2, 3, 4, 5, 4, 4, 1, 1, 1, 1)
# count_of_4 = my_tuple.count(4)  # Count occurrences of 4    
# print("Count of 4: ", count_of_4)

# count_of_1 = my_tuple.count(1)  # Count occurrences of 1    
# print("Count of 1: ", count_of_1)

# index_of_3 = my_tuple.index(3)  # Find index of first occurrence of 3
# print("Index of 3: ", index_of_3)

# index_of_5 = my_tuple.index(5)  # Find index of first occurrence of 5
# print("Index of 5: ", index_of_5)


#============================SETS============================
my_set = {10,20,30}
print("SET basic example: ",my_set)
print(f"SET basic example with f-string: {my_set}")

#removing duplicates from a list using set
my_list = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
my_set_from_list = set(my_list)
print("SET from list: ", my_set_from_list)

numbers=[1, 2, 3, 4, 5, 1, 2, 3, 4, 5] # duplicate values allowed in list
unique_numbers = set(numbers) # duplicate values not allowed in set
print("numbers: ", numbers)
print("unique_numbers: ", unique_numbers)

#adding elements to a set
fruits_set = {"apple", "banana", "mango"}
fruits_set.add("orange")
print(fruits_set)
fruits_set.remove("apple")
print(fruits_set)
#fruits_set.remove("grapes")## This will raise a KeyError because "grapes" is not in the set
#print(fruits_set)


#adding multiple elements to a list
fruits_list = ["apple", "banana", "mango"]
fruits_list.append("orange")
print(fruits_list)

#SET union example
python_students = {"Rahul", "Priya", "Amit"}
java_students = {"Priya", "Amit", "Sneha"}
union_students = python_students.union(java_students)
pipesymbol_students = python_students | java_students
print("UNION All students:", union_students)
print("UNION All students:", pipesymbol_students)

#SET Intersection example
intersection_students = python_students.intersection(java_students)
ampherson_intersection = python_students & java_students
print("Intersection Students:", intersection_students)
print("Intersection Students:", ampherson_intersection)

#SET Difference example
difference_students = python_students.difference(java_students)
only_python = python_students - java_students
print("Difference Students:", difference_students)
print("Only Python Students:", only_python)
difference_students1 = java_students.difference(python_students)
only_python1 = java_students - python_students
print("Difference Students1:", difference_students1)
print("Only Python Students1:", only_python1)



#=============================Disctionaries=============================
student = {
    "name": "Rahul",
    "age": 21,
    "course": "Python",
    "city": "Hyderabad"
}

print(student)

print("Student Name:", student["name"])
print("Student Age:", student["age"])
print("Student Course:", student["course"])
print("Student City:", student["city"])

#Adding a new key-value pair to the dictionary
student["email"] = "rahul@example.com"
print("Student Email:", student["email"])
print("Student Data:", student)

#removing a key-value pair from the dictionary
student.pop("city")
print("Student Data after removing city:", student)

#clear the dictionary
student.clear()
print("Student Data after clearing:", student)

#updating an existing key-value pair in the dictionary
student["age"] = 22
print("Student Age:", student["age"])   

#We can loop through the disctionary
for key,value in student.items():
    print(key,":", value)

#We can loop the disctionary keys
for key in student:
    print("Student Key: ",key)

#We can loop the disctionary keys
for value in student.values():
    print("Student value: ",value)

marks = {
    "Rahul": 85,
    "Priya": 92,
    "Amit": 78,
    "Sneha": 95,
    "Krishna": 95
}

print("Rahul marks",marks["Rahul"])
highest = max(marks.values())
print("highest marks",highest)

top_student = max(marks, key=marks.get)
print(top_student)


