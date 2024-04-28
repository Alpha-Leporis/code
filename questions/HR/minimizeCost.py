'''
1. Reduce the Array

Given an integer array, reduce the array to a single
element.

In each operation, pick two indices i and j (where i !=
J), and:
• append the value of a[i] + a[j] to the array
• delete a[i] and a[J] from the array

The cost of each operation is a[i] + a[j]. Find the
minimum possible cost to reduce the array.

Example
Consider array [25,10,20].

• Pick 10 and 20, cost = 10+20 => 30, array' = [25,30]
• Pick 25 and 30, cost = 25+30 => 55, array" = [55]

The cost is 30+55 = 85. This is the minimum
possible cost.

Function Description
Complete the function minimizeCost in the editor.

minimizeCost has the following parameter :

'''

# Solution:
'''
We can solve this problem using a priority queue (min-heap) data structure.

This code first converts the input array into a min-heap. Then, in each iteration, 
it extracts the two smallest elements from the heap, calculates the cost, 
adds it to the total, and pushes the sum back into the heap. It continues 
this process until there is only one element left in the heap, returning the total cost.

time complexity is O(n log n) + O(n) = O(n log n).  -->  heap takes O(log n) and min-heap takes O(n),
   and while loop is O(n log n).
space complexity is O(n).
'''

import heapq

def minimizeCost(arr):
    # Convert the array into a min-heap
    heapq.heapify(arr)
    
    total_cost = 0
    
    # Continue until there is only one element left in the heap
    while len(arr) > 1:
        # Extract the two smallest elements
        smallest1 = heapq.heappop(arr)
        smallest2 = heapq.heappop(arr)
        
        # Calculate the cost and add it to the total
        cost = smallest1 + smallest2
        total_cost += cost
        
        # Append the new element (sum) back to the heap
        heapq.heappush(arr, cost)
    
    return total_cost

# Example usage:
arr = [25, 10, 20]
print(minimizeCost(arr))  # Output should be 85

'''
Above code Explanation:

    1. The heapq module is imported, which provides functions to create and manipulate heaps.

    2. The minimizeCost function takes an array arr as input and returns the minimum possible cost to reduce the array to a single element.

    3. Inside the function:

        1. The input array arr is converted into a min-heap using heapq.heapify(arr). This operation rearranges the elements of the array into a heap such that the smallest element is at the root.

        2. A variable total_cost is initialized to 0 to store the total cost of reducing the array.

        3. The function enters a while loop that continues until there is only one element left in the heap (i.e., until len(arr) becomes 1).

        4. Inside the loop:

            4.1 The two smallest elements are extracted from the heap using heapq.heappop(arr), assigning them to smallest1 and smallest2.

            4.2 The cost of combining these two smallest elements is calculated by adding them together and stored in the variable cost.

            4.3 The calculated cost is added to the total_cost.

            4.4 The sum of the two smallest elements (cost) is pushed back into the heap using heapq.heappush(arr, cost).

    4. Once the while loop exits (when there is only one element left in the heap), the function returns the total_cost, which represents the minimum possible cost to reduce the array to a single element.

    5. An example usage of the minimizeCost function is demonstrated by creating an array arr = [25, 10, 20] and printing the result of calling the function with this array (print(minimizeCost(arr))). In this example, the expected output is 85, as explained in the comment.
'''

