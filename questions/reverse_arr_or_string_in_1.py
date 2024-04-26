# reverse a array in O(1) space
def reverse_array(arr):
    arr[:] = arr[::-1]

# Example usage:
input_array = [1, 2, 3, 4, 5]
print("Original array:", input_array)
reverse_array(input_array)
print("Reversed array:", input_array)


def reverse_array(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        # Swap elements at left and right indices
        arr[left], arr[right] = arr[right], arr[left]
        # Move left pointer to the right
        left += 1
        # Move right pointer to the left
        right -= 1

# Example usage:
input_array = [1, 2, 3, 4, 5]
print("Original array:", input_array)
reverse_array(input_array)
print("Reversed array:", input_array)


# reverse a String in O(1) space

def reverse_string(input_string):
    # Convert the string to a list of characters
    char_list = list(input_string)
    
    # Initialize pointers for swapping
    left = 0
    right = len(char_list) - 1
    
    # Swap characters from the ends towards the middle
    while left < right:
        char_list[left], char_list[right] = char_list[right], char_list[left]
        left += 1
        right -= 1
    
    # Convert the list of characters back to a string
    reversed_string = ''.join(char_list)
    
    return reversed_string

# Example usage:
input_string = "hello world"
reversed_string = reverse_string(input_string)
print("Original string:", input_string)
print("Reversed string:", reversed_string)

