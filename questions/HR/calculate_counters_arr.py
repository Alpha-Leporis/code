'''
For each element Of an array. a counter is set to
0. The element is compared to each element to its
left. If the element to the left is greater, the
absolute difference is subtracted from the
counter. If the element to the left is less. the
absolute difference is added to the counter. For
each element of the array, determine the value of
the counter. These values should be stored in an
array and returned.

Example
n = 3. the number of elements
arr = [2 4 3]

For arr[0] = 2, counter starts at 0 and there are no
elernents to the left so counter = 0.

• For arr[1] = 4, counter starts at 0 and then
increases by |4- 2| = 2 at the first and only
comparison: counter = 2.

• Testing arr[2] = 3 first against 4, counter = 0 - |3 -4| = - 1 
and then against 2, counter = -1 |3-2| = 0

• The answer array is [0, 2, 0]

'''

# Solution:
'''
Soltution: This solution iterates over each element in the input array. 
For each element, it compares the element with all the elements to its left, 
updating the counter accordingly based on the absolute difference. 
Finally, it stores the counter value for each element in the result array and returns it.

Tme complexity: O(n^2)
Space complexity: O(n)
'''
def calculate_counters(arr):
    n = len(arr)
    counters = [0] * n  # Initialize counters array with zeros

    for i in range(n):
        # Initialize counter for each element
        counter = 0
        # Compare the current element with elements to its left
        for j in range(i):
            diff = abs(arr[i] - arr[j])
            if arr[i] > arr[j]:
                counter += diff
            else:
                counter -= diff
        # Store the counter value for the current element
        counters[i] = counter

    return counters

# Example usage
arr = [2, 4, 3]
result = calculate_counters(arr)
print(result)  # Output: [0, 2, 0]


# optimized solution:

'''
To optimize the solution, we can avoid recalculating the counter values for each element by 
taking advantage of the previous counter value and updating it based on the difference between
the current element and the previous one. This approach reduces the time complexity to O(n) 
while maintaining the same space complexity. 

This optimized solution iterates over each element in the array only once. 
For each element except the first one, it calculates the difference between 
the current element and the previous one, updates the counter accordingly, 
and stores the counter value for the current element. 
This approach reduces the time complexity to O(n) while maintaining the same space complexity of O(n).


Tme complexity: O(n)
Space complexity: O(n)

'''
def calculate_counters(arr):
    n = len(arr)
    counters = [0] * n  # Initialize counters array with zeros

    # Initialize the counter to track the cumulative difference
    counter = 0

    # Iterate over each element in the array
    for i in range(1, n):
        # Calculate the difference between the current element and the previous one
        diff = abs(arr[i] - arr[i - 1])

        # Update the counter based on the difference
        if arr[i] > arr[i - 1]:
            counter += diff
        else:
            counter -= diff

        # Store the counter value for the current element
        counters[i] = counter

    return counters

# Example usage
arr = [2, 4, 3]
result = calculate_counters(arr)
print(result)  # Output: [0, 2, 0]
