# By submitting this assignment, I agree to the following
#  "Aggies do not lie, cheat, or steal, or tolerate those who do."
#  "I have not given or received any unauthorized aid on this assignment."
#
# Name:  Robert Chaney, Colby Hudson, Cash Ostberg
# Section:  538
# Assignment:  9a
# Date: 10/16/24
import math
import statistics

########################### Function A ###########################
def parta(r_sphere, r_hole):
    volSphere = (4 / 3) * (math.pi * r_sphere**3)
    h = r_sphere - math.sqrt(r_sphere**2 - r_hole**2)
    volCap = ((math.pi * h**2) / 3) * (3 * r_sphere - h)
    volCylinder = math.pi * (r_hole**2) * (r_sphere - h)
    volHole = 2 * (volCap + volCylinder)
    return volSphere - volHole

# print(parta(1, 0.25))





########################### Function B ###########################
def partb(n):
    num_set = []                                   
    for i in range(2, n, 2):                        # goes through every 2 numbers from 2 - n
        num_set = []                             # resets the number list
        for j in range(n // 2):                     # iterates n / 2 amount of times
            # print(i)
            num_set.append(i + (j * 2))                          # adds every even number from 2 - n
            if sum(num_set) == n:                          # 
                # print(num_set)
                return num_set
                          
    return False

# print(partb(16))

########################### Function C ###########################

# minimum, median, and maximum value of the list, in that order.

def partc(list):
    list.sort()
    
    return min(list), statistics.median(list), max(list)
     

########################### Function D ###########################
def partd(times, distances):
    velocityList = []
    for i in range(len(times) - 1):
        rise = distances[i] - distances[i + 1]      # find the change in y for the function
        run = times[i] - times[i + 1]               # finds the change in x for the function
        velocity = (rise / run)                     # calculates the slop base on rise/run
        velocityList.append(velocity)

    return velocityList

# print(parte([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [-0.1, 1.5, 1.54, 3.09, 3.95, 4.78, 5.92, 7.5, 8.37, 9.03, 9.54]))

########################### Function E ###########################

# def parte(x):
#     #this is a commam
#     x = x




########################### Function F ###########################
# def partf(list):            
#     for i in range(len(list)):                  # runs through every index of the original list
#         for j in range(i, len(list)):           # runs through every number from i = index to the end of the list
#             if list[i] + list[j] == 2028:       # finds if any number from i to the end of the list will equal 2028
#                 return list[i] * list[j]

#     return False


