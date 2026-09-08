# By submitting this assignment, I agree to the following
#  "Aggies do not lie, cheat, or steal, or tolerate those who do."
#  "I have not given or received any unauthorized aid on this assignment."
#
# Name:  Robert Chaney
# Section:  538
# Assignment:  Lab 2
# Date:  08/29/2024

import math 
import numpy
from decimal import *

# Reynolds Number
print("This program calculates the Reynolds number given velocity, length, and viscosity")
velocity = float(input("Please enter the velocity (m/s): "))
lin_dim = float(input("Please enter the length (m): "))
kin_visc = float(input("Please enter the viscosity (m^2/s): "))
Reynold = Decimal(velocity) * Decimal(lin_dim) / Decimal(kin_visc)
print(f"Reynolds number is {Reynold:.0f}")

print()

# Bragg's Law
print("This program calculates the wavelength given distance and angle")
distance = float(input("Please enter the distance (nm): "))
theta = float(input("Please enter the angle (degrees): "))
radTheta = math.radians(theta)
Bragg = 2 * distance * math.sin(radTheta)
print(f"Wavelength is {Bragg:.4f} nm")

print()

# Arps equation
print("This program calculates the production rate given time, initial rate, and decline rate")
time = float(input("Please enter the time (days): "))
init_prod = float(input("Please enter the initial rate (barrels/day): "))
init_dec = float(input("Please enter the decline rate (1/day): "))
hyp_const = 0.8
Arp = init_prod / math.pow((1 + hyp_const * init_dec * time), 1 / hyp_const)
print(f"Production rate is {Arp:.2f} barrels/day")

print()

# Tsiolkovsky rocket equation
print("This program calculates the change of velocity given initial mass, final mass, and exhaust velocity")
init_mass = float(input("Please enter the initial mass (kg): "))
final_mass = float(input("Please enter the final mass (kg): "))
exhaust_velocity = float(input("Please enter the exhaust velocity (m/s): "))
Tsiolkovsky = exhaust_velocity * math.log(init_mass / final_mass)
print(f"Change of velocity is {Tsiolkovsky:.1f} m/s")