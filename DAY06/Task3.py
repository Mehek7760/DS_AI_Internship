import pandas as pd

marks = pd.Series(
    [75, 55, 82, 45, 68],
    index=["Maths", "Science", "English", "Social", "Computer"]
)


print("Student Marks:")
print(marks)


print("\nUsing positions:")
print("First mark:", marks.iloc[0])
print("Third mark:", marks.iloc[2])


print("\nUsing labels:")
print("Maths:", marks["Maths"])
print("English:", marks["English"])


print("\nValues:")
print(marks.values)


print("\nIndex:")
print(marks.index)

print("\nMarks above 60:")
print(marks[marks > 60])