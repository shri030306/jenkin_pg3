marks1 = float(input("Enter marks of subject 1: "))
marks2 = float(input("Enter marks of subject 2: "))
marks3 = float(input("Enter marks of subject 3: "))
marks4 = float(input("Enter marks of subject 4: "))
marks5 = float(input("Enter marks of subject 5: "))

avg = (marks1 + marks2 + marks3) / 3

if avg >= 85:
    grade = "A"
elif avg >= 70:
    grade = "B"
elif avg >= 55:
    grade = "C"
elif avg >= 40:
    grade = "D"
else:
    grade = "Fail"

print("Average Marks:", avg)
print("Grade:", grade)
