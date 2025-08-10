# Simple To-Do List App
FILENAME = "tasks.txt"

def load_tasks():
    try:
        with open(FILENAME, "r") as file:
            return [line.strip() for line in file]
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(FILENAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def show_tasks(tasks):
    if not tasks:
        print("\nNo tasks found.")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def main():
    tasks = load_tasks()
    while True:
        print("\n--- To-Do List Menu ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            task = input("Enter new task: ")
            tasks.append(task)
            save_tasks(tasks)
        elif choice == "3":
            show_tasks(tasks)
            try:
                task_num = int(input("Enter task number to delete: "))
                tasks.pop(task_num - 1)
                save_tasks(tasks)
            except (ValueError, IndexError):
                print("Invalid task number!")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
