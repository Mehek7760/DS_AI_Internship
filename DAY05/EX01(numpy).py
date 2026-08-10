import numpy as np

sales = np.array([
    120, 250, 180, 300,
    150, 220, 175, 280,
    190, 350, 210, 275
])

print("Sales:", sales)
print("Shape:", sales.shape)
sales_3x4 = sales.reshape(3, 4)

print(sales_3x4)
print("New Shape:", sales_3x4.shape)
sales_4x3 = sales.reshape(4, 3)

print(sales_4x3)
flat_sales = sales.flatten()

print(flat_sales)
print("Shape:", flat_sales.shape)
np.transpose(sales)

import numpy as np

student1 = np.array([80, 75, 90])
student2 = np.array([85, 88, 78])

result = np.vstack((student1, student2))
result = np.concatenate((student1,student2))

print(result)