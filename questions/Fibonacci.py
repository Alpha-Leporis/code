'''
Fibonacci number
'''

# TC: O(n)
# SC: O(n)

def fibonacci(n):
    fib_series = [0, 1]  # Initialize the series with the first two Fibonacci numbers
    
    # Generate subsequent Fibonacci numbers
    for i in range(2, n):
        next_num = fib_series[-1] + fib_series[-2]
        fib_series.append(next_num)
    
    return fib_series[:n]

# Example usage:
n = 10  # Number of Fibonacci numbers to generate
fib_nums = fibonacci(n)
print("Fibonacci Series up to", n, "terms:", fib_nums)


# recursive solution

# TC: O(2^n)
# SC: O(n)

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_series = fibonacci(n - 1)
        fib_series.append(fib_series[-1] + fib_series[-2])
        return fib_series

# Example usage:
n = 10  # Number of Fibonacci numbers to generate
fib_nums = fibonacci(n)
print("Fibonacci Series up to", n, "terms:", fib_nums)
