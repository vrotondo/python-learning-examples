import argparse

def complete_task(args):
    task = Task(args.title)
    task.complete()

parser = argparse.ArgumentParser(description="Task CLI")
subparsers = parser.add_subparsers()

complete_parser = subparsers.add_parser("complete", help="Complete a task")
complete_parser.add_argument("title", help="Title of the Task")
complete_parser.set_defaults(func=complete_task)

args = parser.parse_args()

class Task:
    def __init__(self, title):
        self.title = title
        self.completed = False
    def complete(self):
        self.completed = True
        print(f"✅ Task '{self.title}' marked as complete.")

class User:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)