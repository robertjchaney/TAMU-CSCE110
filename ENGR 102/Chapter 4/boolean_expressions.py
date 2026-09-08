# By submitting this assignment, I agree to the following
#  "Aggies do not lie, cheat, or steal, or tolerate those who do."
#  "I have not given or received any unauthorized aid on this assignment."
#
# Name:  Robert Chaney, Colby Hudson, Cash Ostberg
# Section:  538
# Assignment:  Lab 4a
# Date:  9/3/24

############ Part A ############
a = input("Enter True or False for a: ").upper()
b = input("Enter True or False for b: ").upper()
c = input("Enter True or False for c: ").upper()

aBool = (a == "TRUE") or (a == "T") 

bBool = (b == "TRUE") or (b == "T")

cBool = (c == "TRUE") or (c == "T")

############ Part B ############
print(f'a and b and c:', (aBool and bBool and cBool))
print(f'a or b or c:', aBool or bBool or cBool)

############ Part C ############
print(f'XOR:', (aBool or bBool) and not(aBool and bBool))

isOdd = (int(aBool) + int(bBool) + int(cBool)) % 2 == 1
print(f'Odd number:', isOdd)

############ Part D (OPTIONAL) ############
# # Complex Boolean expressions
# complex1 = (not (a and not b) or (not c and b)) and (not b) or (not a and b and not c) or (a and not b)
# complex2 = (not ((b or not c) and (not a or not c))) or (not (c or not (b and c))) or (a and not c) and (not a or (a and b and c) or (a and ((b and not c) or (not b))))

# # Simple Boolean expressions
# simple1 = False
# simple2 = True

# print(f'Complex 1: {complex1}')
# print(f'Complex 2: {complex2}')
# print(f'Simple 1: {simple1}')
# print(f'Simple 2: {simple2}')