# How to implement custom Stack classes and run operations to visualize how Stack behaves in memory.

# Define class
class Stack:
    # Initialize stack with empty list
    def __init__(self):
        self.items = []
    # Add push() method to add element to the top of the stack
    def push(self, item):
        self.items.append(item)
        print(f"Pushed {item} to stack: {self.items}")
    # Add a pop() method to remove and return the top item from the stack
    def pop(self):
        if not self.is_empty():
            removed = self.items.pop()
            print(f"Popped {removed} from stack: {self.items}")
            return removed
        else:
            print("Stack is empty. Nothing to pop.")
            return None
    # Add a peek() method to see the item at the top of the stack
    def peek(self):
        if not self.is_empty():
            print(f"Top of stack is: {self.items[-1]}")
            return self.items[-1]
        else:
            print("Stack is empty. No top element.")
            return None
    # Add a helper method is_empty() to check if the stack is empty
    def is_empty(self):
        return len(self.items) == 0
# Add a test section at the bottom of the file using if __name__ == "__main__" Here, you’ll create a stack, push items, pop some, and peek at the top.
if __name__ == "__main__":
    stack = Stack()
    stack.push("Task 1")
    stack.push("Task 2")
    stack.push("Task 3")

    stack.peek()

    stack.pop()
    stack.pop()
    stack.pop()
    stack.pop()  # Try popping from empty stack

        