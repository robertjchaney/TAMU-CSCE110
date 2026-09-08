# By submitting this assignment, I agree to the following
#  "Aggies do not lie, cheat, or steal, or tolerate those who do."
#  "I have not given or received any unauthorized aid on this assignment."
#
# Name:  Robert Chaney
# Section:  538
# Assignment:  9b
# Date: 10/23/24

import math 
import random

notNum = False
correctNum = random.randint(1,100) # Selects correct number between 1 and 100 (inclusive)
counter = 0

def getGuess():
    while True:
        try:
            guess = float(input("What is your guess? "))
            return guess  # Return the valid guess if no error occurs
        except ValueError:
            print("Bad input! Try Again:")

def isNumber(num):  # Checks user input against actual number
    global counter
    if num > correctNum:
        print("Too high!")
        counter += 1
    elif num < correctNum:
        print("Too low!")
        counter += 1
    elif num == correctNum:
        print(f"You guessed it! It took you {counter} guesses.")
        return True
    return False

print("Guess the secret number! Hint: it’s an integer between 1 and 100...")
while not notNum:
    guess = getGuess()
    notNum = isNumber(guess)