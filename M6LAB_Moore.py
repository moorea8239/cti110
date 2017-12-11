#Andrew Moore
#M6LAB
#10/30

#Write a simple program to ask user name and age, greet them by name and tell
#age group (infant, child, teenager, or adult

def main():
    #Request user input name
    name = input("What is your name?: ")
    greet(name)
    #Request user input age
    age = float(input("What is your age?: "))
    print("Your age makes you", ageCategory(age))
#Display greeting with user's name
def greet(name):
    print("Hello,", name)

#Display user's age category
def ageCategory(age):
    #Identify age classifications
    infant = 1
    child = 13
    teenager = 19
    adult = 20
    answer = "unknown"    
    #Display results
    if age <= 1:
       answer = "an infant"
    elif age <= 13:
       answer = "a child"
    elif age <= 19:
       answer = "a teenager."
    elif age >= 20:
       answer = "an adult"
    return answer
                
    


    

main()
