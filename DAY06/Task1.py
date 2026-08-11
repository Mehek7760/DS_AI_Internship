import numpy as np

sales = np.array([
    [100, 200, 150],
    [120, 180, 160],
    [90, 220, 140],
    [110, 190, 170]
])

print("Sales Data:")
print(sales)


print("\nProduct-wise:")
print("Mean:", np.mean(sales, axis=0))
print("Median:", np.median(sales, axis=0))
print("Variance:", np.var(sales, axis=0))
print("Standard Deviation:", np.std(sales, axis=0))


print("\nDay-wise:")
print("Mean:", np.mean(sales, axis=1))
print("Median:", np.median(sales, axis=1))
print("Variance:", np.var(sales, axis=1))
print("Standard Deviation:", np.std(sales, axis=1))