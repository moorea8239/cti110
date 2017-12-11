# CTI-110
# M3T1 - Areas of Rectangle
# Andrew Moore
# 09/22

# Dimensions of rectangle 1
length1 = int(input("Enter length of rectangle 1: "))
width1 = int(input("Enter width of rectangle 1: "))

# Dimesnions of rectangle 2
length2 = int(input("Enter length of rectangle 2: "))
width2 = int(input("Enter lenght of rectangle 2: "))

# Calculate the areas of both rectangles
area1 = length1 * width1
area2 = length2 * width2

# Determine the greater area
if area1 > area2:
    print("Rectangle 1 has the greater area.")
elif area2 > area1:
        print("Rectangle 2 has the greater area.")
elif area1 == area2:
            print("The Rectangles have equal area.")
        
    
