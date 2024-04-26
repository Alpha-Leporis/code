# If we are playing a game where in a list if we are asked to remove a value from list on 3rd position on circular fashion what will be the last element left

'''
This problem is commonly known as the Josephus problem, where a group of people stand in a circle and every nth person is eliminated until only one person remains. In your case, instead of people, you have a list of values, and you are removing every 3rd value in a circular fashion until only one value remains.

To solve this problem, you can use a circular linked list or simulate the elimination process iteratively. Here's how you can do it using Python:
'''

def find_last_element(values, k):
    # Initialize index to start removal process
    index = 0

    # Repeat until there is only one element left in the list
    while len(values) > 1:
        # Calculate the index of the element to be removed
        index = (index + k - 1) % len(values)
        
        # Remove the element at the calculated index
        values.pop(index)

    # Return the last remaining element
    return values[0]

# Example usage
values = [1, 2, 3, 4, 5, 6, 7]
k = 3
last_element = find_last_element(values, k)
print("Last element left in the list:", last_element)


'''
TC =  O(n * k), number of elements in the input list (n) and the value of k
SC = O(n)
In this example, the find_last_element function takes a list of values (values) and the value of k,
which represents the step size for removal (in this case, every 3rd value).
It iteratively removes every k-th value from the list in a circular fashion until only one value remains.
Finally, it returns the last remaining value.
'''

# optijmized solution:
'''
The Josephus problem has a well-known solution:
    For a circle of nn elements, the survivor position is denoted by f(n,k)f(n,k), where kk is the step size.
    The recurrence relation for the Josephus problem is f(n,k)=(f(n-1,k)+k) mod n with base case f(1,k)=0.

Using this formula, we can directly calculate the position of the last survivor without simulating the removal process. Here's how we can implement this optimization:

In this optimized solution, we directly calculate the survivor position using the Josephus formula without the need for iterative removal.
The time complexity of this solution is O(n), where n is the number of elements in the circle, and the space complexity is O(1),
as we only store a single variable. 
This approach significantly improves the efficiency of the solution compared to the iterative removal method.

TC =  O(n), number of elements in the input list (n)
SC = O(1)

'''

def find_last_element(n, k):
    # Initialize the survivor position for a single element circle
    survivor = 0

    # Iterate through all elements in the circle
    for i in range(2, n + 1):
        survivor = (survivor + k) % i

    # Return the survivor position
    return survivor + 1  # Adjust for 0-based indexing

# Example usage
n = 7  # Number of elements in the list
k = 3  # Step size for removal
last_element = find_last_element(n, k)
print("Last element left in the list:", last_element)
