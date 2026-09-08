#File: q2.py
#Author: Robert Chaney
#Date: 09/04/2026
#Section: 500 (?)
#Email: robertjchaney@tamu.edu
#Description: e.g. This program asks the user for the area of a circle, then
#calculates the circumfrence of the circle though algebraic methodology

import math
pi = 3.1415
print("Enter the area:", end=" ")
area = float(input())
rad = math.sqrt( area / pi )
cirum = 2 * pi * rad
print("Circumfrence of the circle is ", cirum)