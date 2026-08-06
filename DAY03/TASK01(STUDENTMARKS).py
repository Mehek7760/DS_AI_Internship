
name = input("Enter student name: ")

marks = []
count = 1


while True:
    mark = input(f"Enter Mark {count} (or type 'done' to finish): ")

    if mark.lower() == "done":
        break

    marks.append(int(mark))
    count += 1


if len(marks) > 0:
    average = sum(marks) / len(marks)

    
    if average >= 90:
        grade = "A+"
    elif average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 50:
        grade = "D"
    else:
        grade = "F"

    
    print("\nStudent Details")
    print("Name   :", name)
    print("Marks  :", marks)
    print("Average:", round(average, 2))
    print("Grade  :", grade)
else:
    print("No marks were entered.")