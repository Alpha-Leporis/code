'''
You can find the Least Common Multiple (LCM) of three numbers by 
using the fact that 
LCM(a, b, c) = LCM(LCM(a, b), c). 
'''

# Solution:

'''
In this program:
1. gcd() function calculates the Greatest Common Divisor (GCD) of two numbers using Euclid's algorithm.
2. lcm() function calculates the LCM of two numbers using the formula LCM(a, b) = (a * b) / GCD(a, b).
3. lcm_of_three_numbers() function calculates the LCM of three numbers by first finding the LCM of the first two numbers, and then finding the LCM of that result and the third number.
4. Finally, an example usage is provided where you can input three numbers, and the program will output their LCM.

TC: O(log(min(a, b)))
SC: O(1) 
'''

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b)

def lcm_of_three_numbers(x, y, z):
    lcm_xy = lcm(x, y)
    lcm_xyz = lcm(lcm_xy, z)
    return lcm_xyz

# Example usage
num1 = 12
num2 = 15
num3 = 20

lcm_result = lcm_of_three_numbers(num1, num2, num3)
print("LCM of {}, {}, and {} is: {}".format(num1, num2, num3, lcm_result))
