# remove duplicate in an array
#Solution:
def remove_duplicates(arr):
    return list(set(arr))

# Example usage:
input_array = [1, 2, 3, 3, 4, 5, 5, 6]
print("Input array:", input_array)
print("Array after removing duplicates:", remove_duplicates(input_array))


#solution:
def remove_duplicates(arr):
    unique_elements = {}
    result = []

    for item in arr:
        if item not in unique_elements:
            result.append(item)
            unique_elements[item] = True

    return result

# Example usage:
input_array = [1, 2, 3, 3, 4, 5, 5, 6]
print("Input array:", input_array)
print("Array after removing duplicates:", remove_duplicates(input_array))
'''
time complexity: O(n)
space complexity: O(m), where m is the number of unique elements in the array.
'''