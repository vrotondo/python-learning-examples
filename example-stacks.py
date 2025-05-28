# Initialize the stack
undo_stack = []

# Perform actions and push to stack
def perform_action(action):
	undo_stack.append(action)
	print(f"Action performed: {action}")

# Undo the last action
def undo():
    if undo_stack:
        last_action = undo_stack.pop()
        print(f"Undoing action: {last_action}")
    else:
        print("No actions to undo.")

# Example usage
perform_action("Typed 'Hello'")
perform_action("Bolded text")
undo()  # Undo: Bolded text
undo()  # Undo: Typed 'Hello'
undo()  # No actions to undo