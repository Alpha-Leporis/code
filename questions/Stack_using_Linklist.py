'''
Implement Stack using Linklist.
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        if self.top is None:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        else:
            popped = self.top.data
            self.top = self.top.next
            return popped

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        else:
            return self.top.data

    def is_empty(self):
        return self.top is None

    def display(self):
        current = self.top
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

# Example usage:
stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)

stack.display()  # Output: 3 2 1

print("Popped:", stack.pop())  # Output: Popped: 3

print("Peek:", stack.peek())  # Output: Peek: 2

stack.display()  # Output: 2 1
