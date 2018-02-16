# CTI-110
# P2HW2 - Tip Tax Total
# Sabrina Koncaba
# 2/15/2018

print ("In this program you will calculate the total food bill by")
print ("calculating the amount of tax plus the tip and add this to")
print ("the bill to get the total amount owed to the fast food joint.\n")




print("Hello\n")
billAmount = float(input("Enter the amount of the bill: "))

salesTax = billAmount * .07
print("The total sales tax is: ")
print (format (salesTax, ".2f"))

tipAmount = billAmount * .18
print("The amount of the tip is: ")
print (format (tipAmount, ".2f"))

totalCost = billAmount + salesTax + tipAmount
print("The amount of the bill is: ")
print (format (totalCost, ".2f"))
      



