# A simple method to sort an array of integers in ascending and descending order.

'''
# Explaination: built-in sort() method for Python lists to sort arrays of integers 
    in both ascending and descending order. Here's how you can do it:
    time complexity: O(nlogn) 
    space complexity is O(n)
'''

# Sample array of integers
arr = [5, 2, 9, 1, 7]

# Sorting in ascending order
arr_asc = sorted(arr)

# Sorting in descending order
arr_desc = sorted(arr, reverse=True)

print("Original array:", arr)
print("Ascending order:", arr_asc)
print("Descending order:", arr_desc)

# Solution: Bubble sort
'''
solve without built-in functions

Ascending Order (Bubble Sort):
    time complexity: O(n^2) 
    space complexity is O(1)
'''
def bubble_sort_asc(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Sample array of integers
arr = [5, 2, 9, 1, 7]

# Sorting in ascending order
bubble_sort_asc(arr)
print("Ascending order:", arr)

'''
Descending Order (Bubble Sort with reverse comparison):
'''

def bubble_sort_desc(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Sample array of integers
arr = [5, 2, 9, 1, 7]

# Sorting in descending order
bubble_sort_desc(arr)
print("Descending order:", arr)

