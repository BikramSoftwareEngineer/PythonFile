import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


def poly2(x, a, b, c):
    return a * x**2 + b * x + c


x_data = np.array([1, 2, 3, 4, 5, 6])
y_data = np.array([6, 17, 34, 57, 86, 121])

params, _ = curve_fit(poly2, x_data, y_data)
a, b, c = params

print(f"Fitted Polynomial: y = {a:.2f}x^2 + {b:.2f}x + {c:.2f}")

x_dense = np.linspace(min(x_data), max(x_data), 100)
y_dense = poly2(x_dense, a, b, c)

plt.scatter(x_data, y_data, color='red', label='Original Data')
plt.plot(x_dense, y_dense, color='blue', label=f'Fitted Curve: {a:.1f}x² + {b:.1f}x + {c:.1f}')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Second-Degree Polynomial Fitting')
plt.legend()
plt.grid(True)
plt.show()