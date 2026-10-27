# Method 1: Using a user-defined function with iterative looping
def generate_fibonacci_iterative(n):
    fib_series = []
    if n <= 0:
        return fib_series
    elif n == 1:
        return [0]
    
    fib_series = [0, 1]
    for i in range(2, n):
        next_term = fib_series[-1] + fib_series[-2]
        fib_series.append(next_term)
    return fib_series

# Method 2: Using a recursive function to find the nth Fibonacci term
def fibonacci_recursive_term(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive_term(n - 1) + fibonacci_recursive_term(n - 2)

# Driver Code / Demonstration
terms = int(input("Enter the number of terms for Fibonacci series: "))

if terms <= 0:
    print("Please enter a positive integer.")
else:
    # Generating using iterative user-defined function
    iterative_result = generate_fibonacci_iterative(terms)
    print(f"\nFibonacci Series (Iterative, {terms} terms): {iterative_result}")
    
    # Generating using recursive user-defined function
    recursive_result = [fibonacci_recursive_term(i) for i in range(terms)]
    print(f"Fibonacci Series (Recursive, {terms} terms): {recursive_result}")