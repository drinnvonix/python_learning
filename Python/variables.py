x = 5   # x is int type variable
y = "John"  # y is string type variable
# for string we can use both single and double quotes
Y = 'John'  # Y is string type but it is different from y because python is case sensitive
print(x)    # print() is used to display
print(type(x))  #type() is used to display type of variable    
print(y)    # print() is used to display
print(type(y))  #type() is used to display type of variable    
print(Y)    # print() is used to display
print(type(Y))  #type() is used to display type of variable    


# assign multiple values to multiple variables

a, b, c = "Orange", "Banana", "Cherry"
print("The value of a is:", a)
print("The value of b is:", b)
print("The value of c is:", c)


# assign the same value to multiple variables
a = b = c = "Orange"
print("The value of a is:", a)
print("The value of b is:", b)
print("The value of c is:", c)

# assign values from a list/tuple to variables[Unpacking of Collections]
fruits = ["apple", "banana", "cherry"]
a, b, c = fruits
print("The value of a is:", a)
print("The value of b is:", b)
print("The value of c is:", c)


#global vs. local variables
x = "awesome" # global variable, can be used anywhere in the program, also defined using global keyword inside a function

def myfunc():
  x = "fantastic" # local variable
  print("Python is " + x)

myfunc()

print("Python is " + x)

