'''
Contiguous subarrays are a group Of an
uninterrupted range of elements from an
array as they occur. No elements in the
range can be skipped or reordered. Given
an array of integers, numbers, and an
integer k, determine the total number of
subarrays of numbers that have a product
that is less than or equal to k

Example
numbers = [2, 3, 4]
The subarrays are [2], [3], [4], [2,3], [3,4]
[2, 3, 4] The product of a subarray is the
product of all of its elements so the
products for the list of subarrays are [2, 3, 4,
6, 12, 24].
If k 6, 4 subarrays satisfy the
condition, [2], [3],[4], [2, 3].
'''

# Solution: sliding window

def count_subarrays(arr, k):
    count = 0
    product = 1
    left = 0

    for right in range(len(arr)):
        product *= arr[right]
        
        while product > k and left <= right:
            product //= arr[left]
            left += 1
        
        if product <= k:
            count += right - left + 1

    return count

# Example usage:
arr = [2,3,4]
k = 6
result = count_subarrays(arr, k)
print("Total number of subarrays:", result)

'''
time complexity: O(n)
space complexity: O(1)
'''
