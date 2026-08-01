# For loop

#For i in range(1, 11): range function goes from 1 to (n-1) ie is 10 in this case
for i in range(1, 11): #range function goes from 1 to (n-1) ie is 10 in this case
    print(i) #print the value of i for each iteration of the loop
    #print(i+2) #print the value of i+2 for each iteration of the loop
   
for i in range(1, 11): 
    print("6 x", i, "=", 6*i) #print the multiplication table of 5

#Basic while loop
i=1
while i<6:
    print(i)
    i=i+1

# read j and k from user and print all numbers from j to k using while loop
j= int(input("Enter the j number: "))
k= int(input("Enter the k number: "))
while j<=k:
    print(j)
    j=j+1

# read j and k from user and print all numbers with +2 from j to k using while loop
j= int(input("Enter the j number: "))
k= int(input("Enter the k number: "))
while j<=k:
    print(j)
    j=j+2

#infinite loop
i=1
while False:  
    print(i)
    i=i+1

#break in for loop
print("break statement in for loop") 
for i in range(1, 11):
    if i==5:
        break # BREAK statement stops the loop when i is equal to 5
    print(i)  

#continue in for loop
print("continue statement in for loop") 
for i in range(1, 11):
    if i==8:
        continue # CONTINUE statement skips the current iteration and moves to the next iteration of the loop
    print(i)  

#pass in for loop
print("pass statement in if condition") 
for i in range(1, 11):
    if i==5:
        pass # PASS statement does nothing and continues to the next line of code
    print(i)  

print("pass statement print nothing") 
i=3
if i==32:
    print("i is equal to 32")
else:
    pass # PASS statement does nothing and continues to the next line of code


