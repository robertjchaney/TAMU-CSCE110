# By submitting this assignment, I agree to the following
#  "Aggies do not lie, cheat, or steal, or tolerate those who do."
#  "I have not given or received any unauthorized aid on this assignment."
#
# Name:  Robert Chaney
# Section:  538
# Assignment:  Lab 6a
# Date: 9/21/24

import math

side_length = float(input('Enter the side length in meters: '))
num_layers = int(input('Enter the number of layers: '))
total_vis_triangles = 0
total_vis_squares = 0
total_area = 0


for i in range(num_layers):
    # # layer 1
    # total_vis_triangles += 2 * 0 + 1 # 1
    # # layer 2
    # total_vis_triangles += 2 * 1 + 1 # 4
    # # layer 3 
    # total_vis_triangles += 2 * 2 + 1 # 9

    # total_vis_triangles += 2 * 3 + 1 # 14

    #total_vis_triangles += 2 * 4 + 1 # 25
    total_vis_triangles += 2 * i + 1 
    total_vis_squares += 3 * (i + 1)

total_area += total_vis_squares * (side_length ** 2)
total_area += total_vis_triangles * ((math.sqrt(3) * (side_length**2)) / 4)

print(f'You need {total_area:.2f} m^2 of gold foil to cover the pyramid')