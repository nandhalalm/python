marks=float(input("enter your grade"))
if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B+"
elif marks >= 60:
    grade = "B"
elif marks >= 50:
    grade = "C+"
elif marks >= 40:
    grade = "C"
else:
    grade = "Fail"

print("your grade is:",grade)