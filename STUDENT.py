import pandas as pd

# Read CSV file
df = pd.read_csv("student_performance.csv")

print("Original Dataset:")
print(df)

# Find shape
print("\nOriginal Shape:", df.shape)

# Find missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Count total missing values
print("\nTotal Missing Values:", df.isnull().sum().sum())

# Find duplicate rows
print("\nDuplicate Rows:")
print(df[df.duplicated()])

# Count duplicates
print("\nTotal Duplicates:", df.duplicated().sum())

# Remove duplicates
df = df.drop_duplicates()

# Handle missing values
df["Maths"] = df["Maths"].fillna(df["Maths"].mean())
df["Science"] = df["Science"].fillna(df["Science"].mean())
df["English"] = df["English"].fillna(df["English"].mean())

# Check missing values after cleaning
print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

# Cleaned shape
print("\nCleaned Shape:", df.shape)

print("\nCleaned Dataset:")
print(df)