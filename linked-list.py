class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next

        current.next = new_node

    def delete_node(self, value):
        if not self.head:
            return
        
        if self.head.data == value:
            self.head = self.head.next
            return
        
        current = self.head
        prev = None
        while current and current.data != value:
            prev = current
            current = current.next

        if not current:
            return
        
        prev.next = current.next

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
            print("None")

if __name__ == "__main__":
	ll = LinkedList()
	ll.insert_at_front("Node A")
	ll.insert_at_front("Node B")
	ll.insert_at_end("Node C")

	print("Initial List:")
	ll.display()

	ll.delete_node("Node B")
	print("\nAfter Deleting 'Node B':")
	ll.display()

'''
class Node:
	def __init__(self, data):
    	self.data = data
    	self.next = None

class LinkedList:
	def __init__(self):
    	self.head = None

	def insert_at_front(self, data):
    	new_node = Node(data)
    	new_node.next = self.head
    	self.head = new_node

	def insert_at_end(self, data):
    	new_node = Node(data)
    	if not self.head:
        	self.head = new_node
        	return
    	current = self.head
    	while current.next:
        	current = current.next
    	current.next = new_node

	def delete_node(self, value):
    	if not self.head:
        	return
    	if self.head.data == value:
        	self.head = self.head.next
        	return
    	current = self.head
    	prev = None
    	while current and current.data != value:
        	prev = current
        	current = current.next
    	if not current:
        	return
    	prev.next = current.next

	def display(self):
    	current = self.head
    	while current:
        	print(current.data, end=" -> ")
        	current = current.next
    	print("None")

# Example Usage
if __name__ == "__main__":
	ll = LinkedList()
	ll.insert_at_front("Node A")
	ll.insert_at_front("Node B")
	ll.insert_at_end("Node C")

	print("Initial List:")
	ll.display()

	ll.delete_node("Node B")
	print("\nAfter Deleting 'Node B':")
	ll.display()
'''