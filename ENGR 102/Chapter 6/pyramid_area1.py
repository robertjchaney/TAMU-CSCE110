# By submitting this assignment, I agree to the following
#  "Aggies do not lie, cheat, or steal, or tolerate those who do."
#  "I have not given or received any unauthorized aid on this assignment."
#
# Name:  Robert Chaney
# Section:  538
# Assignment:  Lab 6
# Date: 9/21/24

import math


# genesis or variables
side_length = float(input('Enter the side length in meters: '))
num_layers = int(input('Enter the number of layers: '))
total_cubes = num_layers**2
surfaces = 0
total_area = 0



# number of surfaces
for i in range(num_layers):
    # if i == 0:
    #     surfaces += 5
    # elif i == 1:
    #     surfaces += 11
    # elif i == 2:
    #     surfaces += 17
    # elif i == 3:
    #     surfaces += 23
    # elif i == 4:
    #     surfaces += 29
    surfaces += (i + 1) * 6 - 1
    

total_area = surfaces * (side_length**2)



print(f'You need {total_area:.2f} m^2 of gold foil to cover the pyramid')
