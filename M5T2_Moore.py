#Andrew Moore
#M5T2 - Bug Collector
#10/16

# Write a simple program to calculate running total of bugs collected

def main():
    totalBugs = 0
    #Range is 1 week, 7 days
    week = range(1,8)
    for day in week:
        print ("day", day)
        bugsPerDay = int(input("Enter bugs collected today: "))
        # Add running total of bugs
        totalBugs = totalBugs + bugsPerDay
        print("Bugs collected today is:", bugsPerDay)
        
        # Display total of bugs collected
        
    print("The number of bugs collected this week is,", totalBugs, "Bugs")
    
    
    
main()
