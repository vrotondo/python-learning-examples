from collections import deque

# Initialize the queue
ticket_queue = deque()

# Enqueue a ticket
def add_ticket(ticket):
	ticket_queue.append(ticket)
	print(f"Ticket added: {ticket} | Queue: {list(ticket_queue)}")

# Dequeue and process the next ticket
def process_ticket():
    if ticket_queue:
        ticket = ticket_queue.popleft()
        print(f"Processing ticket: {ticket} | Remaining Queue: {list(ticket_queue)}")
    else:
        print("No tickets to process.")

# Example usage
add_ticket("Ticket #1")
add_ticket("Ticket #2")
process_ticket()
process_ticket()
process_ticket()