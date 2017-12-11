# CTI-110
# M3HW1 - Age Classifier
# Andrew Moore
# 9/25

# A simple program to classify age sets


# Identify age classifications
infant = 1
child = 13
teenager = 19
adult = 20

# Have user input numeric age
age = float(input("Enter age in year: "))
if age <= 1:
        print("This age makes you an infant.")
elif age <= 13:
            print("This age makes you a child.")
elif age <= 19:
                print("This age makes you a teenager.")
elif age >= 20:
                    print("This age makes you an adult.")
        
    
