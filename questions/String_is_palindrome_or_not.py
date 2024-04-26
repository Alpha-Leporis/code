# string is a palindrome or not

'''
Algorithm:
    1. Get the length of input string. 
    2. Do following while low index ‘l’ is smaller than high index ‘h’ where l is initialised to 0 and high to n-1
        a. If str[l] is not same as str[h], then return false. 
        b. Increment l and decrement h, i.e., do l++ and h–. 
    If all character match, return true.

TC = O(n), where nn is the length of the input string
SC = O(n), where nn is the length of the input string
'''

def is_palindrome(input_string):
    # Convert the input string to lowercase and remove non-alphanumeric characters
    input_string = ''.join(char.lower() for char in input_string if char.isalnum())
    # Check if the string is equal to its reverse
    return input_string == input_string[::-1]

# Example usage:
input_string = input("Enter a string: ")
if is_palindrome(input_string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")


'''
Here we have implemented a function is_palindrome to check if the string is a palindrome or not. 
By using left and right pointers to compare the characters from start and end to the string moving towards the center.
'''
def is_palindrome(string):

    string = string.lower()

    left = 0

    right = len(string) - 1

    while left < right:

        if string[left] != string[right]:

            return False

        left += 1

        right -= 1

    return True


