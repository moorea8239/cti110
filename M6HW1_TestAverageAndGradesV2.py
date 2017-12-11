#M6HW1 - Test Average and Grade
#11/06
#CTI - 110
#Andrew Moore

"""A program to take user input test scores and display letter grade
for each score then the average test score."""


def main():
#Main function to have user input test scores
    #Prompt for numeric grade
    """numGrade1 = float(input("Enter the numeric grade for test 1:  "))
    numGrade2 = float(input("Enter the numeric grade for test 2:  "))
    numGrade3 = float(input("Enter the numeric grade for test 3:  "))
    numGrade4 = float(input("Enter the numeric grade for test 4:  "))
    numGrade5 = float(input("Enter the numeric grade for test 5:  "))
    grades = numGrade1 + numGrade2 + numGrade3 + numGrade4 + numGrade5"""


    grades = 0
    for i in range(1,6):
        numGrade = float(input("Enter the numeric grade for test" + str (i)+": "))
        grades += numGrade
        print(determine_grade(grades))
    calc_average(grades)

#Calculate and display average of test scores
def calc_average(grades):
    averageGrade = grades / 5

    print("The average of the entered scores is", averageGrade)
#Calculate the letter grade
def determine_grade(grades):
    if grades <= 59:
        print("Your grade is failing.")
    elif grades <= 69:
        print("Your grade is a D.")
    elif grades <= 79:
        print("Your grade is a C.")
    elif grades <= 89:
        print("Your grade is a B.")
    elif grades <= 100:
        print("Your grade is an A.")
#Determine the letter grade of each test score

main()
    
