
'''
Algorithm:
    1. Traverse through sentence
    2. If character is not a,e,i,o,u r store character in new string else ignore.

TC = O(n+m), where nn is the length of the input string
SC = O(n+m), where nn is the length of the input string
'''

def remove_vowels(input_string):
    vowels = "aeiouAEIOU"
    # Using list comprehension to filter out vowels
    result = ''.join([char for char in input_string if char not in vowels])
    return result

# Example usage:
input_string = input("Enter a string: ")
result = remove_vowels(input_string)
print("String after removing vowels:", result)