# Define an empty list to store tasks
tasks = []

# Function to display the to-do list
def display_tasks():
    if not tasks:
        print("\nYour to-do list is empty.")
    else:
        print("\nTo-Do List:")
        for i, task in enumerate(tasks, start=1):
            status = "Done" if task["completed"] else "Not Done"
            print(f"{i}. {task['task']} ({status})")

# Function to add a task to the to-do list
def add_task(task_name):
    task = {"task": task_name, "completed": False}
    tasks.append(task)
    print(f"\nTask '{task_name}' has been added to your to-do list.")

# Function to mark a task as completed
def mark_completed(task_number):
    if 1 <= task_number <= len(tasks):
        tasks[task_number - 1]["completed"] = True
        print(f"\nTask {task_number} has been marked as completed.")
    else:
        print("\nInvalid task number. Please enter a valid task number.")

# Function to remove a task from the to-do list
def remove_task(task_number):
    if 1 <= task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        print(f"\nTask '{removed_task['task']}' has been removed from your to-do list.")
    else:
        print("\nInvalid task number. Please enter a valid task number.")

# Main program loop
def to_do_list_app():
    while True:
        print("\nOptions:")
        print("1. Display to-do list")
        print("2. Add a task")
        print("3. Mark a task as completed")
        print("4. Remove a task")
        print("5. Quit")
        
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            display_tasks()
        elif choice == '2':
            task_name = input("\nEnter the task: ").strip()
            if task_name:
                add_task(task_name)
            else:
                print("\nTask cannot be empty. Please enter a valid task name.")
        elif choice == '3':
            display_tasks()
            try:
                task_number = int(input("\nEnter the task number to mark as completed: ").strip())
                mark_completed(task_number)
            except ValueError:
                print("\nInvalid input. Please enter a number.")
        elif choice == '4':
            display_tasks()
            try:
                task_number = int(input("\nEnter the task number to remove: ").strip())
                remove_task(task_number)
            except ValueError:
                print("\nInvalid input. Please enter a number.")
        elif choice == '5':
            print("\nThank you for using the To-Do List Application. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please enter a number between 1 and 5.")

# Run the To-Do List Application
to_do_list_app()
