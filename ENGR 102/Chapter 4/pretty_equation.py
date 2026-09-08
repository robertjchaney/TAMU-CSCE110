# By submitting this assignment, I agree to the following
#  "Aggies do not lie, cheat, or steal, or tolerate those who do."
#  "I have not given or received any unauthorized aid on this assignment."
#
# Name:  Robert Chaney
# Section:  538
# Assignment:  Lab 4b
# Date:  9/12/24

import math

# Get number inputs
num1 = str(input("Please enter the coefficient A: "))
num2 = str(input("Please enter the coefficient B: "))
num3 = str(input("Please enter the coefficient C: "))
blank_string = ' '
check = 0


# Format strings
if num1 == '0':
    num1 = ''
elif num1 == '1':
    num1 = 'x^2'
elif num1 == "-1":
    num1 = '- x^2'
elif '-' in num1:
    num1 = num1[:1] + blank_string + num1[1:] + 'x^2'
else:
    num1 =  num1 + 'x^2'

check = 0

if num2 == '0':
    num2 = ''
    check = 1
elif num2 == '1':
    num2 = 'x'
    check = 1
elif num2 == "-1":
    num2 = '- x'
    check = 1
elif '-' in num2:
    num2 = num2[:1] + blank_string + num2[1:] + 'x'
    check = 1
if num1 != '' and check == 0:
    num2 = "+ " + num2 + 'x'
elif num1 == '' and check == 0:
    num2 = num2 + 'x'
elif num1 != '' and num2 == 'x':
    num2 = '+ ' + num2

check = 0

if num3 == '0':
    num3 = ''
    check = 1
elif num3 == '1':
    num3 = '+ 1'
    check = 1
elif num3 == "-1":
    num3 = '- 1'
    check = 1
elif '-' in num3:   
    num3 = num3[:1] + blank_string + num3[1:]
    check = 1
if num2 != '' and check == 0:
    num3 = "+ " + num3
elif num2 == '' and check == 0:
    num3 = num3

# print(num1)
# print(num2)
# print(num3)

if num1 == '':
    print(f'The quadratic equation is {num2} {num3} = 0')
elif num2 == '' and num3 == '':
    print(f'The quadratic equation is {num1} {num3}= 0')
elif num2 == '':
    print(f'The quadratic equation is {num1} {num3} = 0')
elif num3 == '':
    print(f'The quadratic equation is {num1} {num2} = 0')
else:
    print(f'The quadratic equation is {num1} {num2} {num3} = 0')

