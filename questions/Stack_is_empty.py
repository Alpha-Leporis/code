'''
Check wheather the stack is empty or not with out using any other variable or inbuilt functions.
'''

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():  # Check if the stack is not empty
            return self.items.pop()
        else:
            raise IndexError("Stack is empty")

    def is_empty(self):
        return not self.items  # Check if the list of items is empty


# Example usage:
stack = Stack()
stack.push(1)
stack.push(2)

stack.is_empty()

try:
    while True:
        print(stack.pop())
except IndexError as e:
    print(e)  # Output: Stack is empty

stack.is_empty()
