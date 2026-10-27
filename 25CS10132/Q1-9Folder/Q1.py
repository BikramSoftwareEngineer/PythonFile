def calculate_factorial(n):
    if n < 0:
        return None  # Factorial is not defined for negative numbers
    
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

def is_prime(n):
    if n <= 1:
        return False
    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Driver Code / Demonstration
num = int(input("Enter a positive integer: "))

# Factorial calculation
fact = calculate_factorial(num)
if fact is None:
    print("Factorial is not defined for negative numbers.")
else:
    print(f"Factorial of {num} is {fact}")

# Prime number check
if is_prime(num):
    print(f"{num} is a Prime number.")
else:
    print(f"{num} is NOT a Prime number.")