tasks = []

def add_task(task):
    if task not in tasks:
        if len(task) > 3:
            tasks.append(task)
            print("Task added successfully.")
        else:
            print("Enter valid task")
    else:
        print("Task already exists.")

def delete_task(index):
    if index >= 0 and index < len(tasks):
        deleted_task = tasks.pop(index)
        print(f"Deleted task: {deleted_task}")
    else:
        print("Invalid index.")

def clear_task():
    tasks.clear()
    
def edit_task(index, new_task):
    if index >= 0 and index < len(tasks):
        tasks[index] = new_task
        print("Task edited successfully.")
    else:
        print("Invalid index.")

def display_tasks():
    if tasks:
        print("Tasks:")
        for i, task in enumerate(tasks):
            print(f"{i+1}. {task}")
    else:
        print("No tasks found.")

while True:
    command = input("Enter a command (add/delete/edit/clear/display/quit): ").lower()

    if command == "add":
        task = input("Enter the task: ").capitalize()
        add_task(task)
    elif command == "delete":
        index = int(input("Enter the index of the task to delete: ")) - 1
        delete_task(index)
    elif command == "edit":
        index = int(input("Enter the index of the task to edit: ")) - 1
        new_task = input("Enter the new task: ").capitalize()
        edit_task(index, new_task)
    elif command == "clear":
        clear = input("Are you sure you want to clear whole list? (y - yes/ n - no): ")
        if clear == 'y':
            clear_task()
            print('List has been cleared')
        elif clear == 'n':
            print('List is intact')
        else:
            print('Input correct value')
    elif command == "display":
        display_tasks()
    elif command == "quit":
        print("Exiting the program.")
        break
    else:
        print("Invalid command. Please try again.")