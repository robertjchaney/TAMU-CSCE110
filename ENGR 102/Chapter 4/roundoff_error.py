# By submitting this assignment, I agree to the following
#  "Aggies do not lie, cheat, or steal, or tolerate those who do."
#  "I have not given or received any unauthorized aid on this assignment."
#
# Name:  Robert Chaney, Colby Hudson, Cash Ostberg
# Section:  538
# Assignment:  Lab 4a
# Date:  9/3/24



############ Part A ############

a = 1 / 7 
print(f'a = {a}') 
b = a * 7 
print(f'b = a * 7 = {b}')

# Part A Question 1
# When rounding 'a' to less than 15 variables, the result of 'b' is not equal to 1.0, but if it is unrounded 'b' does return 1.0

c = 2 * a
d = 5 * a 
f = c + d 
print(f'f = 2 * a + 5 * a = {f}')

# Part A Question 2
# In theory 'f' should be equal to 1.0, but it does not return 1.0.

from math import sqrt

x = sqrt(1 / 3) 
print(f'x = {x}') 
y = x * x * 3 
print(f'y = x * x * 3 = {y}')
z = x * 3 * x 
print(f'z = x * 3 * x = {z}')

# Part A Question 3
# When doing math in python, python reads left to right on whatever level of PEMDAS it is at. In this case when x is calculated it is one third of the square 
# root of 'x', so when working backwards you would first multiply x by x to get x^2 and then multiply by 3 to get x back to its orginal value. 
# This is true for variable y, but not z 

############ Part B ############

TOL = 1e-10
# check if b and f are equal within specified tolerance
if abs(b - f) < TOL: 
    print(f'b and f are equal within tolerance of {TOL}')
else:
    print(f'b and f are NOT equal within tolerance of {TOL}')

if abs(y - z) < TOL: 
    print(f'y and z are equal within tolerance of {TOL}')
else:
    print(f'y and z are NOT equal within tolerance of {TOL}')


