import math
import numpy as np

# Provided datasets from the experiment description
marks = [78, 85, 92, 67, 88, 73, 95, 81, 76, 89]
temperatures = [28.5, 30.2, 29.8, 31.4, 27.9, 32.1, 30.5]
sales = [12500, 13800, 14200, 11900, 15100, 14750, 16000]

datasets = {
    "Marks": marks,
    "Temperatures": temperatures,
    "Sales": sales
}

# 1. Custom functions without using NumPy
def compute_mean(data):
    return sum(data) / len(data)

def compute_median(data):
    sorted_data = sorted(data)
    n = len(sorted_data)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_data[mid - 1] + sorted_data[mid]) / 2
    else:
        return sorted_data[mid]

def compute_std(data, mean_val):
    variance = sum((x - mean_val) ** 2 for x in data) / len(data)
    return math.sqrt(variance)

def compute_min(data):
    m = data[0]
    for x in data:
        if x < m:
            m = x
    return m

def compute_max(data):
    m = data[0]
    for x in data:
        if x > m:
            m = x
    return m


# 2. Computation & Comparison
for name, data in datasets.items():
    print(f"=" * 60)
    print(f"Dataset: {name} -> {data}")
    print(f"=" * 60)
    
    # Without NumPy
    uw_mean = compute_mean(data)
    uw_median = compute_median(data)
    uw_std = compute_std(data, uw_mean)
    uw_min = compute_min(data)
    uw_max = compute_max(data)
    
    print("--- Without NumPy ---")
    print(f"Mean   : {uw_mean:.2f}")
    print(f"Median : {uw_median}")
    print(f"Std Dev: {uw_std:.2f}")
    print(f"Min    : {uw_min}")
    print(f"Max    : {uw_max}")
    
    # With NumPy
    np_data = np.array(data)
    np_mean = np.mean(np_data)
    np_median = np.median(np_data)
    np_std = np.std(np_data)  # Population standard deviation by default (ddof=0)
    np_min = np.min(np_data)
    np_max = np.max(np_data)
    
    print("\n--- With NumPy ---")
    print(f"Mean   : {np_mean:.2f}")
    print(f"Median : {np_median}")
    print(f"Std Dev: {np_std:.2f}")
    print(f"Min    : {np_min}")
    print(f"Max    : {np_max}\n")