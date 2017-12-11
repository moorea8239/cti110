# CTI-110
# M2HW2 - Tip, Tax, and Total
# Andrew Moore
# 09/12

# Calculate the amount of tip and sales tax

print ("Input charge for food")


foodCost = float(input("Amount: "))

# multiply by amount of tip
tipAmount = foodCost * 0.18

print ("total tip is", tipAmount)

# multiply by amount of tax
salesTax = foodCost * .07

print ("total tax is", salesTax)

# add cost of food, tax and tip for total cost
totalCost = foodCost + tipAmount + salesTax

print ("total cost is", totalCost)











               

