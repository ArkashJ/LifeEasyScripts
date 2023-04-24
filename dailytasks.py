import sys
import os

tasks_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tasks.txt')

def add_task(task):
    with open(tasks_file, 'a') as f:
        f.write(f"{task}\n")

def remove_task(task_id):
    tasks = get_tasks()
    if 0 < task_id <= len(tasks):
        del tasks[task_id - 1]
        with open(tasks_file, 'w') as f:
            for task in tasks:
                f.write(f"{task}\n")
    else:
        print("Invalid task ID.")

def get_tasks():
    with open(tasks_file, 'r') as f:
        tasks = [task.strip() for task in f.readlines()]
    return tasks

def list_tasks():
    tasks = get_tasks()
    print("Tasks:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: tasks.py [add|remove|list] [task]")
        sys.exit(1)

    command = sys.argv[1]

    if command == "add":
        task = ' '.join(sys.argv[2:])
        if task:
            add_task(task)
            print(f"Task added: {task}")
        else:
            print("Error: Please provide a task description.")
    elif command == "remove":
        if len(sys.argv) > 2:
            try:
                task_id = int(sys.argv[2])
                remove_task(task_id)
                print(f"Task {task_id} removed.")
            except ValueError:
                print("Error: Please provide a valid task ID.")
        else:
            print("Error: Please provide a task ID to remove.")
    elif command == "list":
        list_tasks()
    else:
        print("Error: Invalid command. Use 'add', 'remove', or 'list'.")
