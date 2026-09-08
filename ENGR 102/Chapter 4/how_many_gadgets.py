# By submitting this assignment, I agree to the following
#  "Aggies do not lie, cheat, or steal, or tolerate those who do."
#  "I have not given or received any unauthorized aid on this assignment."
#
# Name:  Robert Chaney
# Section:  538
# Assignment:  Lab 4b
# Date:  9/12/24

import math

output = 0
gadsPerDay = 10

day = int(input("Please enter a positive value for day: "))

output = 0
    
if day <= 10:  # Initial production rate: 10/day
    output = day * gadsPerDay

elif 11 <= day < 50:  # Ramp-up phase from day 11 to 49
    # Sum of gadgets for days 1-10
    output = 10 * 10

    # Sum of gadgets for days 11 to 'day'
    min_gadgets = 11  # gadgets produced on day 11
    ramp_up_days = day - 10
    output += (ramp_up_days * (min_gadgets + day)) // 2

elif 50 <= day <= 101:  # Full-speed production phase from day 50 to 101
    # Sum of gadgets for days 1-10
    output = 10 * 10

    # Sum of gadgets for days 11 to 49
    output += (40 * (11 + 50)) // 2

    # Full-speed production from day 50 to 'day'
    full_speed_days = day - 49
    output += 50 * full_speed_days

if(day < 0):
    print("You entered an invalid number!")
else:
    print(f"The sum total number of gadgets produced on day {day} is {int(output)}")