# NumPy is a Python Library, used for working with arrays. NumPy stands for Numerical Python.

import NumPy as np  # To use numpy, it should be import like this.
# as is used to create an alias while importing

arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(type(arr))    # It will send <class 'numpy.ndarray'>.

print(np.__version__)   # To check the version of NumPy.

# Dimensions in Array refers to nested array, that have array as thier elements, Some of them are:
# 0-D Arrays: arr = np.array(42)
# 1-D Arrays: arr = np.array([1, 2, 3, 4, 5])
# 2-D Arrays: arr = np.array([[1, 2, 3], [4, 5, 6]])   # often used to represent metrix, Metrix also have sub-module in numpy named numpy.mat.
# 3-D Arrays: arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

# To check the Dimensions, NumPy Arrays provides the ndim attribute.

a = np.array(42)    # 0-D Array.
b = np.array([1, 2, 3, 4, 5])   # 1-D Array.
c = np.array([[1, 2, 3], [4, 5, 6]])    # 2-D Array.
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])  # 3-d Array.

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

# Higher Dimensional Arrays: An array can have any number of dimensions, When the array is created, we can define the number of dimensions by using ndim argument.
arr1 = np.array([1, 2, 3, 4], ndmin=5)

print(arr1)
print('number of dimensions :', arr1.ndim)  # For the innermost dimension (5th dim) has 4 elements, the 4th dim has 1 element that is the vector, the 3rd dim has 1 element that is the matrix with the vector, the 2nd dim has 1 element that is 3D array and 1st dim has 1 element that is a 4D array.

# NumPy Array Indexing, It is the same as accessing an array element.

arr2 = np.array([1, 2, 3, 4])

print(arr2[2] + arr2[3])

print('5th element on 2nd row: ', c[1, 4])  # Access elements using index from 2D array.
print(d[0, 1, 2]) # Access elements using index from 3D array.
print('Last element from 2nd dim: ', c[1, -1])  # Access elements with Negative index.

# Array Slicing, taking elements from one given index to another given index.

# We pass slice instead of index like this: [start:end].
# We can also define the step, like this: [start:end:step].
# If we don't pass start its considered 0
# If we don't pass end its considered length of array in that dimension
# If we don't pass step its considered 1

arr3 = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr3[1:5])    # Start-end Slicing. [2 3 4 5]
print(arr3[4:])  # Start Slicing. [5 6 7]
print(arr3[:4])  # Start Slicing. [1 2 3 4]
print(arr3[-3:-1])  # Negative Slicing. [5 6]
print(arr3[1:5:2])  # Start-end-step Slicing. [2 4]
print(arr3[::2]) # Step Slicing. [1 3 5 7]

arr4 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr4[0:2, 1:4])   # Slicing of 2D Array. [[2 3 4], [7 8 9]]

# NumPy Data Types
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
# V : fixed chunk of memory for other type (void)

arr5 = np.array([1, 2, 3, 4])

print(arr5.dtype)   # To check the data type of an array object.