# kth largest element in an array

'''
we can find the kth largest element in an array in linear time using a variation of the quickselect algorithm

time complexity :O(n), where n is the length of the array,
space complexity: O(n)
'''

import random

def partition(nums, low, high):
    pivot = nums[high]
    i = low - 1
    for j in range(low, high):
        if nums[j] <= pivot:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
    nums[i + 1], nums[high] = nums[high], nums[i + 1]
    return i + 1

def quickselect(nums, low, high, k):
    if low == high:
        return nums[low]

    pivot_index = random.randint(low, high)
    nums[pivot_index], nums[high] = nums[high], nums[pivot_index]
    pivot_index = partition(nums, low, high)

    if k == pivot_index:
        return nums[k]
    elif k < pivot_index:
        return quickselect(nums, low, pivot_index - 1, k)
    else:
        return quickselect(nums, pivot_index + 1, high, k)

def find_kth_largest(nums, k):
    if not nums or k < 1 or k > len(nums):
        return None
    return quickselect(nums, 0, len(nums) - 1, len(nums) - k)

# Example usage:
nums = [3, 2, 1, 5, 6, 4]
k = 2
print("The {}th largest element is: {}".format(k, find_kth_largest(nums, k)))
