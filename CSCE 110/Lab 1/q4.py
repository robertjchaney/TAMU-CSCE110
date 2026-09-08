#File: q4.py
#Author: Robert Chaney
#Date: 09/04/2026
#Section: 500 (?)
#Email: robertjchaney@tamu.edu
#Description: e.g. This program asks the user for two prices, applies a discount,
#applies a sales tax, then presents the final total.

item1 = float(input("Enter the price of item 1: "))
item2 = float(input("Enter the price of item 2: "))
subtotal = (item1 + item2) * 0.6
print(subtotal)
finalTotal = subtotal + subtotal * 0.0825
print("Final total is $", finalTotal)