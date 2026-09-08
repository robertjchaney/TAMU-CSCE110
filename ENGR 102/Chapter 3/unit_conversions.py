# By submitting this assignment, I agree to the following
#  "Aggies do not lie, cheat, or steal, or tolerate those who do."
#  "I have not given or received any unauthorized aid on this assignment."
#
# Name:  Robert Chaney, Colby Hudson, Cash Ostberg
# Section:  538
# Assignment:  Lab 3a
# Date:  9/3/2024


import math

# Getting user input
x = float(input("Please enter the quantity to be converted: "))

# Defining fuctions
def lbs_to_N(lbs):
    print(f'{lbs:.2f} pounds force is equivalent to {lbs * 4.44822:.2f} newtons')

def m_to_ft(meters):
    print(f'{meters:.2f} meters is equivalent to {meters * 3.28084:.2f} feet')     
    
def atm_to_kPa(atm):
    print(f'{atm:.2f} atmospheres is equivalent to {atm * 101.325:.2f} kilopascals')

def W_to_BTU(W):
    print(f'{W:.2f} watts is equivalent to {W * 3.41214163:.2f} BTU per hour')

def LPS_to_GPM(liters):
    print(f'{liters:.2f} liters per second is equivalent to {liters * 15.850331:.2f} US gallons per minute')
    
def C_to_F(Celcius):  
    print(f'{Celcius:.2f} degrees Celsius is equivalent to {(Celcius * 9/5) + 32:.2f} degrees Fahrenheit')

# Calling Functions
lbs_to_N(x)
m_to_ft(x)
atm_to_kPa(x)
W_to_BTU(x)
LPS_to_GPM(x)
C_to_F(x)
