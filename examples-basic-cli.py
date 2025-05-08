import argparse

def add_task(args):
    print(f"✅ Task added: {args.description}")

def list_tasks(args):
    print("📋 Listing all tasks...")

parser = argparse.ArgumentParser(description="Task Manager CLI")
subparsers = parser.add_subparsers()

# Add task command
add_parser = subparsers.add_parser("add", help="Add a new task")
add_parser.add_argument("description", help="Task description")
add_parser.set_defaults(func=add_task)

# List tasks command
list_parser = subparsers.add_parser("list", help="List all tasks")
list_parser.set_defaults(func=list_tasks)

args = parser.parse_args()
args.func(args)

class Product:
    def __init__(self, name, category, quantity):
        self.name = name
        self.category = category
        self.quantity = quantity

    def restock(self, amount):
        self.quantity += amount
        print(f"Restocked {self.name}. New quantity: {self.quantity}")

# CLI command to restock
def restock_product(args):
    p = Product(args.name, args.category, args.quantity)
    p.restock(args.amount)

restock_parser = subparsers.add_parser("restock", help="Restock a product")
restock_parser.add_argument("name")
restock_parser.add_argument("category")
restock_parser.add_argument("quantity", type=int)
restock_parser.add_argument("amount", type=int)
restock_parser.set_defaults(func=restock_product)