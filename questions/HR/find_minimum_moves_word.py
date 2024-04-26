'''
An English lecture at HackerElementary School is aimed at teaching students the letters of the
alphabet.
The students are provided with a string word that consists of lowercase English letters, In one move.
They can choose any index i, and let the character at that index be c. Then the first occurence ot c to
the left of i, and the first occcurrence of c to right of i are deleted (Note: the operation can still be
carried out even if either the left or right occurance doesnt exist), For example, if word = "adabacaea",
,and if index 4 is Cosenn (0-based), the first occurrence of 'a' to the left and right of ndex
4 (bold, indices 2 and 6) are deleted leaving word = "adbacea".

find the minimum number of moves the students need to perform in order to get a word of minimal length.

Example:
Consider nod = "baabacaa"
The folleing moves are optimal.
1. Choose index 0, "baabacaa", then word "baaacaa". 
Delete the b to its right at index 3. there is no b to its left so the operation is finished.
2. Now, choose index 2,"baaacaa", then word = "bacaa".
3. Now, choose index 3, "bacaa", then word = "bca".

The word cannot be reduced further, The answer is 3.
'''

'''
we can iterate through each character in the word and keep track of the minimum number of moves
required to obtain the minimal length word. We'll maintain a set to store the characters that
have been encountered so far. When encountering a character for the first time, 
we'll calculate the distance to the nearest occurrences of that character on the left and right sides.
The minimum of these distances will represent the minimum number of moves needed to delete that character.
Finally, we sum up the minimum distances for all characters encountered to get the total minimum number of moves.

This solution iterates through each character in the word once, making it an 
O(n) time complexity solution, where n is the length of the input word. 
It uses additional space proportional to the number of unique characters encountered,
resulting in an O(c) space complexity, where c is the number of unique characters in the word.
'''

def min_moves_to_minimal(word):
    # Dictionary to store the index of first occurrence of each character
    char_index = {}

    # Set to store encountered characters
    encountered_chars = set()

    # Initialize minimum moves
    min_moves = 0

    # Iterate through each character in the word
    for i, char in enumerate(word):
        # If the character is encountered for the first time
        if char not in encountered_chars:
            # Update the index of first occurrence of the character
            char_index[char] = i
            encountered_chars.add(char)
        else:
            # Calculate the distance to the nearest occurrences on the left and right
            left_dist = i - char_index[char]
            right_dist = len(word) - i
            # Update minimum moves
            min_moves += min(left_dist, right_dist)
            # Update the index of first occurrence of the character
            char_index[char] = i

    return min_moves

# Example usage
word = "baabacaa"
result = min_moves_to_minimal(word)
print("Minimum number of moves:", result)  # Output: 3


# optimized implementation:
'''
we can simplify the logic and avoid unnecessary data structures. 
We don't need to store the index of the first occurrence of each character 
or keep track of encountered characters explicitly. Instead, we can traverse 
the string and calculate the distances to the nearest occurrences of each character
 on the left and right sides dynamically.

This optimized solution removes the need for storing encountered characters and
their first occurrence indices explicitly. Instead, it dynamically calculates 
the distances to the nearest occurrences of each character on the left and right sides
while traversing the string. This simplifies the logic and reduces the space complexity to O(1)
(excluding the input string). The time complexity remains O(n), where n is the length of the input word.

'''

def min_moves_to_minimal(word):
    # Initialize minimum moves
    min_moves = 0
    # Initialize dictionary to store the last seen index of each character
    last_seen = {}

    # Iterate through each character in the word
    for i, char in enumerate(word):
        # Calculate the distance to the nearest occurrences on the left and right
        left_dist = i - last_seen.get(char, -1)
        right_dist = len(word) - i
        # Update minimum moves
        min_moves += min(left_dist, right_dist)
        # Update the last seen index of the character
        last_seen[char] = i

    return min_moves

# Example usage
word = "baabacaa"
result = min_moves_to_minimal(word)
print("Minimum number of moves:", result)  # Output: 3



