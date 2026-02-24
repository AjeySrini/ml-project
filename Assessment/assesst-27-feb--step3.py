name = input("Enter student name: ")

eng = float(input("Enter marks for Subject 1 (0-100): "))
phy = float(input("Enter marks for Subject 2 (0-100): "))
mat = float(input("Enter marks for Subject 3 (0-100): "))

total = eng + phy + mat

percentage = (total / 300) * 100

if percentage >= 75:
    grade = "A"
elif percentage >= 60:
    grade = "B"
elif percentage >= 40:
    grade = "C"
else:
    grade = "F"

print("\nStudent Name:", name)
print("Total:", total, "/300")
print("Percentage:", percentage, "%")
print("Grade:", grade)