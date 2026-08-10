import numpy as np

arr = np.array([[1, 2, 3],[1,4,5]])

new_arr = arr.reshape(3,2)

print("Original array:")
print(arr)

print("Reshaped array:")
print(new_arr)