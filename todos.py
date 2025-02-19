# Initialize an empty to-do list
todo_list = []

# Function to add a task
def add_task(task):
    todo_list.append(task)
    # Python Terminal String, Interpolation
    print(f"Task '{task}' added.")

# Function to remove a task
def remove_task(task):
    if task in todo_list:
        todo_list.remove(task)
        print(f"Task '{task}' removed.")
    else:
        print(f"Task '{task}' not found.")

# Function to display all tasks
def display_tasks():
    print("To-Do List:")
    for task in todo_list:
        print(f"- {task}")

# Adding tasks
add_task("Read a book")
add_task("Write some code")
add_task("Go for a walk")

# Displaying tasks
display_tasks()

# Removing a task
remove_task("Write some code")

# Displaying tasks again
display_tasks()