'''
For an array arr of n positive integers, count the
unordered pairs (i, j) (0 <= i < j < n) where arr[i] XOR
arr[j] > arr[i] AND arr[j]. XOR denotes the bitwise
XOR operation and AND denotes the bitwise AND
operation.

Example
Given n = 4, arr = [4, 3, 5, 2]. All unordered pairs
(i, j) are-

Indices		XOR	AND	XOR > AND
(0,1)		 7	 0	  True
(0,2)		 1	 4	  False
(0,3)		 6	 0	  True
(1,2)		 6	 1	  True
(1,3)		 1	 2	  False
(2,3)		 7	 0	  True

for the first line:
• arr[0] = 4, arr[1] = 3
• 4 XOR 3 = 7
• 4 AND 3 = 0
• 7 > 3

Thre are 4 good pairs where XOR > AND shows True.
Return 4.
'''

# Solution:

'''
Time complexity: O(n^2), where n is the length of the array.
Space complexity: O(1)
'''

def countUnorderedPairs(arr):
    n = len(arr)
    count = 0
    
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] ^ arr[j] > arr[i] & arr[j]:
                count += 1
    
    return count

# Example usage:
arr = [4, 3, 5, 2]
print(countUnorderedPairs(arr))  # Output: 4


# Second solution:

'''
DP solution Explanation:
    1. The function dominating_xor_pairs takes an array arr as input.
    2. It initializes a counter count to 0 and creates a list bits of size 32, initialized with zeros. This list will be used to count the occurrence of each bit position in the array elements.
    3. It then iterates through each element of the array and calculates the position of the most significant bit that is set in the binary representation of the element using math.log2(arr[i]). This gives the position of the leftmost bit that is 1. For example, if the value of arr[i] is 5 (binary: 101), the result will be 2 (as 2^2 = 4).
    4. It then increments the count of bits at that position in the bits list and accumulates the count in the variable count.
    5. Finally, it calculates the total number of dominating XOR pairs using the formula n * (n-1) // 2 - count, where n is the length of the array. This formula calculates the total number of possible pairs and subtracts the count of dominating XOR pairs.

Time complexity: O(n), where n is the length of the array.
Space complexity: O(1) 
'''

import math

def dominating_xor_pairs(arr):
    n = len(arr)
    count = 0
    # for storing count of numbers
    bits = [0] * 32
    # itreating from 0 to n-1
    for i in range(n):
        val = int(math.log2(arr[i]))
        count += bits[val]
        bits[val] += 1
    
    return n * (n-1) // 2 - count

# Example usage:
arr = [4, 3, 5, 2]
print(dominating_xor_pairs(arr))  # Output: 4


