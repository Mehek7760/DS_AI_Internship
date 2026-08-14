import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
data = sns.load_dataset("iris")

# 1. Basic Information
print("First 5 Rows:")
print(data.head())

print("\nShape:")
print(data.shape)

print("\nData Types:")
print(data.dtypes)

print("\nMissing Values:")
print(data.isnull().sum())

# 2. Statistical Summary
print("\nStatistical Summary:")
print(data.describe())

# 3. Univariate Analysis
print("\nMean:")
print(data.select_dtypes("number").mean())

print("\nMedian:")
print(data.select_dtypes("number").median())

print("\nSkewness:")
print(data.select_dtypes("number").skew())

# Visualization 1 - Histogram
data.hist(figsize=(10, 8))
plt.suptitle("Histogram of Numerical Variables")
plt.show()


# 4. Bivariate Analysis

# Visualization 2 - Scatter Plot
sns.scatterplot(
    data=data,
    x="sepal_length",
    y="petal_length",
    hue="species"
)

plt.title("Sepal Length vs Petal Length")
plt.xlabel("Sepal Length")
plt.ylabel("Petal Length")
plt.show()


# Visualization 3 - Bar Chart
sns.barplot(
    data=data,
    x="species",
    y="petal_length"
)

plt.title("Average Petal Length by Species")
plt.xlabel("Species")
plt.ylabel("Average Petal Length")
plt.show()


# 5. Correlation Analysis
print("\nCorrelation Matrix:")
print(data.select_dtypes("number").corr())

# Visualization 4 - Heatmap
sns.heatmap(
    data.select_dtypes("number").corr(),
    annot=True,
    cmap="coolwarm"
)

plt.title("Correlation Heatmap")
plt.show()


# 6. Outlier Detection

# Visualization 5 - Boxplot
plt.figure(figsize=(10, 6))

sns.boxplot(
    data=data.select_dtypes("number")
)

plt.title("Outlier Detection using Boxplot")
plt.show()


# 7. Categorical Analysis

print("\nSpecies Count:")
print(data["species"].value_counts())

# Visualization 6 - Count Plot
sns.countplot(
    data=data,
    x="species"
)

plt.title("Number of Flowers in Each Species")
plt.xlabel("Species")
plt.ylabel("Count")
plt.show()


# 8. Pattern Identification
print("\nPattern Identification:")
print("1. Petal length and petal width have a strong positive relationship.")
print("2. Different species have different petal measurements.")
print("3. Setosa is clearly different from the other two species.")
print("4. Some variables may contain outliers.")
print("5. The dataset contains no missing values.")


# 9. Conclusion
print("\nConclusion:")
print("The EDA shows important relationships between the numerical variables.")
print("Visualization helps identify distributions, relationships and outliers.")
print("Petal measurements are useful for distinguishing Iris species.")