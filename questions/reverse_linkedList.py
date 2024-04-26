# reverse a linked list ?

'''
we can iterate through the list while changing the pointers to reverse the direction of the links. 

time complexity: O(n)
space complexity: O(1)
'''

class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def reverse_linked_list(head):
    prev = None
    current = head

    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    return prev

# Function to print the linked list
def print_linked_list(head):
    current = head
    while current is not None:
        print(current.value, end=" -> ")
        current = current.next
    print("None")

# Example usage:
# Creating a linked list: 1 -> 2 -> 3 -> 4 -> None
node4 = ListNode(4)
node3 = ListNode(3, node4)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)

print("Original linked list:")
print_linked_list(node1)

reversed_head = reverse_linked_list(node1)
print("\nReversed linked list:")
print_linked_list(reversed_head)

