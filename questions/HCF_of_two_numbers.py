
# Write a program to find HCF of two numbers by without using recursion
'''
Algorithm:
    1. Check if smaller of two number divide larger number. If yes, HCF is smaller
    2. Else, Start from smaller/2 to 1 and check if current number divides both the input numbers.
    3. If yes, then current number is required HCF.

TC = O(min(num1,num2)), where num1num1 and num2num2 are the input numbers.
SC = O(1)
'''

def find_hcf(num1, num2):
    # Determining the Smaller Number
    if num1 > num2:
        smaller = num2
    else:
        smaller = num1

    # Finding the HCF
    for i in range(1, smaller + 1):
        if num1 % i == 0 and num2 % i == 0:
            hcf = i
    return hcf # Returning the HCF

# Example usage:
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("The HCF of", num1, "and", num2, "is:", find_hcf(num1, num2))

'''
This program first determines which of the two input numbers is smaller.
Then, it iterates from 1 up to the smaller number and checks if both input numbers are divisible by the current number in the iteration. 
If they are, it updates the HCF. Finally, it returns the HCF after the loop completes.

'''