import numpy as np
from scipy.optimize import minimize


def f(variables):
    x, y = variables
    return (x - 2) ** 2 + (y - 2) ** 2


initial_guess = [0, 0]

result = minimize(f, initial_guess)

if result.success:
    x_min, y_min = result.x
    min_value = result.fun
    print(f"Optimization Successful!")
    print(f"Minimum occurs at (x, y) = ({x_min:.4f}, {y_min:.4f})")
    print(f"Minimum value of the function f(x, y) = {min_value:.4f}")
else:
    print("Optimization failed.")