'''
Consider a string, S, that is a series of characters,
each followed by its frequency as an integer. The
string is not compressed correctly, so there may
be multiple occurrences of the same character. A
properly compressed string will consist of one
instance of each character in alphabetical order
followed by the total count of that character
within the string.
'''

# solution:

'''
can solve this problem in Python by iterating through the string 
and constructing a dictionary to store the frequency of each character. 
Then, you can generate the compressed string by iterating through the 
dictionary keys in alphabetical order and appending the character 
followed by its frequency. 

This function takes a string s as input, iterates through it to 
construct a frequency dictionary, and then generates the compressed 
string by iterating through the dictionary keys in alphabetical order. 
Finally, it returns the compressed string.

time complexity: O(n), where n is the length of the input string.
space complexity: O(n),
'''

def compress_string(s):
    freq_dict = {}
    compressed_string = ""

    # Construct frequency dictionary
    i = 0
    while i < len(s):
        char = s[i]
        freq = ""
        i += 1
        while i < len(s) and s[i].isdigit():
            freq += s[i]
            i += 1
        freq_dict[char] = freq_dict.get(char, 0) + int(freq)

    # Generate compressed string
    for char in sorted(freq_dict.keys()):
        compressed_string += char + str(freq_dict[char])

    return compressed_string

# Example usage
s = "a3b4a1c5q6"
compressed = compress_string(s)
print("Compressed string:", compressed)
