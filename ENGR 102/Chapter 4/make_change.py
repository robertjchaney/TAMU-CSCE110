# By submitting this assignment, I agree to the following
#  "Aggies do not lie, cheat, or steal, or tolerate those who do."
#  "I have not given or received any unauthorized aid on this assignment."
#
# Name:  Robert Chaney, Colby Hudson, Cash Ostberg
# Section:  538
# Assignment:  Lab 4a
# Date:  9/3/24


paid = float(input("How much did you pay? "))
cost = float(input("How much did it cost? "))
paid *= 100
cost *= 100

change = paid - cost 
print(f'You received ${change / 100:.2f} in change. That is...')

# Genisis of variables
quarters = 0
dimes = 0
nickels = 0
pennies = 0


# Get number of coins
while change >= 0:
    if change >= 25:       
        quarters = change // 25
        change -= quarters * 25

    if change >= 10:
        dimes = change // 10
        change -= dimes * 10

    if change >= 5:
        nickels = change // 5
        change -= nickels * 5


    if change >= 1:
        pennies = change
        change -= pennies * 1


    if change < 1:
        break

# Print exact change
if quarters == 0:
    pass
elif quarters == 1:
    print(f'{int(quarters)} quarter') 
elif quarters > 1:
    print(f'{int(quarters)} quarters') 

if dimes == 0:
    pass
elif dimes == 1:
    print(f'{int(dimes)} dime') 
elif dimes > 1:
    print(f'{int(dimes)} dimes') 

if nickels == 0:
    pass
elif nickels == 1:
    print(f'{int(nickels)} nickel') 
elif nickels > 1:
    print(f'{int(quarters)} nickels') 

if pennies == 0:
    pass
elif pennies == 1:
    print(f'{int(pennies)} penny') 
elif pennies > 1:
    print(f'{int(pennies)} pennies') 
