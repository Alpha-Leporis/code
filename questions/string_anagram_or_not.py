# check if two strings are anagrams or not
'''
For example:
"listen" and "silent" are anagrams because they contain the same letters ('l', 'i', 's', 't', 'e', 'n') 
with the same frequency, even though the order of the letters is different.
'''

# solution:
def are_anagrams(str1, str2):
    # Convert both strings to lowercase and remove spaces
    str1 = str1.lower().replace(" ", "")
    str2 = str2.lower( ).replace(" ", "")
    
    # Check if the sorted versions of the strings are equal
    return sorted(str1) == sorted(str2)

# Example usage:
string1 = "listen"
string2 = "silent"
print(f"'{string1}' and '{string2}' are anagrams:", are_anagrams(string1, string2))


'''
time complexity: O(n log n)
space complexity: O(n)
'''

# optimized solution:

def are_anagrams(str1, str2):
    # Convert both strings to lowercase and remove spaces
    str1 = str1.lower().replace(" ", "")
    str2 = str2.lower().replace(" ", "")
    
    # Check if the lengths of the strings are equal
    if len(str1) != len(str2):
        return False
    
    # Create character frequency counters
    char_count1 = {}
    char_count2 = {}

    # Populate character frequency counters for both strings
    for char in str1:
        char_count1[char] = char_count1.get(char, 0) + 1
    for char in str2:
        char_count2[char] = char_count2.get(char, 0) + 1
    
    # Check if the character frequency counters are equal
    return char_count1 == char_count2

# Example usage:
string1 = "listen"
string2 = "silent"
print(f"'{string1}' and '{string2}' are anagrams:", are_anagrams(string1, string2))

'''
time complexity: O(n)
space complexity: O(n)
'''