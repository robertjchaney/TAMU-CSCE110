# By submitting this assignment, I agree to the following
#  "Aggies do not lie, cheat, or steal, or tolerate those who do."
#  "I have not given or received any unauthorized aid on this assignment."
#
# Name:  Robert Chaney, Colby Hudson, Cash Ostberg
# Section:  538
# Assignment:  13a
# Date: 11/5/24



import numpy as np
import matplotlib.pyplot as plt

coefficients = input('Enter the coefficients: ').split()
# print(coefficients)


def find_local_extrema(y_values):
    maxima = []
    minima = []
    for i in range(1, len(y_values) - 1):
        # Check for a local maximum
        if y_values[i - 1] < y_values[i] > y_values[i + 1]:
            maxima.append(i)
        # Check for a local minimum
        elif y_values[i - 1] > y_values[i] < y_values[i + 1]:
            minima.append(i)
    return maxima, minima



xvalue = np.arange(-5, 5, .1)

f = np.zeros_like(xvalue)
fPrime = np.zeros_like(xvalue)
fDoublePrime = np.zeros_like(xvalue)

degree = len(coefficients) - 1

for i, coef in enumerate(coefficients):
    power = degree - i

    f += int(coef) * (xvalue ** (degree - i))
    
    if power > 0:
        fPrime += int(coef) * power * (xvalue ** (power - 1))

    if power > 1:
        fDoublePrime += int(coef) * power * (power - 1) * (xvalue ** (power - 2))

        

f_maxima, f_minima = find_local_extrema(f)
fPrime_maxima, fPrime_minima = find_local_extrema(fPrime)
fDoublePrime_maxima, fDoublePrime_minima = find_local_extrema(fDoublePrime)



plt.figure(figsize=(10, 6))
plt.axis((-5, 5, -100, 250))
plt.xlabel("X")
plt.ylabel("Y")
plt.axhline(y=0, color="black")
plt.axvline(x=0, color="black")
plt.title("Plots of f(x), f'(x), and f''(x) with Local Maxima and Minima")

# Plot f(x)
plt.plot(xvalue, f, color='blue', label='f(x)')
plt.plot(xvalue[f_maxima], f[f_maxima], "ko")
plt.plot(xvalue[f_minima], f[f_minima], "ko")

# Plot f'(x)
plt.plot(xvalue, fPrime - 11, color='green', linestyle='dashed', label="f'(x)")
plt.plot(xvalue[fPrime_maxima], fPrime[fPrime_maxima] - 11, "ko")
plt.plot(xvalue[fPrime_minima], fPrime[fPrime_minima] - 11, "ko")

# Plot f''(x)
plt.plot(xvalue, fDoublePrime, color='red', linestyle='dotted', label="f''(x)")
plt.plot(xvalue[fDoublePrime_maxima], fDoublePrime[fDoublePrime_maxima] - 11, "ko")
plt.plot(xvalue[fDoublePrime_minima], fDoublePrime[fDoublePrime_minima] - 11, "ko")

plt.legend(loc='upper left')
plt.show()

