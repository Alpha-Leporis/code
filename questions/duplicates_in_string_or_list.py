# find out duplicate character in string in python

def find_duplicates(input_string):
    seen = set()
    duplicates = set()

    for char in input_string:
        if char in seen:
            duplicates.add(char)
        seen.add(char)

    return list(duplicates)

# Example usage:
input_string = "hello world"
print("Duplicate characters:", find_duplicates(input_string))

'''
time complexity: O(n)
space complexity: O(m), where m is the number of unique characters in the input string.
'''

# find string has duplicate or not in python 
def has_duplicates(input_string):
    seen = set()

    for char in input_string:
        if char in seen:
            return True
        seen.add(char)

    return False

# Example usage:
input_string1 = "hello"
input_string2 = "world"
print("Input string 1 has duplicates:", has_duplicates(input_string1))
print("Input string 2 has duplicates:", has_duplicates(input_string2))

'''
time complexity: O(n)
space complexity: O(n), where n is the number of unique characters in the input string.
'''
