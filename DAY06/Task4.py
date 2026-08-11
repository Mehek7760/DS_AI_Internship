import pandas as pd

names = pd.Series(["Alice", "BOB", None, "Charlie", "DAVID", None])

print("Original Series:")
print(names)

print("\nMissing values:")
print(names.isnull())

names = names.fillna("Unknown")

print("\nAfter filling missing values:")
print(names)

names = names.str.lower()

print("\nNames in lowercase:")
print(names)

result = names[names.str.contains("a")]

print("\nNames containing 'a':")
print(result)