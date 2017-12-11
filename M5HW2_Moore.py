#CTI 110
#M5HW2 - RUNNING TOTAL
#Andrew Moore
#11/26

"""Write program to add series of user entered numbers and keep a
running total until the user enters negative number"""

def main():

    numberEntered = int(input("Enter a number?  "))
    total = 0

    while numberEntered > 0:
        numberEntered = int(input("Enter a new number?  "))
        total = total + numberEntered
        
    print("Total:", total)   







main()
