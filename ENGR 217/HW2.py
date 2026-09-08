import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error

P = np.array([0.6, 1, 1.4, 1.8, 2.2, 2.6, 3, 3.4, 3.8, 4.2, 4.6, 5, 5.4]).reshape(-1, 1)
K = np.array([5.89, 4.68, 4.1, 3.45, 3.25, 2.69, 2.25, 1.92, 1.55, 1.45, 1.19, 0.99, 0.84])

# Linear regression of log(K) vs P
logK = np.log(K)
linreg_log = LinearRegression().fit(P, logK)

# Find A and B
B = linreg_log.coef_[0]
A = np.exp(linreg_log.intercept_)

# Predicted K from exponential model
Kfit_exp = A * np.exp(B * P.flatten())

# MSE for exponential fit
mse_exp = mean_squared_error(K, Kfit_exp)

# Polynomial regression loop
order = 1
mse_poly = float('inf')
best_order = None
best_Kfit_poly = None

while mse_poly > mse_exp and order < 10:
    poly = PolynomialFeatures(degree=order)
    P_poly = poly.fit_transform(P)
    linreg_poly = LinearRegression().fit(P_poly, K)
    Kfit_poly = linreg_poly.predict(P_poly)
    mse_poly = mean_squared_error(K, Kfit_poly)
    
    if mse_poly < mse_exp:
        best_order = order
        best_Kfit_poly = Kfit_poly
        break
    order += 1

# Plot results
plt.figure(figsize=(10,5))

# Exponential fit plot
plt.scatter(P, K, color="blue", label="Data")
plt.plot(P, Kfit_exp, color="red", label=f"Exponential Fit (MSE={mse_exp:.4f})")

# Polynomial fit plot (only if found)
if best_order is not None:
    plt.plot(P, best_Kfit_poly, color="green", label=f"Polynomial Fit (order={best_order}, MSE={mse_poly:.4f})")

plt.xlabel("Pressure (1000 psia)")
plt.ylabel("Equilibrium Constant K")
plt.title("Exponential vs Polynomial Regression Fits")
plt.legend()
plt.grid(True)
plt.show()

(best_order, mse_exp, mse_poly)
