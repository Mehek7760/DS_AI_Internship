import numpy as np

# Create two matrices
A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

# Matrix multiplication
matrix_result = np.dot(A, B)

# Element-wise multiplication
element_result = A * B

print("Matrix A:")
print(A)

print("\nMatrix B:")
print(B)

print("\nMatrix Multiplication using np.dot():")
print(matrix_result)

print("\nElement-wise Multiplication using *:")
print(element_result)

print("\nShape of Matrix Multiplication result:")
print(matrix_result.shape)

# Swap the matrices
swap_result = np.dot(B, A)

print("\nAfter swapping A and B:")
print(swap_result)

print("\nShape after swapping:")
print(swap_result.shape)