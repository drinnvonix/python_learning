x = 1    # int type is whole number, positive or negative, without decimals
y = 2.8  # float type is a number, positive or negative, containing one or more decimals
z = 1j   # complex type is a number, positive or negative, containing one or more decimals with a j as the imaginary part
# complex type can be

print(type(x))
print(type(y))
print(type(z))


# String

a = """This is a Multiline Strings
        This is the second line
        This is the third line"""

print(a)

a = "Hello, World!" # python strings are arrays of bytes representing unicode characters and can be accessed using indexing
print(a[1])

b = "Hello, World!"
print(b[:5]) # slicing of strings, it will return the characters from index 0 to 4 (5 is not included)

print(b[2:]) # slicing of strings, it will return the characters from index 2 to the end of the string

print(b[2:5]) # slicing of strings, it will return the characters from index 2 to 4 (5 is not included)

print(b[-5:-2]) # negative indexing, it will return the characters from index -5 to -3 (-2 is not included)

print(b.upper()) # upper() method returns the string in upper case

print(b.lower()) # lower() method returns the string in lower case

print(b.strip()) # strip() method removes any whitespace from the beginning or the end of the string

print(b.replace("o", "a")) # replace() method replaces a string with another string

print(b.split(" ")) # split() method splits the string into a list

a = "Hello"
b = "World"

c = a + b # concatenation of strings, it will join the two strings without any space in between
print(c)

c = a + " " + b # concatenation of strings, it will join the two strings with a space in between
print(c)


c = "Hello, World!"
for x in c: # loop through the string, it will print each character in the string
  print(x)

print(len(c)) # len() function returns the length of the string

txt = "Converstion of data types" # check if a substring is present in a string
print("data" in txt)

# can also use the not in keyword to check if a substring is not present in a string
txt = "Converstion of data types"
if "data" not in txt:
  print("No, 'data' is NOT present.")


age = 15
txt = f"My name is Bob, I am {age}" # f-strings are a way to format strings in python, it allows us to embed expressions inside string literals, using curly braces {}
print(txt)

txt = "We are the so-called \"Vikings\" from the north." 
# escape character \ is used to escape the double quotes inside the string
#\' : for single quote
#\\ : for backslash
#\n : for new line
#\t : for tab
#\r : for carriage return, means to move the cursor to the beginning of the line
#\b : for backspace
#\f : for form feed, means to move the cursor to the next line and to the beginning of the line
#\ooo : for octal value, means to represent a character using its octal value
#\xhh : for hex value, means to represent a character using its hex value

# string methods are built-in functions that can be used to manipulate strings in python. Some of the most commonly used string methods are:
# capitalize() - capitalizes the first character of the string
# casefold() - converts the string to lower case
# center() - centers the string in a field of a given width
# count() - counts the number of occurrences of a substring in the string
# encode() - encodes the string using a given encoding
# endswith() - checks if the string ends with a given substring
# find() - finds the first occurrence of a substring in the string
# format() - formats the string using placeholders
# index() - finds the first occurrence of a substring in the string and returns its index
# isalnum() - checks if all characters in the string are alphanumeric
# isalpha() - checks if all characters in the string are alphabetic
# isdigit() - checks if all characters in the string are digits
# islower() - checks if all characters in the string are lowercase
# isupper() - checks if all characters in the string are uppercase
# join() - joins a list of strings into a single string
# lower() - converts the string to lower case
# upper() - converts the string to upper case
# lstrip() - removes any whitespace from the beginning of the string
# rstrip() - removes any whitespace from the end of the string
# strip() - removes any whitespace from the beginning or the end of the string


# Boolean

# Boolean data type is a data type that can have one of two values: True or False. It is used to represent the truth value of an expression. In Python, the boolean data type is represented by the bool class.

a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

# The bool() function is used to convert a value to a boolean value. It returns True if the value is true, and False if the value is false. 
# Almost any value can be evaluated to a true, except empty values, such as 0, None, False, and empty strings or lists.
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

# for converstion of data types, we can use the following functions
# int() - converts to integer, it will remove the decimals if the number is float
# float() - converts to float, it will add decimals if the number is integer
# str() - converts to string, it will convert the number to a string representation
# complex() - converts to complex, it will add a j as the imaginary part if the number is integer or float