# By submitting this assignment, I agree to the following
#  "Aggies do not lie, cheat, or steal, or tolerate those who do."
#  "I have not given or received any unauthorized aid on this assignment."
#
# Name:  Robert Chaney
# Section:  538
# Assignment:  Lab 7b
# Date: 10/15/24

import math
entry = False
namesAndPasswords = {}

# Gathering usernames and passwords
numTimes = int(input("How many usernames/passwords are there?"))
for i in range(numTimes):
    username = input("What is a username: ")
    namesAndPasswords[username] = ""

for username in namesAndPasswords:
    password = input("What is the password: ")
    namesAndPasswords[username] = password

#print(namesAndPasswords)

while entry == False:
    tryUsername = input("Enter your username: ")
    tryPassword = input("Enter your password: ")

    if tryUsername in namesAndPasswords:
        if namesAndPasswords[tryUsername] == password and namesAndPasswords[username] == tryPassword:
            print("You are allowed into the system")
            entry = True
        else:
            print("Wrong Password, Try Again")
    else:
        print("Wrong Username, Try Again")

