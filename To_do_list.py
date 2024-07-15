def display_menu():
    print("\nTo-Do List Application")
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Mark Task as Complete")
    print("4. Remove Task")
    print("5. Exit")


def view_tasks(tasks):
    print("\nTo-Do List:")
    if not tasks:
        print("No tasks found.")
    else:
        for i, task in enumerate(tasks, start=1):
            status = "Complete" if task['complete'] else "Incomplete"
            print(f"{i}. {task['description']} [{status}]")


def add_task(tasks):
    description = input("Enter the task description: ")
    tasks.append({'description': description, 'complete': False})
    print("Task added.")


def mark_task_complete(tasks):
    view_tasks(tasks)
    task_number = int(input("Enter the task number to mark as complete: "))
    if 0 < task_number <= len(tasks):
        tasks[task_number - 1]['complete'] = True
        print("Task marked as complete.")
    else:
        print("Invalid task number.")


def remove_task(tasks):
    view_tasks(tasks)
    task_number = int(input("Enter the task number to remove: "))
    if 0 < task_number <= len(tasks):
        tasks.pop(task_number - 1)
        print("Task removed.")
    else:
        print("Invalid task number.")


def main():
    tasks = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            mark_task_complete(tasks)
        elif choice == '4':
            remove_task(tasks)
        elif choice == '5':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
