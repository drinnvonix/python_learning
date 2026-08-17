# Control statements in Python are used to control the flow of execution of the program. They allow you to make decisions, repeat actions, and handle exceptions. The main control statements in Python include:

# 1. Conditional Statements:
#    - if statement: Executes a block of code if a specified condition is true.

number = 9
if number < 0:
  print("The number is negative")

#    - if-else statement: Executes one block of code if the condition is true, and another block if the condition is false.

number = 9
if number < 0:
    print("The number is negative")
else:
    print("The number is positive or zero")

#    - if-elif-else statement: Allows you to check multiple conditions and execute different blocks of code based on which condition is true.

score = 85

if score >= 90:
  print("Grade: A")
elif score >= 80:
  print("Grade: B")
elif score >= 70:
  print("Grade: C")
elif score >= 60:
  print("Grade: D")
else:
  print("Grade: F")

# Multiple conditions in one line
username = ""
display_name = username if username else "Guest"
print("Welcome,", display_name)

# Multiple conditions in one line using logical operators
age = 55
is_student = False
has_discount_code = True

if (age < 18 or age > 65) and not is_student or has_discount_code:
  print("Discount applies!")

# Nested if statements: You can have if statements inside other if statements to create more complex decision-making structures.
x = 49

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

# Match statement: Introduced in Python 3.10, the match statement allows you to perform pattern matching on values, similar to switch-case statements in other languages.
day = 4

match day:
  case 1:
    print("Monday")
  case 2:
    print("Tuesday")
  case 3:
    print("Wednesday")
  case 4:
    print("Thursday")
  case 5:
    print("Friday")
  case 6:
    print("Saturday")
  case 7:
    print("Sunday")
  case _:
    print("Invalid day")

# 2. Looping Statements:
#    - for loop: Iterates over a sequence (like a list, tuple, or string) and executes a block of code for each item in the sequence.
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

  # break, continue, else and pass statements can also be used within loops to control the flow of execution.
  # also use the range() function to generate a sequence of numbers for iteration.
  # can also be used as nested loops, where one loop is placed inside another loop.

#    - while loop: Repeats a block of code as long as a specified condition is true.
i = 1
while i < 10:
  print(i)
  i += 1

  # break, continue, else and pass statements can also be used within loops to control the flow of execution.

# 3. Control Flow Statements:
#    - break statement: Exits the nearest enclosing loop prematurely.

i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

#    - continue statement: Skips the rest of the code inside the loop for the current iteration and moves to the next iteration.

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
  
#    - pass statement: A null operation; it is used as a placeholder when a statement is required syntactically but you do not want any command or code to execute.
value = 50

if value < 0:
  print("Negative value")
elif value == 0:
  pass # Zero case - no action needed
else:
  print("Positive value")