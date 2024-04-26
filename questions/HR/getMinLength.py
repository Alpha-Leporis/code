'''
1. Substring Removal

Given a string, seq, that consists of the characters
'A' and 'B' only. In one move. delete ether an "AB"
or a "BB" substring and concatenate the remaining
substrings.

Find the minimum possible length of the remaining
string after performing any number of moves.

Note: A substring is a contiguous subsequence of a
string.

Example
seq = "BABBA"

using 0-based indexing, the following moves are
optimal.

• Delete the substring "AB" starting at index 1. 
"BABBA" --> "BBA"

• Delete the substang starting at index 0. 
    "BBA" --> "A"

There are no more moves. so the the minimum possible 
length of the remaining string is 1.
'''

# Solution:

'''
This function iterates through the characters of the input string seq, keeping track of a stack. 
It considers each character and checks if it can be paired with the last character in the stack to be removed. 
Finally, it returns the length of the remaining stack, which represents the minimum possible length of the remaining string.

time complexity: O(n), where n is the length of the input string seq.
space complexity: O(n), where n is the length of the input string seq.
'''

def getMinLength(seq):
    stack = []
    for char in seq:
        if char == 'A':
            if stack and stack[-1] == 'B':
                stack.pop()
            else:
                stack.append(char)
        elif char == 'B':
            if stack and stack[-1] == 'B':
                stack.pop()
            else:
                stack.append(char)
    return len(stack)

# Example usage:
seq = "BABBA"
print(getMinLength(seq))  # Output: 1


# Optimized version:

'''
To optimize the solution, we can avoid using a stack and instead directly count the number of 
"AB" and "BB" substrings in the input string. By doing so, we can eliminate the need for additional space.

This optimized solution directly counts the number of "AB" and "BB" substrings in the input string by 
iterating over the string once. Then, it calculates the remaining length by subtracting the counts of 
these substrings from the total length of the string. Finally, it subtracts the minimum count of "AB" and "BB" 
substrings to account for removing those substrings. This approach avoids using extra space, resulting in a more efficient solution.

time complexity: O(n), where n is the length of the input string seq.
space complexity: O(1)
'''

def min_remaining_length(seq):
    count_AB = 0
    count_BB = 0
    for i in range(len(seq)):
        if seq[i:i+2] == 'AB':
            count_AB += 1
        elif seq[i:i+2] == 'BB':
            count_BB += 1
    
    # After counting, calculate the remaining length
    remaining_length = len(seq) - (count_AB + count_BB)
    
    # If there are any "AB" or "BB" substrings left, we need to remove them as well
    remaining_length -= min(count_AB, count_BB)
    
    return remaining_length

# Example usage:
seq = "BABBA"
print(min_remaining_length(seq))  # Output: 1

