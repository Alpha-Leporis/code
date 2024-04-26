'''
Given a string containing a number of
characters, find the substrings within
the string that satisfy the conditions
below:
• The substring's length should be in the
inclusive interval [minLength,maxLength]
•  The total number of unique characters
should not exceed maxUnique.

Using those conditions, determine the
frequency of the maximum occurring
substring.

Example 1
Sample Input:
    components = 'abcde'
    minLength = 2
    maxLength = 3
    maxUnique = 3
Sample output: 1

Example 2
Sample Input:
    components = 'abcde'
    minLength = 2
    maxLength = 4
    maxUnique = 26
Sample output:  1
'''

# Solution:  sliding window
'''
Explanation of the Code:
    1. The function getMaxOccurances takes four parameters: components (the input string), minLength, maxLength, and maxUnique.
    2. It iterates through the range of possible substring lengths (minLength to maxLength).
    3. For each substring length, it maintains a sliding window of that length (Window) and a counter (char_count) to keep track of the frequency of characters within the window.
    4. It also maintains a variable unique_chars to track the number of unique characters within the window.
    5. As the window slides through the input string, it updates the char_count and unique_chars accordingly.
    6. If the number of unique characters within the window is less than or equal to maxUnique, it calculates the frequency of the current substring and updates the maximum occurrence (max_occurance).

Time Complexity: O(n * (maxLength - minLength) * maxUnique)
Space Complexity: O(maxLength + maxUnique), depending on the size of window
'''
from collections import Counter

def getMaxOccurances(components, minLength, maxLength, maxUnique):
    n = len(components)
    max_occurance = 0

    for length in range(minLength, maxLength + 1):
        Window = []
        char_count = Counter()
        unique_chars = 0
        # store the character count in window
        for i in range(n):
            Window.append(components[i])
            char_count[components[i]] += 1

            if len(Window) > length:
                left_chars = Window.pop(0)
                char_count[left_chars] -= 1
                if char_count[left_chars] == 0:
                    del char_count[left_chars]
            
            if len(char_count) <= maxUnique:
                unique_chars = len(char_count)
            
            if len(Window) == length and unique_chars <= maxUnique:
                substring = ''.join(Window)
                count = components.count(substring, i - length +1, i+1)
                max_occurances = max(max_occurance, count)
                
    return max_occurances
    
# Example usage:
components = 'abcde'
minLength = 2
maxLength = 3
maxUnique = 3
print(getMaxOccurances(components, minLength, maxLength, maxUnique))  # Output: 1
   
print()

# Example usage:
components = 'abcde'
minLength = 2
maxLength = 4
maxUnique = 26
print(getMaxOccurances(components, minLength, maxLength, maxUnique))  # Output: 1
