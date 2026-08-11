import numpy as np

A = np.array([[1, 2],
              [3, 4]])

B = np.linalg.det(A)

print("Matrix A:")
print(A)

print("Determinant of Matrix A:")
print(B)