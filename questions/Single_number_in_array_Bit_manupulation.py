'''
Problem Statement:
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

Example:
Input: nums = [2,2,1]
Output: 1

Approach:
This problem can be efficiently solved using bitwise XOR operation. XORing a number with itself results in 0, and XORing a number with 0 results in the number itself. Therefore, if we XOR all elements in the array, the duplicate numbers will cancel each other out, leaving only the single number.

'''

def singleNumber(nums):
    result = 0
    for num in nums:
        result ^= num
    return result

# Example usage:
nums = [2, 2, 1]
print(singleNumber(nums))  # Output: 1

'''
Explanation:
    1. Initialize the result variable to 0.
    2. Iterate through each number in the array.
    3. Perform bitwise XOR operation between the current number and the result.
    4. After iterating through all numbers, the result will contain the single number that appears only once.

This solution has a time complexity of O(n), where n is the number of elements in the array, as we iterate through the array once.
The space complexity is O(1), as we only use a constant amount of extra space regardless of the input size.
'''