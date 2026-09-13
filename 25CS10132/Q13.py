import numpy as np
from scipy.integrate import quad


def f(x):
    return x**3 + np.sin(x)


def compute_derivative(func, x_val, dx=1e-6):
    return (func(x_val + dx) - func(x_val - dx)) / (2 * dx)


def compute_definite_integral(func, a, b):
    result, abs_error = quad(func, a, b)
    return result, abs_error


if __name__ == "__main__":
    x_point = 2.0
    lower_bound = 0.0
    upper_bound = 3.0

    df_dx = compute_derivative(f, x_point)
    integral_val, error = compute_definite_integral(
        f, lower_bound, upper_bound
    )

    print(f"Derivative at x = {x_point}: {df_dx:.6f}")
    print(
        f"Definite Integral from {lower_bound} to {upper_bound}: {integral_val:.6f} (Estimated Error: {error:.2e})"
    )