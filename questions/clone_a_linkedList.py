# Write a function to clone a linked list

'''
To clone a linked list in Python, you need to create a new linked list where each node
has the same value as the original list but different memory addresses.

time complexity: O(n), where n is the number of nodes in the original linked list
space complexity: O(n), where nn is the number of nodes in the original linked list
'''

class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def clone_linked_list(head):
    if not head:
        return None

    # Create a dictionary to map original nodes to their clones
    node_map = {}

    # Iterate through the original list to create clones and populate the dictionary
    current = head
    while current:
        node_map[current] = ListNode(current.value)
        current = current.next

    # Reset the current pointer to the head of the original list
    current = head

    # Iterate through the original list to set the next pointers of clones
    while current:
        node_map[current].next = node_map.get(current.next)
        current = current.next

    # Return the clone of the head node
    return node_map[head]

# Function to print the linked list
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> ")
        current = current.next
    print("None")

# Example usage:
# Creating a linked list: 1 -> 2 -> 3 -> None
node3 = ListNode(3)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)

print("Original linked list:")
print_linked_list(node1)

cloned_head = clone_linked_list(node1)
print("\nCloned linked list:")
print_linked_list(cloned_head)
