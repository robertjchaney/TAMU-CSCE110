#File: q1.py
#Author: Robert Chaney
#Date: 09/04/2026
#Section: 500 (?)
#Email: robertjchaney@tamu.edu
#Description: e.g. This program asks the user their first and last name and
#age, then returns the user's age in 4 years

print("Enter first name:", end=" ")
first = input()
print("Enter last name:", end=" ")
last = input()
print("Enter age:", end=" ")
agePlusFour = int(input()) + 4
print()
print("Howdy!", first, last + "! You will be", agePlusFour, "in 4 years.")