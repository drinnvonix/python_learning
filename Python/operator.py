# Operators are used to perform operations on variables and values.

# Arithmetic operators are used to perform mathematical operations like addition, subtraction, multiplication, division, etc. The following are the arithmetic operators in Python:
# + : addition, to add two numbers
# - : subtraction, to subtract one number from another
# * : multiplication, to multiply two numbers
# / : division, to divide one number by another
# % : modulus, to get the remainder of a division
# ** : exponentiation, to raise a number to the power of another number
# // : floor division, to get the integer part of a division

x = 10
y = 3

print(x + y) # addition
print(x - y) # subtraction
print(x * y) # multiplication
print(x / y) # division
print(x % y) # modulus
print(x ** y) # exponentiation
print(x // y) # floor division

# Assignment operators are used to assign values to variables. The following are the assignment operators in Python:
# = : assigns a value to a variable
# += : adds a value to a variable and assigns the result to the variable
# -= : subtracts a value from a variable and assigns the result to the variable
# *= : multiplies a variable by a value and assigns the result to the variable
# /= : divides a variable by a value and assigns the result to the variable
# %= : gets the modulus of a variable and a value and assigns the result to the variable
# **= : raises a variable to the power of a value and assigns the result to the variable
# //= : gets the floor division of a variable and a value and assigns the result to the variable
# &= : performs a bitwise AND operation on a variable and a value and assigns the result to the variable
# |= : performs a bitwise OR operation on a variable and a value and assigns the result to the variable 
# ^= : performs a bitwise XOR operation on a variable and a value and assigns the result to the variable
# >>= : performs a bitwise right shift operation on a variable and a value and assigns the result to the variable
# <<= : performs a bitwise left shift operation on a variable and a value and assigns the
# := : assigns a value to a variable as part of an expression (walrus operator)

x = 5 # assignment
x += 3 # addition assignment
x -= 2 # subtraction assignment
x *= 4 # multiplication assignment
x /= 2 # division assignment
x %= 3 # modulus assignment
x **= 2 # exponentiation assignment
x //= 2 # floor division assignment
# x &= 2 # bitwise AND assignment
# x |= 2 # bitwise OR assignment
# x ^= 2 # bitwise XOR assignment
# x >>= 2 # bitwise right shift assignment
# x <<= 2 # bitwise left shift assignment

numbers = [1, 2, 3, 4, 5]

if (count := len(numbers)) > 2: # walrus operator, assigns the length of the list to the variable count and checks if it is greater than 2
    print(f"List has {count} elements")

# Ternary operator is a shorthand way of writing an if-else statement. It is also known as a conditional expression. The syntax for the ternary operator is:
# value_if_true if condition else value_if_false
num = 4

x = "WEEKEND!" if num > 5 else "Workday"

print(x)

# Nested ternary operator is a shorthand way of writing multiple if-else statements. It is also known as a conditional expression. The syntax for the nested ternary operator is:
# value_if_true if condition1 else value_if_false if condition2 else value_if_true

num = 5

x = "Fri" if num == 5 else "Sat" if num == 6 else "Sun" if num == 7 else "weekday"

print(x)

# Comparison operators are used to compare two values. The following are the comparison operators in Python:
# == : equal to, checks if two values are equal
# != : not equal to, checks if two values are not equal
# > : greater than, checks if one value is greater than another
# < : less than, checks if one value is less than another
# >= : greater than or equal to, checks if one value is greater than or equal to another
# <= : less than or equal to, checks if one value is less than or equal to another

a = 10
b = 20

print(a == b) # equal to
print(a != b) # not equal to
print(a > b) # greater than
print(a < b) # less than
print(a >= b) # greater than or equal to
print(a <= b) # less than or equal to

x = 8
print(1 < x < 10)   #alllows for chaining of comparison operators, it will return True if x is greater than 1 and less than 10

# Logical operators are used to combine conditional statements. The following are the logical operators in Python:
# and : returns True if both statements are true
# or : returns True if one of the statements is true
# not : returns True if the statement is false

print(1 < x and x < 10)
print(1 < x or x > 10)
print(not(x > 7 and x < 10))

# Identity operators are used to compare the memory locations of two objects. The following are the identity operators in Python:
# is : returns True if both variables are the same object
# is not : returns True if both variables are not the same object

x = ["ABC", "XYZ"]
y = ["ABC", "XYZ"]
z = x

print(x is z)
print(x is not y)
print(x == y)

# Differentiate between identity operators and comparison operators. Identity operators compare the memory locations of two objects, while comparison operators compare the values of two objects.
# is : Checks if both variables point to the same object in memory
# == : Checks if the values of both variables are equal

# Membership operators are used to test if a sequence is presented in an object. The following are the membership operators in Python:
# in : returns True if a sequence with the specified value is present in the object
# not in : returns True if a sequence with the specified value is not present in the object
# Membership operators can be used with strings, lists, tuples, sets, and dictionaries. They can be used to check if a value is present in a sequence or not.

x = ["ABC", "XYZ"]
y = "ABC"

print(y in x)
print(y not in x)

# Bitwise operators are used to compare (binary) numbers. The following are the bitwise operators in Python:
# & : AND, sets each bit to 1 if both bits are 1
# | : OR, sets each bit to 1 if one of two bits is 1
# ^ : XOR, sets each bit to 1 if only one of two bits is 1
# ~ : NOT, inverts all the bits
# << : zero fill left shift, shifts the bits of the first operand to the left by the number of positions specified by the second operand
# >> : signed right shift, shifts the bits of the first operand to the right by the

print(1 & 3) # AND
print(1 | 3) # OR
print(1 ^ 3) # XOR
print(~1) # NOT
print(1 << 3) # zero fill left shift
print(1 >> 3) # signed right shift

# Operators precedence is the order in which the operators are evaluated in an expression. The following is the order of precedence of operators in Python:
# 1. Parentheses ()
# 2. Exponentiation (**)
# 3. Unary plus and minus (+x, -x)
# 4. Multiplication, division, floor division, and modulus (*, /, //, %)
# 5. Addition and subtraction (+, -)
# 6. Bitwise shift operators (<<, >>)
# 7. Bitwise AND (&)
# 8. Bitwise XOR (^)
# 9. Bitwise OR (|)
# 10. Comparison operators (==, !=, >, <, >=, <=)
# 11. Identity operators (is, is not)
# 12. Membership operators (in, not in)
# 13. Logical operators (and, or, not)