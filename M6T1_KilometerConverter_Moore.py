#Andrew Moore
#M6T1 - Kilometer Converter
#10/25

#Write a simple program to convert kilometers to miles

CONVERSION_FACTOR = 0.6214

def main():
#Main function gets user input of distance in kilometers
    #Prompt for distance in kilometers
    km = float(input("Enter a distance in kilometers: "))
    show_miles(km)

def show_miles(km):
#The show_miles function converts kilometers to miles and displays result
    #Calculate miles
    miles = km * CONVERSION_FACTOR

    #Display result
    print(km, "kilometers equals", miles, "miles.")


main()
