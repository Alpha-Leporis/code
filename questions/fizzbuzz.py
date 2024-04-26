'''
This function takes an integer n as input and prints Fizz, Buzz, FizzBuzz,
or the number itself based on the rules described above.
we can adjust the argument to fizzbuzz() to generate the FizzBuzz sequence for different ranges.

time complexity = O(n) and space complexity = O(1)
'''
def fizzbuzz(n):
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

# Example usage:
fizzbuzz(20)


