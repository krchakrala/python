#map() function applies a given function to all items in an input list (or any iterable) and returns a map object (which is an iterator).
#Definition:map() takes each element from a collection, applies a function, and returns the transformed values.
#syntax: map(function, iterable)

numbers = [1, 2, 3, 4, 5]
result = map(lambda x: x * 2, numbers)
print(list(result))

#map() function can be used with addition in lambda
numbers1 = [10, 20, 30, 40, 50]
result1 = map(lambda x: x + 2, numbers1)
print(list(result1))

#without lambda function
def square(number):
    return number * number

numbers2 = [1, 2, 3, 4, 5]
result2 = map(square, numbers2)
print(set(result2))

#map() function can be used with Salary increment example
salaries = [30000, 40000, 50000]
new_salaries = map(lambda salary: salary * 1.10, salaries)
print(list(new_salaries))

#filter() function is used to filter the given iterable (list, tuple, etc.) with the help of a function that tests each element in the iterable to be true or not.
#Definition:filter() takes each element from a collection, applies a function, and returns the satisfied values.
#syntax: filter(function, iterable)
#filter() function can be used with even number example
numbers3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result3 = filter(lambda x: x % 2 == 0, numbers3)
print(list(result3))

#map() and filter() functions can be used together to perform operations on filtered data.
numbers5 = [1, 2, 3, 4, 5]
result51 = map(lambda x: x *2 , numbers5)
result52 = filter(lambda x: x % 2 == 0, numbers5)
print(list(result51))
print(list(result52))

#filter() function can be used with condition in lambda
numbers6 = [5, 10, 15, 20, 25]
result6 = filter(lambda x: x > 10, numbers6)
print(list(result6))

#filter() function can be used with Salary example
salaries = [25000, 40000, 55000, 30000, 65000]
high_salaries = filter(lambda salary: salary > 40000, salaries)
print(list(high_salaries))

#reduce() function is used to apply a particular function passed in its argument to all of the list elements mentioned in the sequence passed along. This function is defined in "functools" module.
#Definition:reduce() takes each element from a collection, applies a function, and returns a single value.
#syntax: reduce(function, iterable)
from functools import reduce
numbers = [1, 2, 3, 4, 5]
result = reduce(lambda x, y: x + y, numbers)
print(result)

#map(), filter() and reduce() functions can be used together to perform operations on filtered data.
from functools import reduce
prices = [100, 200, 300, 400, 500]
total = reduce(
    lambda x, y: x + y,
    map(
        lambda price: price * 0.90, #[270, 360, 450]
        filter(lambda price: price >= 300, prices) #[300, 400, 500]
    )
)
print(total)

#walrus operator :=
#The main purpose is to assign and use a value at the same time, avoiding repeated calculations or function calls.
x=10
print("without Walrus operator with x value: ",x)

print("with Walrus operator with x value: ",(x:=10))
print("with Walrus operator with x value: ",x+10)




