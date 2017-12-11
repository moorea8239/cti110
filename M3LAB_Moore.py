# CTI 110
# M3LAB
# A Moore
# 9/25

# This program takes a numeric grade and tranlates it to a letter grade.

# Grades based on 10-point scale
A_score = 90
B_score = 80
C_score = 70
D_score = 60

# ask the user for numeric grade
score = float(input("Type Numeric Grade Here: "))

if score >= A_score:
    print("Your grade is: A")
elif score >= B_score:
    print("Your grade is: B")
elif score >= C_score:
    print("Your grade is: C")
elif score >= D_score:
    print("Your grade is: D")
elif score < D_score:
    print("You have a failing grade")
