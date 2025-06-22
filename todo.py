import argparse
import json
import os

DATA_FILE = "todos.json"

def load_todos():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return []

def save_todos(todos):
    with open(DATA_FILE, 'w') as f:
        json.dump(todos, f)

def add_task(description):
    todos = load_todos()
    todos.append({
        "id": len(todos) + 1,
        "description": description,
        "completed": False
    })
    save_todos(todos)
    print(f"✅ Added: {description}")

def list_tasks():
    todos = load_todos()
    if not todos:
        print("No tasks found!")
        return
    
    print("\n📝 Your To-Do List:")
    for task in todos:
        status = "✓" if task["completed"] else " "
        print(f"{task['id']}. [{status}] {task['description']}")

def complete_task(task_id):
    todos = load_todos()
    for task in todos:
        if task["id"] == task_id:
            task["completed"] = True
            save_todos(todos)
            print(f"🎉 Completed task #{task_id}")
            return
    print(f"❌ Task #{task_id} not found")

def delete_task(task_id):
    todos = load_todos()
    todos = [task for task in todos if task["id"] != task_id]
    save_todos(todos)
    print(f"🗑️ Deleted task #{task_id}")

def main():
    parser = argparse.ArgumentParser(description="To-Do List Manager")
    subparsers = parser.add_subparsers(dest="command")

    # Add command
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("description", help="Task description")

    # List command
    subparsers.add_parser("list", help="List all tasks")

    # Complete command
    complete_parser = subparsers.add_parser("complete", help="Mark task as complete")
    complete_parser.add_argument("task_id", type=int, help="ID of task to complete")

    # Delete command
    delete_parser = subparsers.add_parser("delete", help="Delete a task")
    delete_parser.add_argument("task_id", type=int, help="ID of task to delete")

    args = parser.parse_args()

    if args.command == "add":
        add_task(args.description)
    elif args.command == "list":
        list_tasks()
    elif args.command == "complete":
        complete_task(args.task_id)
    elif args.command == "delete":
        delete_task(args.task_id)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
