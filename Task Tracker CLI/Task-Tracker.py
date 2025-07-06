import sys
import json
import os
from datetime import datetime
from prettytable import PrettyTable

TASKS_FILE = 'tasks_py.json'


def load_tasks():
    try:
        with open(TASKS_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []


def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)


def get_time_stamp():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')


def create_id():
    tasks = load_tasks()
    return max([task['id'] for task in tasks], default=0) + 1


def add_task(desc):
    tasks = load_tasks()
    task = {
        'id': create_id(),
        'description': desc,
        'status': 'todo',
        'created_at': get_time_stamp(),
        'updated_at': get_time_stamp()
    }
    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully with ID:", task['id'])


def delete_task(task_id):
    tasks = load_tasks()
    new_tasks = [task for task in tasks if task['id'] != task_id]
    if len(tasks) == len(new_tasks):
        print("Task not found.")
    else:
        save_tasks(new_tasks)
        print("Task deleted successfully.")


def update_task(task_id, updated_desc):
    tasks = load_tasks()
    found = False
    for task in tasks:
        if task['id'] == task_id:
            task['description'] = updated_desc
            task['updated_at'] = get_time_stamp()
            found = True
            break
    if found:
        save_tasks(tasks)
        print("Task updated successfully.")
    else:
        print("Task not found.")


def display_all_tasks():
    tasks = load_tasks()
    table = PrettyTable()
    table.field_names = ["Task_ID", "Description", "Status", "Created At", "Updated At"]
    for task in tasks:
        table.add_row([task['id'], task['description'], task['status'], task['created_at'], task['updated_at']],divider=True)
    print(table)


def display_task_by_status(filtered_status):
    tasks = load_tasks()
    table = PrettyTable()
    table.field_names = ["Task_ID", "Description", "Status", "Created At", "Updated At"]
    filtered = [task for task in tasks if task['status'] == filtered_status]
    if not filtered:
        print("No tasks found with status:", filtered_status)
        return
    for task in filtered:
        table.add_row([task['id'], task['description'], task['status'], task['created_at'], task['updated_at']],divider=True)
    print(table)


def mark_task(task_id, status):
    tasks = load_tasks()
    found = False
    for task in tasks:
        if task['id'] == task_id:
            task['status'] = status
            task['updated_at'] = get_time_stamp()
            found = True
            break
    if found:
        save_tasks(tasks)
        print("Task status updated to:", status)
    else:
        print("Task not found.")


def main():
    if len(sys.argv) < 2:
        print("Usage:\n  add <desc>\n  delete <id>\n  update <id> <desc>\n  list [status]\n  mark-in-progress <id>\n  mark-done <id>")
        sys.exit(1)

    command = sys.argv[1].lower()

    try:
        match command:
            case "add":
                if len(sys.argv) < 3:
                    print("Please provide the task description")
                else:
                    add_task(sys.argv[2])

            case "delete":
                if len(sys.argv) < 3:
                    print("Please provide the task ID")
                else:
                    delete_task(int(sys.argv[2]))

            case "update":
                if len(sys.argv) < 4:
                    print("Please provide task ID and new description")
                else:
                    update_task(int(sys.argv[2]), sys.argv[3])

            case "list":
                if len(sys.argv) == 2:
                    display_all_tasks()
                else:
                    status = sys.argv[2]
                    display_task_by_status(status)

            case "mark-in-progress":
                if len(sys.argv) < 3:
                    print("Please provide the task ID")
                else:
                    mark_task(int(sys.argv[2]), "in-progress")

            case "mark-done":
                if len(sys.argv) < 3:
                    print("Please provide the task ID")
                else:
                    mark_task(int(sys.argv[2]), "done")

            case _:
                print("Invalid command")

    except ValueError:
        print("Invalid input (ID should be an integer)")


if __name__ == '__main__':
    main()
