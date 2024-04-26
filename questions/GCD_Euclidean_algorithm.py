# Write a code to find out the greatest common divisor (GCD) of two numbers.

'''
we can find the greatest common divisor (GCD) of two numbers using the Euclidean algorithm.

This function repeatedly applies the Euclidean algorithm, 
which states that the GCD of two numbers remains the same as the GCD of the smaller number
and the remainder of the larger number divided by the smaller number, 
until the remainder becomes 0. Then, the GCD is the non-zero value left

time complexity: O(log(min(a,b)))
space complexity: O(1)
'''

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Example usage:
num1 = 48
num2 = 18
print("The GCD of", num1, "and", num2, "is:", gcd(num1, num2))
