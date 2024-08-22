import math

#! /usr/bin/env python

# Reynolds Number
u = 9
v = 0.0015
L = 0.875
Re = u * L / v
print(f"Reynolds number is {Re}")

# Bragg's Law
d = 0.028
theta = math.radians(35)
nLambda = 2 * d * math.sin(theta)
print(f"Wavelength is {nLambda} nm")

# Arps equation
t = 10
qi = 100
Di = 2
b = 0.8
q = qi / math.pow((1+ b * Di * t), 1 / b)
print(f"Production rate is {q} barrels/day")

# Tsiolkovsky rocket equation
ve = 2028
m0 = 11000
mf = 8300
deltaV = ve * math.log(m0 / mf)
print(f"Change of velocity is {deltaV} m/s")