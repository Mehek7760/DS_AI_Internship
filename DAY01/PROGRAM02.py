# Python program to verify age

age = int(input("Enter your age: "))

if age >= 18:
    print("You are an adult and eligible.")
elif age > 0:
    print("You are a minor.")
else:
    print("Invalid age entered.")
