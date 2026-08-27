#Creating a list
numbers=[1,2,3,4,5,6,7,8,9]
print(numbers)

mixed = [1, 2.5, "Hello", True, [1, 2, 3], (4, 5), {6, 7}, {"name": "Alice", "age": 25}]
print(mixed)

#Common List Operations
my_list =[1,2,3]
print("List of elements: ",my_list)
my_list.append(4) # [1, 2, 3, 4]
print("After appending 4: ",my_list)
my_list.insert(5,9) # [1, 2, 3, 4, 9]
print("After inserting 9 at index 5: ",my_list)
my_list.remove(2) # [1, 3, 4, 9]
print("After removing 2: ",my_list)
my_list.pop() # Removes last element -> [1, 99, 3]
print("After popping last element: ",my_list)
my_list.reverse() # [3, 99, 1]
print("After reversing: ",my_list)
my_list.sort() # [1, 3, 99]
print("After sorting: ",my_list)

#List Comprehensions
squared_numbers = [x**2 for x in numbers]
print("Squared numbers: ", squared_numbers)


# Tuples
my_tuple = (1, 2, 3, 4, 5)
print("Tuple: ", my_tuple)

print("Tuple: ", my_tuple[3]) # Accessing elements in a tuple 4 POSITIONAL INDEXING

single_element_tuple = (42,)   # Tuple with one element (comma required)
print("Single element tuple: ", single_element_tuple)

a,b,e,d,c = my_tuple           #unpacking a tuple into variables
print("Unpacked values: ", a, b, c, d, e)

#Count and Index in a tuple
my_tuple = (1, 2, 3, 4, 5, 2, 3, 4, 5, 4, 4, 1, 1, 1, 1)
count_of_4 = my_tuple.count(4)  # Count occurrences of 4    
print("Count of 4: ", count_of_4)

count_of_1 = my_tuple.count(1)  # Count occurrences of 1    
print("Count of 1: ", count_of_1)

index_of_3 = my_tuple.index(3)  # Find index of first occurrence of 3
print("Index of 3: ", index_of_3)

index_of_5 = my_tuple.index(5)  # Find index of first occurrence of 5
print("Index of 5: ", index_of_5)
