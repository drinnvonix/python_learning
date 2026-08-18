# NumPy is a Python library used for working with arrays.
# NumPy stands for Numerical Python.  

# To use NumPy, it should be imported like this:
# import numpy as np
# 'as' is used to create an alias while importing.

import numpy as np


# Creating a basic NumPy array.
arr = np.array([1, 2, 3, 4, 5])

print(arr)
print(type(arr))    # It will send <class 'numpy.ndarray'>.

# To check the installed version of NumPy.
print(np.__version__)



# NumPy CREATING ARRAYS

# NumPy arrays can have different numbers of dimensions.

# 0-D Array:
arr = np.array(42)

# 1-D Array:
arr = np.array([1, 2, 3, 4, 5])

# 2-D Array:
# Often used to represent a matrix.
arr = np.array([[1, 2, 3], [4, 5, 6]])

# 3-D Array:
arr = np.array([
    [[1, 2, 3], [4, 5, 6]],
    [[1, 2, 3], [4, 5, 6]]
])


# Checking dimensions using ndim.
a = np.array(42)                              # 0-D Array.
b = np.array([1, 2, 3, 4, 5])               # 1-D Array.
c = np.array([[1, 2, 3], [4, 5, 6]])        # 2-D Array.
d = np.array([                             # 3-D Array.
    [[1, 2, 3], [4, 5, 6]],
    [[1, 2, 3], [4, 5, 6]]
])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)


# Higher Dimensional Arrays:
# An array can have any number of dimensions.
# When the array is created, we can define the number of
# dimensions by using the ndmin argument.

arr1 = np.array([1, 2, 3, 4], ndmin=5)

print(arr1)
print('number of dimensions:', arr1.ndim)

# In this example:
# The innermost dimension has 4 elements.
# The other dimensions contain one element at each level.

# NumPy ARRAY INDEXING

# NumPy Array Indexing is the same as accessing an array element.
# Indexing starts from 0.

arr2 = np.array([1, 2, 3, 4])

print(arr2[2])                 # Access the 3rd element.
print(arr2[2] + arr2[3])       # Add the 3rd and 4th elements.

# Accessing elements from a 2-D array.
c = np.array([[1, 2, 3], [4, 5, 6]])

print('3rd element on 2nd row:', c[1, 2])

# Accessing elements from a 3-D array.
d = np.array([
    [[1, 2, 3], [4, 5, 6]],
    [[1, 2, 3], [4, 5, 6]]
])

print(d[0, 1, 2])

# Negative indexing starts from the end.
print('Last element from 2nd row:', c[1, -1])

# NumPy ARRAY SLICING

# Array slicing means taking elements from one given index
# to another given index.

# Syntax:
# [start:end]

# We can also define the step:
# [start:end:step]

# If start is not passed, it is considered 0.
# If end is not passed, it is considered the length of the array.
# If step is not passed, it is considered 1.

arr3 = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr3[1:5])       # Start-end slicing: [2 3 4 5]
print(arr3[4:])        # Start slicing: [5 6 7]
print(arr3[:4])        # End slicing: [1 2 3 4]
print(arr3[-3:-1])     # Negative slicing: [5 6]
print(arr3[1:5:2])     # Start-end-step slicing: [2 4]
print(arr3[::2])       # Step slicing: [1 3 5 7]

# Slicing a 2-D array.
arr4 = np.array([
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10]
])

print(arr4[0:2, 1:4])  # [[2 3 4]
                       #  [7 8 9]]

# NumPy DATA TYPES

# NumPy supports several data types.
# i : integer
# b : boolean
# u : unsigned integer
# f : float
# c : complex float
# m : timedelta
# M : datetime
# O : object
# S : string
# U : unicode string
# V : fixed-size memory block (void)

arr5 = np.array([1, 2, 3, 4])

print(arr5.dtype)       # Check the data type of an array.

# Creating an array with a specific data type.
arr6 = np.array([1, 2, 3], dtype='f')
print(arr6)
print(arr6.dtype)

# NumPy COPY VS VIEW

# A copy creates a completely independent array.
# Changes made to the copy do not affect the original array.

arr7 = np.array([1, 2, 3, 4])

copy_arr = arr7.copy()

copy_arr[0] = 100

print('Original array:', arr7)
print('Copy array:', copy_arr)


# A view does not create a completely independent array.
# A view looks at the same underlying data.
# Changes made to the view can affect the original array.

arr8 = np.array([1, 2, 3, 4])

view_arr = arr8.view()

view_arr[0] = 100

print('Original array:', arr8)
print('View array:', view_arr)


# The base attribute can be used to check whether an array
# is based on another array.

print(copy_arr.base)     # None because copy_arr is a copy.
print(view_arr.base)     # Shows the original array because it is a view.

# NumPy ARRAY SHAPE

# The shape of an array is the number of elements in each dimension.
# The shape is returned as a tuple.

arr9 = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(arr9.shape)        # (2, 3)
# 2 rows and 3 columns.


# Shape can also be used to determine the dimensions of
# higher-dimensional arrays.

arr10 = np.array([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
])

print(arr10.shape)       # (2, 2, 2)

# NumPy ARRAY RESHAPE

# Reshaping means changing the shape of an array
# without changing its data.

arr11 = np.array([1, 2, 3, 4, 5, 6])

new_arr = arr11.reshape(2, 3)

print(new_arr)


# Reshape to 3 rows and 2 columns.

new_arr = arr11.reshape(3, 2)

print(new_arr)

# The total number of elements must remain the same.
# 6 elements can become 2x3 or 3x2, but not 2x2.

# Reshaping into an unknown dimension using -1.
# NumPy automatically calculates the missing dimension.

new_arr = arr11.reshape(2, -1)

print(new_arr)

# Flattening an array means converting it into a 1-D array.

arr12 = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(arr12.reshape(-1))

# NumPy ARRAY ITERATING

# Iterating means going through each element of an array.

arr13 = np.array([1, 2, 3, 4, 5])

for x in arr13:
    print(x)

# Iterating through a 2-D array.
# The first loop returns each row.

arr14 = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

for row in arr14:
    print(row)

# To access every individual element in a 2-D array,
# use a nested loop.

for row in arr14:
    for x in row:
        print(x)

# Iterating through higher-dimensional arrays requires
# additional nested loops.

# np.nditer() can be used to iterate through every element
# regardless of the number of dimensions.

arr15 = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

for x in np.nditer(arr15):
    print(x)

# NumPy ARRAY JOIN

# Joining means putting the contents of two or more arrays
# into a single array.

# NumPy does not have a general np.join() function.
# Common functions used for joining are:
# np.concatenate()
# np.stack()
# np.hstack()
# np.vstack()

arr16 = np.array([1, 2, 3])
arr17 = np.array([4, 5, 6])

# concatenate() joins arrays along an existing axis.

joined = np.concatenate((arr16, arr17))

print(joined)

# Joining 2-D arrays along axis 0 means joining rows.

arr18 = np.array([
    [1, 2],
    [3, 4]
])

arr19 = np.array([
    [5, 6],
    [7, 8]
])

print(np.concatenate((arr18, arr19), axis=0))

# Joining 2-D arrays along axis 1 means joining columns.
print(np.concatenate((arr18, arr19), axis=1))

# stack() joins arrays along a new axis.
print(np.stack((arr16, arr17)))

# vstack() stacks arrays vertically.
print(np.vstack((arr16, arr17)))

# hstack() stacks arrays horizontally.
print(np.hstack((arr16, arr17)))

# NumPy ARRAY SPLIT

# Splitting means breaking one array into multiple arrays.

arr20 = np.array([1, 2, 3, 4, 5, 6])

# split() divides an array into equal-sized sub-arrays.
# The number of elements must be divisible by the number of splits.

print(np.split(arr20, 3))

# array_split() is more flexible and can split arrays
# even when the elements cannot be divided equally.

arr21 = np.array([1, 2, 3, 4, 5, 6, 7])

print(np.array_split(arr21, 3))

# Splitting a 2-D array vertically.

arr22 = np.array([
    [1, 2],
    [3, 4],
    [5, 6],
    [7, 8]
])

print(np.vsplit(arr22, 2))

# Splitting a 2-D array horizontally.

arr23 = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8]
])

print(np.hsplit(arr23, 2))

# NumPy ARRAY SEARCH

# where() is used to find indexes where a condition is True.

arr24 = np.array([10, 20, 30, 40, 50])

print(np.where(arr24 == 30))

# Find indexes of elements that are divisible by 2.

print(np.where(arr24 % 2 == 0))

# searchsorted() finds the index where a value should be inserted
# to keep the array sorted.

arr25 = np.array([10, 20, 30, 40])

print(np.searchsorted(arr25, 25))

# Find the insertion position for multiple values.

print(np.searchsorted(arr25, [15, 25, 35]))

# NumPy ARRAY SORT

# sort() returns a sorted copy of the array.
# The original array is not changed.

arr26 = np.array([3, 1, 5, 2, 4])

print(np.sort(arr26))
print(arr26)       # Original array remains unchanged.

# Sorting strings.

arr27 = np.array(['banana', 'apple', 'cherry'])

print(np.sort(arr27))

# Sorting a 2-D array.
# Each row is sorted by default.

arr28 = np.array([
    [3, 2, 1],
    [6, 5, 4]
])

print(np.sort(arr28))

# NumPy ARRAY FILTER

# Filtering means selecting elements from an array
# based on a condition.

arr29 = np.array([10, 20, 30, 40, 50])

# Create a Boolean array.
filter_arr = arr29 > 25

print(filter_arr)

# Use the Boolean array to filter the original array.
print(arr29[filter_arr])

# Filtering can also be written directly.
print(arr29[arr29 > 25])

# Filtering even numbers.
arr30 = np.array([1, 2, 3, 4, 5, 6])
print(arr30[arr30 % 2 == 0])

# Filtering numbers greater than 10 and less than 40.
arr31 = np.array([5, 10, 15, 20, 25, 30, 35, 40])
print(arr31[(arr31 > 10) & (arr31 < 40)])