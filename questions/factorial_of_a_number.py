# Write a function to find the factorial of a number

'''
time complexity: O(n), where nn is the value of the input number
space complexity:O(n), due to the recursion depth
'''

def factorial(number):

    if number == 0:

        return 1

    return number * factorial(number - 1)