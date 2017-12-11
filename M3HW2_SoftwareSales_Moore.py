# CTI-110
# M3HW2 - Software Sales
# Andrew Moore
# 09/25

# Simple program to calculate the cost of purchases made factoring discounts

softwarePackage = 99

# Ask user to enter number of packages purchased

packagesPurchased = int(input("Enter number of packages purchased: "))

# Calculate cost before discount
costBeforeDiscount = softwarePackage * packagesPurchased
print ("The total cost before dicounts is," , costBeforeDiscount )
# Determine applicable discount
if packagesPurchased >= 100:
    print ("Your total including 40 percent discount is,", costBeforeDiscount * .6)
elif packagesPurchased >= 50:
    print ("Your total including 30 percent discount is,", costBeforeDiscount * .7)
elif packagesPurchased >= 20:
    print ("Your total including 20 percent discount is,", costBeforeDiscount * .8)
elif packagesPurchased >= 10:
    print ("Your total including 10 percent discount is,", costBeforeDiscount * .9)
elif packagesPurchased < 10:
    print ("You must purchase at least 10 packages to receive an additional discount.")
