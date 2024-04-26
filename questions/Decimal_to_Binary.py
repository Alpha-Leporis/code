# Write a program to Change Decimal Number to Binary

'''
Algorithm: Convert Decimal to Binary

Input: decimal (a non-negative integer)

    1. Initialize an empty string binary to store the binary representation.
    2. While the decimal number is greater than 0, do the following:
        a. Calculate the remainder of the division of the decimal number by 2.
        b. Convert the remainder to a string and prepend it to the binary string.
        c. Update the decimal number to be the result of integer division by 2.
    3. If the binary string is still empty (i.e., the input decimal number was 0), set the binary string to "0".
    4. Return the binary string, which represents the binary representation of the input decimal number.

TC = O(logn), where n is the decimal number
SC = O(logn), where n is the decimal number
'''

def decimal_to_binary(decimal):
    binary = "" # Initializing Binary Representation
    # Conversion to Binary
    while decimal > 0:
        remainder = decimal % 2
        binary = str(remainder) + binary
        decimal //= 2
    return binary if binary else "0" # Returning Binary Representation

# Example usage:
decimal_number = int(input("Enter a decimal number: "))
binary_representation = decimal_to_binary(decimal_number)
print("Binary representation:", binary_representation)



