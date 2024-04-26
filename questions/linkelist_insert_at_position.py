
# insert a node in linkedlist at given position

'''
time complexity is O(n)
space complexity is O(1)
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insert_at_position(head, data, position):
    new_node = Node(data)

    # If the position is 0 or the list is empty, insert at the beginning
    if position == 0 or head is None:
        new_node.next = head
        return new_node

    # Traverse the list to find the position
    current = head
    for _ in range(position - 1):
        if current.next is None:
            break
        current = current.next

    # Insert the new node at the given position
    new_node.next = current.next
    current.next = new_node

    return head
