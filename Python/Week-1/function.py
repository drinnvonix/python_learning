# Function is a block of code which run when it is called, It can reutrn data as a result.
# Function name must start with letter or underscore, can only contains letters, numbers and underscore, and also case-sensitive.

def my_function():  # def is used to defined a new function.
  return "Hello from a function"

msg = my_function()   # To call function
print(msg)

# Argument Function

def my_function(name): # name is a parameter
  print("Hello", name)

my_function("John") # "John" is an argument

# Default value as a parameter
def my_function(country = "Norway"):
  print("I am from", country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

# Keyeord argument
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function(animal = "dog", name = "Buddy")

# Send list as an argument
def my_function(fruits):
  for fruit in fruits:
    print(fruit)

my_fruits = ["apple", "banana", "cherry"]
my_function(my_fruits)

# Return Value
def my_function(x, y):
  return x + y

result = my_function(4, 5)
print(result)

# Return Different data types
def my_function():
  return ["apple", "banana", "cherry"]

fruits = my_function()
print(fruits[0])
print(fruits[1])
print(fruits[2])

# *args, used when don't know how many arguments will be passed into the function.
def my_function(*numbers):
  total = 0
  for num in numbers:
    total += num
  return total

print(my_function(1, 2, 3))
print(my_function(10, 20, 30, 40))
print(my_function(5))

# *kwargs, allows a function to accept any number of keyword aarguments.
def my_function(username, **details):
  print("Username:", username)
  print("Additional details:")
  for key, value in details.items():
    print(" ", key + ":", value)

my_function("emil123", age = 25, city = "Oslo", hobby = "coding")

# Scope of variable inside function
# Local : variable created inside a function belogns to local scope.
# Global : variable created in the main body of code, belogns to global scope.
# NonLocal : keyword used to work with variables inside nested functions.

# Python follows LEGB rule, when looking up variable names.
# L : Inside current function.
# E : Inside enclosing function(inner to outer).
# G : At the top level of function.
# B : Built-in namespace.

x = "global"

def outer():
  x = "enclosing"
  def inner():
    x = "local"
    print("Inner:", x)
  inner()
  print("Outer:", x)

outer()
print("Global:", x)


# Decorators add extra behavior to a function without changing the function code, it takes another functio as input and return new function.
def changecase(func):
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Hello Sally"

@changecase
def otherfunction():
  return "I am speed!"

print(myfunction())
print(otherfunction())

# Lambda Function is a small anonymous function, it takes an argument but can only have one expression.
# Syntax : lambda argument : expression

x = lambda a, b, c : a + b + c
print(x(1, 3, 2))

# Lambda function with regular funcation
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(15))
print(mytripler(18))

# Lambda with built-in function
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(doubled)
print(odd_numbers)

# Recursion function calls itself.
# Every recursive function has two parts:
# Base case : A condition that stops the recursion.
# Recursive case : The function calling itself with a modified argument.
def factorial(n):
  # Base case
  if n == 0 or n == 1:
    return 1
  # Recursive case
  else:
    return n * factorial(n - 1)

print(factorial(5))

# Recursion with list
def find_max(numbers):
  if len(numbers) == 1:
    return numbers[0]
  else:
    max_of_rest = find_max(numbers[1:])
    return numbers[0] if numbers[0] > max_of_rest else max_of_rest

my_list = [14, 58, 79, 55, 123]
print(find_max(my_list))

# Recursion Depth Limmit, by default it is 1000
import sys
sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())
