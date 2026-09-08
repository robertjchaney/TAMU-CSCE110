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

# Reynolds Number
velocity = 9
kin_visc = 0.0015
lin_dim = 0.875
Reynold = velocity * lin_dim / kin_visc
print(f"Reynolds number is {Reynold}")

# Bragg's Law
distance = 0.028
theta = math.radians(35)
Bragg = 2 * distance * math.sin(theta)
print(f"Wavelength is {Bragg} nm")

# Arps equation
time = 10
init_prod = 100
init_dec = 2
hyp_const = 0.8
Arp = init_prod / math.pow((1 + hyp_const * init_dec * time), 1 / hyp_const)
print(f"Production rate is {Arp} barrels/day")

# Tsiolkovsky rocket equation
exhaust_velocity = 2028
init_mass = 11000
final_mass = 8300
Tsiolkovsky = exhaust_velocity * math.log(init_mass / final_mass)
print(f"Change of velocity is {Tsiolkovsky} m/s")