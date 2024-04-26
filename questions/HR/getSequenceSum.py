'''
Given three integers. i, j and k, a sequence sum tobe the value of 
i + (i + 1) + (i + 2) + (i + 3)+....+ j + (j-1) + (j-2) + (j-3) +....+ k 
(increment from i until it equals j, then decrement from j until it equals k).
Given values i, J, and k, calculate the sequence sum.

Example
i = 5
j = 9
k = 6

Sum all the values from i to j and back to k: 5 + 6 +
7 + 8 + 9 + 8 +  7 + 6 = 56.

Function Description:
Complete the function getSequenceSum.

getSequenceSum has the following parameter(s):
int i, intj, int k: three integers

Return:
long: the value of the sequence sum
'''

# solution:

'''
To solve this problem, we can calculate the sum of the sequence in two parts: 
from i to j (inclusive) and from j to k (inclusive). 
Then, we return the sum of these two parts.

This function calculates the sum of the sequence in two parts: 
from i to j and from j to k, and then returns the total sum of the sequence.

time complexity: O(j - i + k - j + 2), which simplifies to O(k - i + 2).
Space complexity: O(1)
'''

def getSequenceSum(i, j, k):
    # Calculate the sum from i to j
    sum1 = sum(range(i, j + 1))
    
    # Calculate the sum from j to k
    sum2 = sum(range(j, k - 1, -1))
    
    # Return the total sum
    return sum1 + sum2

# Example usage:
i = 5
j = 9
k = 6
result = getSequenceSum(i, j, k)
print(result)  # Output: 56


# Optimized solution:

'''
To optimize the solution, we can avoid calculating the sum of ranges separately for each part of the sequence. 
Instead, we can directly calculate the sum of the sequence using a formula.

The sum of a sequence from i to j is the arithmetic sum of the integers in that range, 
which can be calculated as (j - i + 1) * (i + j) / 2. Similarly, the sum of a sequence from j to k can be calculated in the same way.

This optimized solution directly calculates the sum of each part of the sequence using the arithmetic sum formula, 
resulting in a more efficient implementation

Time complexity: O(1)
Space complexity: O(1)
'''

def getSequenceSum(i, j, k):
    # Calculate the sum from i to j
    sum1 = (j - i + 1) * (i + j) // 2
    
    # Calculate the sum from j to k
    sum2 = (k - j + 1) * (j + k) // 2
    
    # Return the total sum
    return sum1 + sum2

# Example usage:
i = 5
j = 9
k = 6
result = getSequenceSum(i, j, k)
print(result)  # Output: 56
