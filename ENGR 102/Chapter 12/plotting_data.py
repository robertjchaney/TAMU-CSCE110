# By submitting this assignment, I agree to the following
#  "Aggies do not lie, cheat, or steal, or tolerate those who do."
#  "I have not given or received any unauthorized aid on this assignment."
#
# Name:  Robert Chaney
# Section:  538
# Assignment:  10b
# Date: 11/04/24

import csv
import matplotlib.pyplot as plt
import numpy as np
from collections import defaultdict


def read_weather_data(filename):
    dates = []
    max_temps = []
    min_temps = []
    avg_temps = []
    avg_wind_speeds = []
    
    with open(filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        
        for row in reader:
            dates.append(row['Date'])
            max_temps.append(float(row['Maximum Temperature (F)']) if row['Maximum Temperature (F)'] else 0.0)
            min_temps.append(float(row['Minimum Temperature (F)']) if row['Minimum Temperature (F)'] else 0.0)
            avg_temps.append(float(row['Average Temperature (F)']) if row['Average Temperature (F)'] else 0.0)
            avg_wind_speeds.append(float(row['Average Daily Wind Speed (mph)']) if row['Average Daily Wind Speed (mph)'] else 0.0)
    
    return dates, max_temps, min_temps, avg_temps, avg_wind_speeds

filename = 'C:\\Users\\ososb\\Downloads\\pythonProject\\Chapter 11\\WeatherDataCLL.csv'
dates, max_temps, min_temps, avg_temps, avg_wind_speeds = read_weather_data(filename)

# Create a figure thta can fit all 4 multiple subplots
fig, axs = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Weather Data Charts', fontsize=14)

# Line graph
ax1 = axs[0, 0]
ax1.plot(dates, max_temps, color='tab:red', label='Max Temperature')
ax1.set_xlabel('Date')
ax1.set_ylabel('Max Temperature (°F)', color='tab:red')
ax1.tick_params(axis='y', labelcolor='tab:red')
ax1Twin = ax1.twinx()
ax1Twin.plot(dates, avg_wind_speeds, color='tab:blue', label='Average Wind Speed')
ax1Twin.set_ylabel('Average Wind Speed (MPH)', color='tab:blue')
ax1Twin.tick_params(axis='y', labelcolor='tab:blue')
ax1.set_title('Max Temperature and Average Wind Speed Over Time')
ax1.legend(loc='upper left')
ax1Twin.legend(loc='upper right')

# Histogram
ax2 = axs[0, 1]
ax2.hist(avg_wind_speeds, bins=10, color='purple', edgecolor='black')
ax2.set_xlabel('Average Wind Speed (MPH)')
ax2.set_ylabel('Number of Days')
ax2.set_title('Average Wind Speeds')

# Scatterplot
ax3 = axs[1, 0]
ax3.scatter(avg_wind_speeds, min_temps, color='blue', s = 1)
ax3.set_xlabel('Average Wind Speed (MPH)')
ax3.set_ylabel('Min Temperature (°F)')
ax3.set_title('Average Wind Speed vs Min Temperature')

# Plot 4: Bar chart
monthlyData = defaultdict(lambda: {'sum_temp': 0, 'count': 0, 'max_temp': float('-inf'), 'min_temp': float('inf')})

for date, avg, max_temp, min_temp in zip(dates, avg_temps, max_temps, min_temps):
    month = int(date.split('-')[1])  # Extract month as an integer (1 = January, 2 = February, etc.)
    monthlyData[month]['sum_temp'] += avg
    monthlyData[month]['count'] += 1
    monthlyData[month]['max_temp'] = max(monthlyData[month]['max_temp'], max_temp)
    monthlyData[month]['min_temp'] = min(monthlyData[month]['min_temp'], min_temp)

# Sort the data by month
months = range(1, 13)
avgMonthlyTemp = [monthlyData[month]['sum_temp'] / monthlyData[month]['count'] for month in months]
maxMonthlyTemp = [monthlyData[month]['max_temp'] for month in months]
minMonthlyTemp = [monthlyData[month]['min_temp'] for month in months]

# Bar chart with line overlays
ax4 = axs[1, 1]
ax4.bar(months, avgMonthlyTemp, color='gold', label='Average Temperature', width=0.8, edgecolor= "black")
ax4.plot(months, maxMonthlyTemp, color='red', marker='o', label='High T')
ax4.plot(months, minMonthlyTemp, color='blue', marker='o', label='Low T')
ax4.set_xlabel('Month')
ax4.set_ylabel('Temperature (°F)')
ax4.set_title('Temperature by Month')
ax4.legend()
ax4.set_xticks(months)
ax4.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

plt.tight_layout(rect=[0, 0.03, 1, 0.95])  # Reserve space for the main title
plt.show()