# Define class called Queue
class Queue:
    # Initialize with empty list
    def __init__(self):
        self.items = []
    # Add push method
    def push(self, item):
        self.items.append(item)
        print(f"Pushed {item} to stack: {self.items}")
    # Added enqueue() method to add elements to the rear of the queue
    def dequeue(self):
        if not self.is_empty():
            removed = self.items.pop(0)
            print(f"Dequeued {removed} | Queue: {self.items}")
            return removed
        else:
            print("Queue is empty. Nothing to dequeue.")
            return None
    # Added peek() method to view the front item without removing it
    def peek(self):
        if not self.is_empty():
            print(f"Front of queue: {self.items[0]}")
            return self.items[0]
        else:
            print("Queue is empty. No front item.")
            return None
    # Added helper method is_empty() to check if the queue is empty
    def is_empty(self):
        return len(self.items) == 0
# Add a test block at the bottom using if __name__ == "__main__" Use this section to simulate how a queue handles tasks.
if __name__ == "__main__":
	q = Queue()

	q.enqueue("Order #1")
	q.enqueue("Order #2")
	q.enqueue("Order #3")

	q.peek()

	q.dequeue()
	q.dequeue()
	q.dequeue()
	q.dequeue()  # Try to dequeue from empty queue