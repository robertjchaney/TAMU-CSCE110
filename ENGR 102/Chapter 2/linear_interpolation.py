# By submitting this assignment, I agree to the following
#  "Aggies do not lie, cheat, or steal, or tolerate those who do."
#  "I have not given or received any unauthorized aid on this assignment."
#
# Name:  Robert Chaney, Colby Hudson, Cash Ostberg
# Section:  538
# Assignment:  Lab 2a
# Date:  08/29/2024

# After conferring in class, we unified our code and made it uniform before we turned it in

import math


#Notes:
# at time = 10 minutes distance = 2028 kilometers    
# at time = 55 mintues distance  = 23028 kilometers
# equation: y = (slope)(x - x1) + y1


# Given linear interpolation variables
x1 = 10
x2 = 55


y1 = 2028
y2 = 23028


# Determining distance at time = test_time = 25 minutes
test_time = 25
test_distance = ((y2 - y1) / (x2 - x1)) * (test_time - x1) + y1


print('Part 1:')
print(f'For t = {test_time} minutes, the position p = {test_distance} kilometers')


# Determining distance at time = 300 minutes
test_time = 300
test_distance = ((y2 - y1) / (x2 - x1)) * (test_time - x1) + y1     # total distance traveled
circumfrence = 2 * math.pi * 6745                                   # circumfrence of ISS path
test_distance = test_distance % circumfrence                        # distance from Houston at time = 300 minutes


print('Part 2:')
print(f'For t = {test_time} minutes, the position p = {test_distance} kilometers')

