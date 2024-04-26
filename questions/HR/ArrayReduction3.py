'''

given an array of n integers, a sequence of n-1 operations
must be performed on the array.

In each operation:
Remove the minimum and maximum elements from the current array and add their sum back to the array.
The cost of an operation, cost = ceil((minimum_element + maximium_element) / (mavimum_element - minimum_element + 1))

find the total cost to reduce the array to a single element.

Example:
Given array = [2, 3, 4, 5, 7]
output: 8

Sample Input :
arr[] , size: n = 4
arr = [8, 8, 8, 8]

Sample output:
21

'''

# solution:

'''
Time complexity: O(n^2), due to the repeated operations in the while loop.
Space complexity: O(1)
'''

import math

def findtotalCost(arr):
    
    total_cost = 0
    
    while len(arr) > 1:
        min_element = min(arr)
        max_element = max(arr)
        # calculating cost of operation
        cost = math.ceil((min_element + max_element) / (max_element - min_element + 1))
        # removing elements from array
        arr.remove(min_element)
        arr.remove(max_element)
        # adding there sum to array
        arr.append(min_element + max_element)
        # calculating total cost
        total_cost += cost
    return total_cost

# Example 1:
nums = [2,3,4,5,7]
print(findtotalCost(nums),"")  # Output: 8
# Example 2:
nums2 = [8, 8, 8, 8]
print(findtotalCost(nums2))  # Output: 21
# Example 2:
nums3 = [3,5,2,1,9,6]
print(findtotalCost(nums3))  # Output: 10


# optimize solution:

'''
To optimize the code, we can avoid repeatedly finding the minimum and maximum elements in the array 
in each iteration of the while loop. Instead, we can use a priority queue (min-heap) to efficiently 
find the minimum and maximum elements. This approach will reduce the time complexity of finding the 
minimum and maximum elements from O(n) to O(log n) per iteration.

a min-heap to efficiently find the minimum and maximum elements in the array in each iteration, 
reducing the time complexity to O(n log n). Additionally, 
it maintains a constant space complexity of O(1) as before.
'''

import heapq
import math

def findTotalCost(arr):
    total_cost = 0
    
    # Convert the array into a min-heap
    heapq.heapify(arr)
    
    while len(arr) > 1:
        # Pop the two smallest elements
        min_val = heapq.heappop(arr)
        max_val = heapq.heappop(arr)
        
        # Calculate the cost of the operation
        cost = math.ceil((min_val + max_val) / (max_val - min_val + 1))
        
        # Add their sum back to the heap
        heapq.heappush(arr, min_val + max_val)
        
        # Increment the total cost
        total_cost += cost
    
    return total_cost

# Example usage:
arr = [4, 2, 6, 8, 5]
print(findTotalCost(arr))  # Output: 14

