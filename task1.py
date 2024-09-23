tasks = []

while True:
    print("1. Add Task")
    print("2. View All Tasks")
    print("3. Update Task")
    print("4. Mark Task as Completed")
    print("5. Delete Task")
    print("6. Search Task by Name")
    print("7. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        # Add Task
        task_name = input("Enter task name: ")
        task_description = input("Enter task description: ")
        task_due_date = input("Enter task due date: ")
        task_priority = input("Enter task priority (High, Medium, Low): ")
        task_completed = False

        task = {
            "name": task_name,
            "description": task_description,
            "due_date": task_due_date,
            "priority": task_priority,
            "completed": task_completed
        }

        tasks.append(task)
        print("Task added successfully.")

    elif choice == "2":
        # View All Tasks
        if not tasks:
            print("No tasks available.")
        else:
            for task in tasks:
                print("Task:")
                print("Name: " + task["name"])
                print("Description: " + task["description"])
                print("Due Date: " + task["due_date"])
                print("Priority: " + task["priority"])
                print(f"Completed: {'Yes' if task['completed'] else 'No'}")
                print()

    elif choice == "3":
        # Update Task
        task_name = input("Enter the name of the task to update: ")
        for task in tasks:
            if task["name"] == task_name:
                task["name"] = input("Enter new task name: ")
                task["description"] = input("Enter new task description: ")
                task["due_date"] = input("Enter new task due date: ")
                task["priority"] = input("Enter new task priority (High, Medium, Low): ")
                print("Task updated successfully.")
                break
        else:
            print("Task not found.")

    elif choice == "4":
        # Mark Task as Completed
        task_name = input("Enter the name of the task to mark as completed: ")
        for task in tasks:
            if task["name"] == task_name:
                task["completed"] = True
                print("Task marked as completed.")
                break
        else:
            print("Task not found.")

    elif choice == "5":
        # Delete Task
        task_name = input("Enter the name of the task to delete: ")
        for task in tasks:
            if task["name"] == task_name:
                tasks.remove(task)
                print("Task deleted successfully.")
                break
        else:
            print("Task not found.")

    elif choice == "6":
        # Search Task by Name
        task_name = input("Enter the name of the task to search: ")
        for task in tasks:
            if task["name"] == task_name:
                print("Task found:")
                print("Name: " + task["name"])
                print("Description: " + task["description"])
                print("Due Date: " + task["due_date"])
                print("Priority: " + task["priority"])
                print(f"Completed: {'Yes' if task['completed'] else 'No'}")
                break
        else:
            print("Task not found.")

    elif choice == "7":
        # Exit
        print("Exiting the program")
        break
    else:
        print("Invalid option. Please try again.")
