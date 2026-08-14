import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from io import StringIO

# ============================================================
# DATASET
# ============================================================

data = """PassengerId,Survived,Pclass,Name,Sex,Age,SibSp,Parch,Fare,Embarked
1,0,3,Braund Owen,male,22,1,0,7.25,S
2,1,1,Cumings Mrs John,female,38,1,0,71.28,C
3,1,3,Heikkinen Laina,female,26,0,0,7.93,S
4,1,1,Futrelle Mrs Jacques,female,35,1,0,53.10,S
5,0,3,Allen William,male,35,0,0,8.05,S
6,0,3,Moran James,male,28,0,0,8.46,Q
7,0,1,McCarthy Timothy,male,54,0,0,51.86,S
8,0,3,Palsson Gosta,male,2,3,1,21.08,S
9,1,3,Johnson Mrs Oscar,female,27,0,2,11.13,S
10,1,2,Nasser Mrs Nicholas,female,14,1,0,30.07,C
11,1,3,Sandstrom Marguerite,female,4,1,1,16.70,S
12,1,1,Bonnell Elizabeth,female,58,0,0,26.55,S
13,0,3,Saul Nicholas,male,20,0,0,8.05,S
14,0,3,Andersson Ingeborg,female,39,1,5,31.28,S
15,0,3,Vestrom Hulda,female,14,0,0,7.85,S
16,1,2,Hewlett Mrs George,female,55,0,0,16.00,S
17,0,3,Rice Eugene,male,2,4,1,29.13,Q
18,1,2,Williams Charles,male,30,0,0,13.00,S
19,0,3,Vander Julius,female,31,1,0,18.00,S
20,1,3,Masselmani Hussein,female,22,0,0,7.23,C
21,0,2,Fynney Joseph,male,35,0,0,26.00,S
22,1,2,Beesley Lawrence,male,34,0,0,13.00,S
23,1,3,McGough James,male,15,0,0,8.03,Q
24,1,1,Chaffee Herbert,female,28,1,0,35.50,S
25,0,3,Peters Katie,female,8,3,1,21.08,S
26,1,3,Asplund Carl,female,38,1,5,31.39,S
27,0,3,Emir Anthony,male,18,0,0,7.23,C
28,0,1,Fortune Charles,male,19,3,2,263.00,S
29,1,3,ODwyer Ellen,female,28,0,0,7.88,Q
30,0,3,Todoroff Lalio,male,28,0,0,7.90,S
31,0,1,Uruchurtu Manuel,male,40,0,0,27.72,C
32,1,1,Graham Margaret,female,29,1,0,146.52,C
33,1,3,Harrison Henry,female,18,0,0,7.75,Q
34,0,2,Williams Charles,male,66,0,0,10.50,S
35,0,1,Lurette Joseph,male,28,1,0,82.17,C
36,0,1,Harper John,male,45,1,0,52.55,S
37,1,3,Wells Arthur,female,22,0,0,7.23,C
38,0,3,Holverson Alexander,male,21,0,0,8.05,S
39,0,3,Vander Julius,female,18,2,0,18.00,S
40,1,2,West Edvard,female,14,1,0,26.00,S
41,0,3,Hawksford Walter,male,40,0,0,7.90,S
42,0,1,Giglio Victor,male,28,0,0,13.00,S
43,0,3,Rydberg Alfred,male,20,0,0,7.85,S
44,1,2,Isham Ann,female,24,1,0,26.00,S
45,1,3,Devaney Margaret,female,19,0,0,7.88,Q
46,0,3,Rogers John,male,29,0,0,8.05,S
47,0,3,Andersson Ebba,female,21,0,0,9.83,S
48,1,3,Goodwin Lillian,female,16,1,0,7.65,S
49,0,3,Sage Constance,female,30,2,0,20.53,S
50,1,1,Ward Anna,female,35,0,0,227.53,C"""

# Convert the given data directly into a DataFrame
df = pd.read_csv(StringIO(data))


# ============================================================
# EXPLORATORY DATA ANALYSIS - TITANIC DATASET
# ============================================================

print("=" * 60)
print("EXPLORATORY DATA ANALYSIS - TITANIC DATASET")
print("=" * 60)


# ============================================================
# 1. FIRST 5 ROWS
# ============================================================

print("\n1. FIRST 5 ROWS")
print(df.head())


# ============================================================
# 2. LAST 5 ROWS
# ============================================================

print("\n2. LAST 5 ROWS")
print(df.tail())


# ============================================================
# 3. SHAPE OF DATASET
# ============================================================

print("\n3. SHAPE OF DATASET")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])


# ============================================================
# 4. COLUMN NAMES
# ============================================================

print("\n4. COLUMN NAMES")
print(df.columns.tolist())


# ============================================================
# 5. DATA TYPES
# ============================================================

print("\n5. DATA TYPES")
print(df.dtypes)


# ============================================================
# 6. DATASET INFORMATION
# ============================================================

print("\n6. DATASET INFORMATION")
df.info()


# ============================================================
# 7. STATISTICAL SUMMARY
# ============================================================

print("\n7. STATISTICAL SUMMARY")
print(df.describe())


# ============================================================
# 8. MISSING VALUES
# ============================================================

print("\n8. MISSING VALUES")
print(df.isnull().sum())

print("\nMISSING VALUE PERCENTAGE")
print((df.isnull().sum() / len(df)) * 100)


# ============================================================
# 9. DUPLICATE ROWS
# ============================================================

print("\n9. DUPLICATE ROWS")
print("Number of duplicate rows:", df.duplicated().sum())

df = df.drop_duplicates()

print("Shape after removing duplicates:", df.shape)


# ============================================================
# 10. DATA CLEANING
# ============================================================

if df["Age"].isnull().sum() > 0:
    df["Age"] = df["Age"].fillna(df["Age"].median())

if df["Embarked"].isnull().sum() > 0:
    df["Embarked"] = df["Embarked"].fillna(
        df["Embarked"].mode()[0]
    )

print("\n10. MISSING VALUES AFTER CLEANING")
print(df.isnull().sum())


# ============================================================
# NUMERICAL COLUMNS
# ============================================================

numerical_columns = [
    "Age",
    "Fare",
    "SibSp",
    "Parch"
]


# ============================================================
# NUMERICAL SUMMARY
# ============================================================

print("\nNUMERICAL SUMMARY")
print(df[numerical_columns].describe())


# ============================================================
# GENDER DISTRIBUTION
# ============================================================

print("\nGENDER DISTRIBUTION")
print(df["Sex"].value_counts())


# ============================================================
# PASSENGER CLASS DISTRIBUTION
# ============================================================

print("\nPASSENGER CLASS DISTRIBUTION")
print(df["Pclass"].value_counts())


# ============================================================
# SURVIVAL DISTRIBUTION
# ============================================================

print("\nSURVIVAL DISTRIBUTION")
print(df["Survived"].value_counts())


# ============================================================
# EMBARKED DISTRIBUTION
# ============================================================

print("\nEMBARKED DISTRIBUTION")
print(df["Embarked"].value_counts())


# ============================================================
# 11. UNIVARIATE ANALYSIS - NUMERICAL
# ============================================================

for column in numerical_columns:

    plt.figure(figsize=(7, 5))

    plt.hist(
        df[column],
        bins=10,
        edgecolor="black"
    )

    plt.title("Distribution of " + column)
    plt.xlabel(column)
    plt.ylabel("Frequency")

    plt.show()


# ============================================================
# 12. UNIVARIATE ANALYSIS - CATEGORICAL
# ============================================================

categorical_columns = [
    "Sex",
    "Pclass",
    "Survived",
    "Embarked"
]

for column in categorical_columns:

    plt.figure(figsize=(7, 5))

    sns.countplot(
        data=df,
        x=column
    )

    plt.title("Count Plot of " + column)
    plt.xlabel(column)
    plt.ylabel("Count")

    plt.show()


# ============================================================
# 13. BOX PLOTS
# ============================================================

for column in numerical_columns:

    plt.figure(figsize=(7, 5))

    sns.boxplot(
        y=df[column]
    )

    plt.title("Box Plot of " + column)
    plt.ylabel(column)

    plt.show()


# ============================================================
# 14. BIVARIATE ANALYSIS
# ============================================================

print("\nSURVIVAL BY GENDER")
print(
    pd.crosstab(
        df["Sex"],
        df["Survived"]
    )
)


print("\nSURVIVAL BY PASSENGER CLASS")
print(
    pd.crosstab(
        df["Pclass"],
        df["Survived"]
    )
)


print("\nSURVIVAL BY EMBARKED PORT")
print(
    pd.crosstab(
        df["Embarked"],
        df["Survived"]
    )
)


# ============================================================
# 15. SURVIVAL RATE BY GENDER
# ============================================================

plt.figure(figsize=(7, 5))

sns.barplot(
    data=df,
    x="Sex",
    y="Survived"
)

plt.title("Survival Rate by Gender")
plt.xlabel("Gender")
plt.ylabel("Average Survival Rate")

plt.show()


# ============================================================
# 16. SURVIVAL RATE BY PASSENGER CLASS
# ============================================================

plt.figure(figsize=(7, 5))

sns.barplot(
    data=df,
    x="Pclass",
    y="Survived"
)

plt.title("Survival Rate by Passenger Class")
plt.xlabel("Passenger Class")
plt.ylabel("Average Survival Rate")

plt.show()


# ============================================================
# 17. SURVIVAL RATE BY EMBARKATION PORT
# ============================================================

plt.figure(figsize=(7, 5))

sns.barplot(
    data=df,
    x="Embarked",
    y="Survived"
)

plt.title("Survival Rate by Embarkation Port")
plt.xlabel("Embarked")
plt.ylabel("Average Survival Rate")

plt.show()


# ============================================================
# 18. AGE VS FARE
# ============================================================

plt.figure(figsize=(8, 5))

sns.scatterplot(
    data=df,
    x="Age",
    y="Fare",
    hue="Survived"
)

plt.title("Age vs Fare")
plt.xlabel("Age")
plt.ylabel("Fare")

plt.show()


# ============================================================
# 19. AGE VS SURVIVAL
# ============================================================

plt.figure(figsize=(8, 5))

sns.scatterplot(
    data=df,
    x="Age",
    y="Survived"
)

plt.title("Age vs Survival")
plt.xlabel("Age")
plt.ylabel("Survived")

plt.show()


# ============================================================
# 20. FARE BY PASSENGER CLASS
# ============================================================

plt.figure(figsize=(8, 5))

sns.boxplot(
    data=df,
    x="Pclass",
    y="Fare"
)

plt.title("Fare Distribution by Passenger Class")
plt.xlabel("Passenger Class")
plt.ylabel("Fare")

plt.show()


# ============================================================
# 21. AGE BY SURVIVAL
# ============================================================

plt.figure(figsize=(8, 5))

sns.boxplot(
    data=df,
    x="Survived",
    y="Age"
)

plt.title("Age Distribution by Survival")
plt.xlabel("Survived")
plt.ylabel("Age")

plt.show()


# ============================================================
# 22. SKEWNESS ANALYSIS
# ============================================================

print("\nSKEWNESS ANALYSIS")

for column in numerical_columns:

    skew_value = df[column].skew()

    print(
        f"{column} skewness: {skew_value:.3f}"
    )

    if skew_value > 1:

        print("Highly positively skewed")

    elif skew_value > 0.5:

        print("Moderately positively skewed")

    elif skew_value < -1:

        print("Highly negatively skewed")

    elif skew_value < -0.5:

        print("Moderately negatively skewed")

    else:

        print("Approximately symmetric")


# ============================================================
# 23. CORRELATION ANALYSIS
# ============================================================

print("\nCORRELATION MATRIX")

correlation = df[
    numerical_columns + ["Survived", "Pclass"]
].corr()

print(correlation)


# ============================================================
# 24. CORRELATION HEATMAP
# ============================================================

plt.figure(figsize=(10, 7))

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)

plt.title("Correlation Heatmap")

plt.show()


# ============================================================
# 25. OUTLIER DETECTION USING IQR
# ============================================================

print("\nOUTLIER DETECTION")

for column in numerical_columns:

    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)

    IQR = Q3 - Q1

    lower_limit = Q1 - 1.5 * IQR
    upper_limit = Q3 + 1.5 * IQR

    outliers = df[
        (df[column] < lower_limit) |
        (df[column] > upper_limit)
    ]

    print("\nColumn:", column)
    print("Q1:", Q1)
    print("Q3:", Q3)
    print("IQR:", IQR)
    print("Lower Limit:", lower_limit)
    print("Upper Limit:", upper_limit)
    print("Number of Outliers:", len(outliers))


# ============================================================
# 26. OUTLIER VISUALIZATION
# ============================================================

for column in numerical_columns:

    plt.figure(figsize=(7, 5))

    sns.boxplot(
        y=df[column]
    )

    plt.title("Outlier Detection - " + column)
    plt.ylabel(column)

    plt.show()


# ============================================================
# 27. OVERALL SURVIVAL RATE
# ============================================================

survival_rate = df["Survived"].mean() * 100

print("\nOVERALL SURVIVAL RATE")
print(f"{survival_rate:.2f}%")


# ============================================================
# 28. SURVIVAL RATE BY GENDER
# ============================================================

gender_survival = (
    df.groupby("Sex")["Survived"].mean() * 100
)

print("\nSURVIVAL RATE BY GENDER")
print(gender_survival)


# ============================================================
# 29. SURVIVAL RATE BY CLASS
# ============================================================

class_survival = (
    df.groupby("Pclass")["Survived"].mean() * 100
)

print("\nSURVIVAL RATE BY PASSENGER CLASS")
print(class_survival)


# ============================================================
# 30. PATTERN IDENTIFICATION
# ============================================================

print("\nPATTERN IDENTIFICATION")

print("""
1. Gender has an important relationship with survival.

2. Passenger class shows a noticeable relationship with survival.

3. Higher fare values are generally associated with higher
   passenger classes.

4. Fare contains extreme values.

5. Age has a weaker relationship with survival.

6. Fare is generally right-skewed.

7. Gender and passenger class are important patterns
   in the dataset.
""")


# ============================================================
# 31. FINAL INSIGHTS
# ============================================================

print("\nFINAL INSIGHTS")

print("""
The Titanic dataset contains both numerical and categorical
variables.

Missing values and duplicate records were checked and handled.

Univariate analysis showed the distribution of the variables.

Bivariate analysis showed relationships between survival and
other variables.

Female passengers generally had a higher survival rate than
male passengers.

Higher-class passengers generally had better survival outcomes.

Fare contained noticeable outliers and showed positive skewness.

Correlation analysis helped identify relationships between
numerical variables.
""")


# ============================================================
# 32. CONCLUSION
# ============================================================

print("\nCONCLUSION")

print("""
The EDA of the Titanic dataset revealed important patterns
in passenger survival.

Gender and passenger class showed strong relationships with
survival.

Fare had outliers and a right-skewed distribution.

Visualizations, correlation analysis, skewness analysis,
and outlier detection provided a better understanding of
the dataset.

Overall, EDA helped identify trends, relationships,
distributions, and unusual observations in the Titanic
dataset.
""")


print("\n" + "=" * 60)
print("EDA COMPLETED SUCCESSFULLY!")
print("=" * 60)