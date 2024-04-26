'''
# Given a linked list, determine if it has a cycle.

we can determine if a linked list has a cycle by using the "slow and fast pointers" technique. 
Essentially, you have two pointers moving through the list at different speeds. 
If there is a cycle in the list, the faster pointer will eventually catch up to the slower pointer.

In this code:
    1. We define a ListNode class to represent nodes in the linked list.
    2. The has_cycle function takes the head of the linked list as input and returns True if the linked list contains a cycle, and False otherwise.
    3. We initialize two pointers, slow and fast, both starting from the head of the linked list. The slow pointer moves one step at a time while the fast pointer moves two steps at a time.
    4. If there's a cycle, the fast pointer will eventually catch up to the slow pointer.
    5. We return True if the pointers meet, indicating the presence of a cycle, and False if the fast pointer reaches the end of the list, indicating no cycle.

'''

class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

def has_cycle(head):
    if not head or not head.next:
        return False
    
    slow = head
    fast = head.next

    while fast and fast.next:
        if slow == fast:
            return True
        slow = slow.next
        fast = fast.next.next

    return False

# Example usage:
# Construct a linked list with a cycle
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = head  # Creating a cycle

# Check if the linked list has a cycle
if has_cycle(head):
    print("The linked list has a cycle.")
else:
    print("The linked list does not have a cycle.")
