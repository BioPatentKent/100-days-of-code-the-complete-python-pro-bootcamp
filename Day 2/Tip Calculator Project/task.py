"""
Title: Tip Calculator
Author: BioPatentKent
Date: 2025-06-02
Description: This program calculates the tip amount.
"""

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
BillWithTip = bill + (bill * tip/100)
CostPerPerson = BillWithTip / people
CostPerPersonRound = round(CostPerPerson, 2)
print("Each person should pay: " + "$" + str(CostPerPersonRound))
