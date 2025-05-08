import argparse

def add_task(args):
    print(f"✅ Task added: {args.description}")

parser = argparse.ArgumentParser(description="Task Manager CLI")
subparsers = parser.add_subparsers()

# Add command
add_parser = subparsers.add_parser("add", help="Add a new task")
add_parser.add_argument("description", help="Description of the task")
add_parser.set_defaults(func=add_task)

args = parser.parse_args()

# Check if a subcommand was provided
if hasattr(args, "func"):
    args.func(args)
else:
    parser.print_help()  # Show help message if no subcommand is provided