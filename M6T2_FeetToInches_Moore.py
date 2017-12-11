#CTI 110
#M6T2_FeetToInches
#11/1
#MooreA

#Write a simple program to convert distance in feet to inches

def main():
    #have user input distance in feet
    feet = int(input("What is the number of feet?: "))
    feet_to_inches(feet)

def feet_to_inches(feet):
    #Calculate the distance in inches and display result
    inch = feet * 12

    #Display result
    print(feet, "feet equals", inch, "inches.")
    


main()
