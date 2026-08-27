#String printing and length calculation

name = "Koteswar"
print(name)
length = len(name)
print("Length of the name is: ", length)

name = 'Hari Surya'
print(name)
length = len(name)
print("Length of the name is: ", length)

name='''Koteswar is good boy'''
print(name)
length = len(name)
print("Length of the name is: ", length)

name="""This is python programme"""
print(name)
length = len(name)
print("Length of the name is: ", length)

'''this is a multi-line comment. It can span multiple lines and is often used for documentation or explanations within the code.'''
"""this is a multi-line comment. It can span multiple lines and is often used for documentation or explanations within the code."""

#String Indexing

name="Koteswar"
#name = "K  o  t  e  s  w  a  r"
#        0  1  2  3  4  5  6  7   indexing starts from 0, so the first character 'K' is at index 0, the second character 'o' is at index 1, and so on. The last character 'r' is at index 7.
#       -8 -7 -6 -5 -4 -3 -2 -1   indexing starts from -1, so the last character 'r' is at index -1, the second last character 'a' is at index -2, and so on. The first character 'K' is at index -8.

print("First character of the name is: ", name[0])
print("Last character of the name is: ", name[-1])  

print(name[0])  # Output: K
print(name[1])  # Output: o     
print(name[2])  # Output: t
print(name[3])  # Output: e
print(name[4])  # Output: s
print(name[5])  # Output: w
print(name[6])  # Output: a
print(name[7])  # Output: r
print(" ")  # Output: empty line for better readability
print(name[-1])  # Output: r
print(name[-2])  # Output: a
print(name[-3])  # Output: w
print(name[-4])  # Output: s
print(name[-5])  # Output: e
print(name[-6])  # Output: t  #name[-6+8]  # Output: t
print(name[-7])  # Output: o  #name[-7+8]  # Output: o
print(name[-8])  # Output: K

print(" ")  # Output: empty line for better readability

#String Slicing

name = "Koteswar"
print(name[0:4])  # Output: Kote  0 to n-1, so 0 to 4-1=3, so the characters at index 0, 1, 2, and 3 are included in the output.
print(name[4:8])  # Output: swar  4 to n-1, so 4 to 8-1=7, so the characters at index 4, 5, 6, and 7 are included in the output.

print(name[1:6])  # Output: otesw     1 to n-1, so 1 to 6-1=5, so the characters at index 1, 2, 3, 4, and 5 are included in the output.
print(name[0:8])  # Output: Koteswar  0 to n-1, so 0 to 8-1=7, so the characters at index 0, 1, 2, 3, 4, 5, 6, and 7 are included in the output.

print(name[2:-1]) # Output: teswa  2 to n-1, so 2 to 8-1=7, so the characters at index 2, 3, 4, 5, and 6 are included in the output.

print(name[0:8:2])  # Output: Ktsa       0 to n-1, so 0 to 8-1=7, so the characters at index 0, 2, 4, and 6 are included in the output. The step value of 2 means that every second character is included in the output.
print(name[1:8:3])  # Output: osr        1 to n-1, so 1 to 8-1=7, so the characters at index 1, 3, 5, and 7 are included in the output. The step value of 3 means that every third character is included in the output.
print(name[0:8:1])  # Output: Koteswar   0 to n-1, so 0 to 8-1=7, so the characters at index 0, 1, 2, 3, 4, 5, 6, and 7 are included in the output. The step value of 1 means that every character is included in the output.

print(name[:8])  # Output: Koteswar      0 to n-1, so 0 to 8-1=7, so the characters at index 0, 1, 2, 3, 4, 5, 6, and 7 are included in the output. The step value is not specified, so it defaults to 1, meaning that every character is included in the output.
print(name[0:])  # Output: Koteswar      0 to n-1, so 0 to 8-1=7, so the characters at index 0, 1, 2, 3, 4, 5, 6, and 7 are included in the output. The step value is not specified, so it defaults to 1, meaning that every character is included in the output.
print(name[:])   # Output: Koteswar      0 to n-1, so 0 to 8-1=7, so the characters at index 0, 1, 2, 3, 4, 5, 6, and 7 are included in the output. The step value is not specified, so it defaults to 1, meaning that every character is included in the output.

#String Methods

text="Hello,Koteswar" #Strings are immutable, meaning they cannot be changed after they are created. However, Python provides a variety of string methods that allow you to manipulate and work with strings in different ways.
#text[0]="H"  #you can do this
print("\nString Methods:\n")
text = "Hello, Python!"  
print(text.upper())  # Output: HELLO, PYTHON!
print(text.lower())  # Output: hello, python!
print(text.capitalize())  # Output: Hello, python!
print(text.title())  # Output: Hello, Python!
print(text.swapcase())  # Output: hELLO, pYTHON!

#string Removing whitespace from the beginning and end of a string
print("\nString Removing Whitespace:\n")
text = "   Hello, Python!   "
print(text)           # Output: Hello, Python!
print(text.strip())   # Output: Hello, Python!
print(text.lstrip())  # Output: Hello, Python!  
print(text.rstrip())  # Output: Hello, Python!

#String Searching and Replacing
print("\nString Searching and Replacing:\n")
text ="Python is fun"
print("\"is\" position: ", text.find("is")) # Output: 7
print(text.replace("fun","awesome")) # Output: "Python is awesome"

#String Splitting and Joining
print("\nString Splitting and Joining:\n")
text ="apple,banana,orange"
fruits = text.split(",")
print(fruits) # Output: ['apple', 'banana', 'orange']

#String Joining
print("\nString Joining:\n")
fruits = ['apple', 'banana', 'orange']
text = ",".join(fruits)
print(text) # Output: apple,banana,orange

#String properties and checks
print("\nString Properties and Checks:\n")
text = "hello1234"
print("Is alphanumeric:", text.isalnum())  # Output: True
print("Is alphabetic:", text.isalpha())  # Output: False
print("Is decimal:", text.isdecimal())  # Output: False
print("Is digit:", text.isdigit())  # Output: False
print("Is lowercase:", text.islower())  # Output: True
print("Is uppercase:", text.isupper())  # Output: False
print("Is whitespace:", text.isspace())  # Output: False

#string formatting
print("\nString Formatting:\n") 
name ="Alice"
age =30
print("My name is {} and I am {} years old.".format(name, age))
print(f"My name is {name} and I am {age} years old.")

#len() - Get Length of a String 
text ="Hello, Python!"
print(len(text)) # Output: 14

#ord() and chr() - Character Encoding
print(ord('A')) # Output: 65
print(chr(65)) # Output: 'A'