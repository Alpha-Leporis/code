# 

'''
program consists of three functions:

    fibonacci(n): This function generates the Fibonacci series up to the nnth term.

    fibonacci_triangle(rows): This function generates the Fibonacci triangle with the specified number of rows. It calls the fibonacci() function to generate the Fibonacci series for each row and appends these series to form the triangle.

    print_fibonacci_triangle(triangle): This function prints the Fibonacci triangle row by row.

TC = O(rows2)
SC = O(rows2)
'''

def fibonacci(n):
    fib_series = [0, 1]  # Initialize Fibonacci series with first two numbers
    while len(fib_series) < n:
        fib_series.append(fib_series[-1] + fib_series[-2])  # Generate next Fibonacci number
    return fib_series

def fibonacci_triangle(rows):
    triangle = []  # Initialize the triangle
    for i in range(1, rows + 1):
        fib_row = fibonacci(i)  # Generate Fibonacci series for the current row
        triangle.append(fib_row)  # Add the Fibonacci series to the triangle
    return triangle

def print_fibonacci_triangle(triangle):
    for row in triangle:
        print(" ".join(map(str, row)))  # Print each row of the triangle

# Example usage:
rows = int(input("Enter the number of rows for the Fibonacci triangle: "))
fib_triangle = fibonacci_triangle(rows)
print("Fibonacci Triangle:")
print_fibonacci_triangle(fib_triangle)
