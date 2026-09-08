#File: q3.py
#Author: Robert Chaney
#Date: 09/04/2026
#Section: 500 (?)
#Email: robertjchaney@tamu.edu
#Description: e.g. This program asks the user for number of days as
#input and return the output in days, months, and years.

days = int(input("Enter the number of days: "))
months = days // 30
daysLeft = days % 30
days = days - days 
years = months // 12
months = months - 12 * years
print(days, "days =", years, "years,", months, "months, and", days, "days")