'''
Implementation:

    We define a TableReservationStack class with methods to interact with the stack.
    The push method adds a new reservation to the top of the stack.
    The pop method removes and returns the reservation at the top of the stack.
    The peek method returns the reservation at the top of the stack without removing it.
    The is_empty method checks if the stack is empty.
    The size method returns the number of reservations currently in the stack.

we can use this implementation to manage table reservations by pushing new reservations onto the stack and popping reservations when they are cancelled or fulfilled.

TC = O(1), time complexity of the push, pop, peek, is_empty, and size methods is O(1)
SC = O(n), where n is the number of reservations in the stack.

'''

class TableReservationStack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, reservation):
        self.stack.append(reservation)

    def pop(self):
        if self.is_empty():
            return None
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.stack[-1]

    def size(self):
        return len(self.stack)

# Example usage:
table_stack = TableReservationStack()

# Making reservations
table_stack.push("Table 1")
table_stack.push("Table 2")
table_stack.push("Table 3")

# Peek at the top reservation
print("Top reservation:", table_stack.peek())

# Cancelling the last reservation
cancelled_reservation = table_stack.pop()
print("Cancelled reservation:", cancelled_reservation)

# Check if the stack is empty
print("Is the stack empty?", table_stack.is_empty())

# Print the number of remaining reservations
print("Number of remaining reservations:", table_stack.size())


