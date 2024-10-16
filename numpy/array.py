import numpy as np

# Create a numpy array
arr = np.array([1, 2, 3, 4, 5])
print(arr)

print(type(arr))


print("-----------------------------------------------------------")

#check how many dimensions the arrays have:
a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)


print("-----------------------------------------------------------")

# Higher Dimensional Arrays
arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print('number of dimensions :', arr.ndim)


print("-----------------------------------------------------------")

# Araay Indexing
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[10, 20, 30], [40, 50, 60]]])

print(f"Index (0) : {arr[0]}")
print(f"Index (0, 0) : {arr[0, 0]}")
print(f"Index (0, 0, 0) : {arr[0, 0, 0]}")

print(arr[0] + arr[1])

print("-----------------------------------------------------------")

# Array Slicing
arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[1:5])
print(arr[4:])
print(arr[:4])
print(arr[-3:-1])

