'''
A password string pwd, consists of binary characters (0's
and 1's). A cyber security expert is trying to determine the
minimum number of changes required to make the
password secure. To do so, it must be divided into
substrings of non-overlapping even length substrings. Each
substring can only contain 1's or 0's, not a mix. This helps to
ensure that the password is strong and less vulnerable to
hacking attacks
Find the minimum number of characters that muust be
flipped in the password string i.e. changed from 0 to 1 or 1
to 0 to allow the string to be divided as described.

Sample test 1
Input
pwd = "101011"
output: 2

Sample test 2
Input
pwd = "100110"
output: 3
'''

'''
To solve this problem in Python, you can follow these steps:
1. Iterate through the password string and count the number of mismatches in each even-length substring.
2. For each even-length substring, determine the minimum number of changes required to make it contain only one type of character (either all 0's or all 1's).
3. Sum up the minimum number of changes required for all even-length substrings.
4. Return the total minimum number of changes required.

This code defines a function min_changes_to_secure_password that takes the password string as
input and returns the minimum number of changes required to make the password secure according to the described criteria.

time complexity is O(n), where n is the length of the password string.
space complexity is O(1).
'''

def min_changes_to_secure_password(pwd):
    changes = 0
    for i in range(0, len(pwd), 2):
        # Count mismatches in the current even-length substring
        count_0 = pwd[i:i+2].count('0')
        count_1 = pwd[i:i+2].count('1')
        
        # Determine the minimum number of changes required to make the substring secure
        changes += min(count_0, count_1)
    
    return changes

# Example usage:
password = "100110"
min_changes = min_changes_to_secure_password(password)
print("Minimum number of changes required:", min_changes)


# optimized solution:

'''
To optimize the solution, we can avoid iterating over each character in the password 
string by realizing that we only need to count mismatches at even indices. 
Additionally, we can avoid creating substrings and directly compare characters at even indices.

This optimized solution directly compares characters at even indices, 
avoiding the need to create substrings and count occurrences of '0' and '1'. 
It reduces the number of operations needed and improves efficiency.

time complexity is O(n), where n is the length of the password string.
space complexity is O(1).

'''

def min_changes_to_secure_password(pwd):
    changes = 0
    for i in range(0, len(pwd), 2):
        if pwd[i] != pwd[i + 1]:
            changes += 1
    
    return changes

# Example usage:
password = "100110"  # 3
# password = "101011" # 2
min_changes = min_changes_to_secure_password(password)
print("Minimum number of changes required:", min_changes)

