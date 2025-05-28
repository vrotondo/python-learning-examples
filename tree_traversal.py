# Instructions
# You will define a simple Node class, construct a binary tree representing an organization chart, and implement traversal methods to explore the structure.

# Define Node
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Implement four traversal methods
    # Pre-order: Node ➝ Left ➝ Right
    def pre_order(node):
        if node:
            print(node.value)
            pre_order(node.left)
            pre_order(node.right)

    # In-order: Left ➝ Node ➝ Right
    def in_order(node):
        if node:
            in_order(node.left)
            print(node.value)
            in_order(node.right)

    # Post-order: Left ➝ Right ➝ Node
    def post_order(node):
        if node:
            post_order(node.left)
            post_order(node.right)
            print(node.value)

    # Level-order (Breadth-First): Top-down, left-to-right
    from collections import deque

    def level_order(root):
        if not root:
            return
        queue = deque([root])
        while queue:
            current = queue.popleft()
            print(current.value)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

root = Node("CEO")
root.left = Node("CTO")
root.right = Node("CFO")
root.left.left = Node("DevMgr")
root.left.right = Node("QA")
root.right.right = Node("Finance")

if __name__ == "__main__":
	print("Pre-order Traversal:")
	pre_order(root)

	print("\nIn-order Traversal:")
	in_order(root)

	print("\nPost-order Traversal:")
	post_order(root)

	print("\nLevel-order Traversal:")
	level_order(root)