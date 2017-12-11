#CTI 110
#M5HW1 - Distance Traveled
#10/29
#moorea

#Write a program that displays the distance traveled after the user inputs
#speed and number of hours.

def main():
    #have the user input speed of vehicle in mph
    
    milesPerHour = int(input("What is the speed of the vehicle in MPH?: "))

    #have the user input time traveled in hours

    hoursTraveled = int(input("How many hours has it traveled?: ")) + 1   

    distanceTraveled = milesPerHour * hoursTraveled

    for x in range(1, hoursTraveled):
        print(x * milesPerHour)
        
    







main()

