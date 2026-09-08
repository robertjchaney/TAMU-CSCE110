# By submitting this assignment, I agree to the following
#  "Aggies do not lie, cheat, or steal, or tolerate those who do."
#  "I have not given or received any unauthorized aid on this assignment."
#
# Name:  Robert Chaney
# Section:  538
# Assignment:  10b
# Date: 11/04/24

import numpy as np
import matplotlib.pyplot as plt

# Define the initial point and matrix
point = np.array([0, 1])
matrix = np.array([[1.01, 0.09], [-0.09, 1.01]])
x_values = []
y_values = []

# Perform the matrix multiplication 200 times
for time in range(200):
    x_values.append(point[0])
    y_values.append(point[1])
    
    point = matrix @ point

# Plot the results
plt.figure(figsize=(8, 8))
plt.plot(x_values, y_values, marker='^', markersize=3, linestyle='-', color='gold')
plt.xlabel('X values')
plt.ylabel('Y values')
plt.title('Plot of points after repeated matrix multiplication (Da Vinci Spiral)')
plt.show()
