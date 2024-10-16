import numpy as np

arr = np.array(['apple', 'banana', 'cherry'])
print(arr.dtype)

arr = np.array([1, 2, 3, 4, 5])
print(arr.dtype)

print("-----------------------------------------------------------")

# Creating Arrays With a Defined Data Type

arr = np.array([1, 2, 3, 4], dtype='S')
print(arr)
print(arr.dtype)

print("-----------------------------------------------------------")

# Create an array with data type 4 bytes integer:

arr = np.array([1, 2, 3, 4], dtype='i4')
print(arr)
print(arr.dtype)

print("-----------------------------------------------------------")

arr = np.array([1.1, 2.1, 3.1])

newarr = arr.astype('i')

print(newarr)
print(newarr.dtype)