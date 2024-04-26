'''
Odd-Even-Transform Problem works on an array of integers (both positive, negative, and zero), by taking in a value (a whole number) that
specifies the number of times the transformation has to be applied.

On an array of integers, the transformation that n number of times needs to occur:
- Adds three (+3) to each odd integer.
- Subtracts three (-3) from each even integer.

Example:
[3, 4, 9] means the array with integers 3, 4, 9 has to undergo transformation 3 times.
[3, 4, 9] -> [6, 1, 12] -> [3, 4, 9] -> [6, 1, 12], 
So the result is [6, 1, 12].
'''

# Solution:

'''
To solve this problem in Python, you can iterate through the array of integers 
and apply the specified transformation for the given number of times. 

In this code:
    1. The function odd_even_transform takes two arguments: arr (the array of integers) and n (the number of times the transformation needs to be applied).
    2. It iterates n times to apply the transformation.
    3. Within each iteration, it iterates through the array arr and checks if each element is even or odd.
    4. For even elements, it subtracts 3, and for odd elements, it adds 3.
    5. Finally, it returns the transformed array.

time complexity is O(n * m), where n is the number of times the transformation needs to be applied, and m is the length of the input array.

space complexity is O(1)
'''

def odd_even_transform(arr, n):
    for _ in range(n):
        for i in range(len(arr)):
            if arr[i] % 2 == 0:  # Even number
                arr[i] -= 3
            else:  # Odd number
                arr[i] += 3
    return arr

# Example usage:
arr = [3, 4, 9]
transformed_arr = odd_even_transform(arr, 3)
print("Transformed array:", transformed_arr)

# optimized solution:
'''
We can optimize the solution by realizing that we don't need to iterate through 
the array multiple times to apply the transformation. Instead, we can apply the 
transformation directly (using list comprehension) to each element of the array based on whether it's even or odd.

we can directly applies the transformation to each element of the array using 
list comprehension within a single iteration. 
It avoids multiple iterations over the array, resulting in improved efficiency.

time complexity is O(m), where m is the length of the input array.
space complexity is O(m), where m is the length of the input array.
'''

def odd_even_transform(arr, n):
    for _ in range(n):
        arr = [(num + 3) if num % 2 != 0 else (num - 3) for num in arr]
    return arr

# Example usage:
arr = [3, 4, 9]
transformed_arr = odd_even_transform(arr, 3)
print("Transformed array:", transformed_arr)

