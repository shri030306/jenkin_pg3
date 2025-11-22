import sys

if len(sys.argv) != 6:
    print("Usage: python studentgrade.py mark1 mark2 mark3 mark4 mark5")
    sys.exit(1)

marks1 = float(sys.argv[1])
marks2 = float(sys.argv[2])
marks3 = float(sys.argv[3])
marks4 = float(sys.argv[4])
marks5 = float(sys.argv[5])

avg = (marks1 + marks2 + marks3 + marks4 + marks5) / 5

if avg >= 85:
    grade = "A"
elif avg >= 70:
    grade = "B"
elif avg >= 55:
    grade = "C"
elif avg >= 40:
    grade = "D"
elif avg >= 30:
    grade = "E"
else:
    grade = "Fail"

print("\n--- Result ---")
print("Marks:", marks1, marks2, marks3, marks4, marks5)
print("Average Marks:", avg)
print("Grade:", grade)
