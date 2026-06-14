import os  # os module has been imported that helps Python interact with operating system

tasks = []  # TASK LIST - An empty list


def load_tasks():
    # When the program starts, load_tasks() runs first, it opens tasks.txt and loads old tasks

    if os.path.exists("tasks.txt"):  # os module has been used here to check if the file already exists

        with open("tasks.txt", "r") as file:

            for line in file:

                line = line.strip()

                if line:

                    parts = line.split("|")

                    # Adding task over here, each task is stored in the form of a dictionary

                    if len(parts) == 5:

                        task = {
                            "id": int(parts[0]),
                            "name": parts[1],
                            "completed": parts[2] == "True",
                            "priority": parts[3],
                            "due_date": parts[4]
                        }

                        tasks.append(task)


def save_tasks():
    # This function writes all tasks into the file
    # Whenever Add Task, Delete Task, Mark Complete or Edit is performed,
    # this function saves the latest data

    with open("tasks.txt", "w") as file:

        for task in tasks:

            file.write(
                f"{task['id']}|"
                f"{task['name']}|"
                f"{task['completed']}|"
                f"{task['priority']}|"
                f"{task['due_date']}\n"
            )


def add_task():
    # User enters a task that creates a dictionary
    # Then tasks.append(task) adds it to the list

    task_name = input("Enter Task: ")

    if task_name.strip() == "":
        print("Task Cannot Be Empty!")
        return

    priority = input("Priority (High/Medium/Low): ")

    due_date = input("Enter Due Date (DD-MM-YYYY): ")

    next_id = 1

    if tasks:

        max_id = max(task["id"] for task in tasks)

        next_id = max_id + 1

    task = {
        "id": next_id,
        "name": task_name,
        "completed": False,
        "priority": priority,
        "due_date": due_date
    }

    tasks.append(task)
    print(tasks)

    save_tasks()

    print("Task Added Successfully!")


def view_tasks():
    # This displays every task
    if not tasks :
        print("No Tasks found!")
        return
    print("\n---TASK LIST---")

    for task in tasks :
        print(task)

def edit_task():
    # User can modify an existing task

    view_tasks()

    try:

        task_id = int(input("Enter Task ID to Edit: "))

        for task in tasks:

            if task["id"] == task_id:

                new_name = input("Enter New Task Name: ")

                if new_name.strip() == "":
                    print("Task Name Cannot Be Empty!")
                    return

                task["name"] = new_name

                save_tasks()

                print("Task Updated Successfully!")

                return

        print("Task Not Found!")

    except ValueError:

        print("Invalid Input!")


def mark_completed():
    # User enters task ID
    # Program finds the task and changes the completed status

    view_tasks()

    try:

        task_id = int(input("Enter Task ID: "))

        for task in tasks:

            if task["id"] == task_id:

                task["completed"] = True

                save_tasks()

                print("Task Marked Completed!")

                return

        print("Task Not Found!")

    except ValueError:

        print("Invalid Input!")


def delete_task():
    # User enters the Task ID which is to be deleted

    view_tasks()

    try:

        task_id = int(input("Enter Task ID to Delete: "))

        for task in tasks:

            if task["id"] == task_id:

                tasks.remove(task)

                save_tasks()

                print("Task Deleted!")

                return

        print("Task Not Found!")

    except ValueError:

        print("Invalid Input!")


def search_task():
    # Search task using a keyword

    keyword = input("Enter Keyword: ").lower()

    found = False

    for task in tasks:

        if keyword in task["name"].lower():

            status = "Completed" if task["completed"] else "Pending"

            print(
                f"ID: {task['id']} | "
                f"Task: {task['name']} | "
                f"Status: {status}"
            )

            found = True

    if not found:

        print("No Matching Tasks Found!")


def task_statistics():
    # Shows total, completed and pending tasks

    total = len(tasks)

    completed = 0

    for task in tasks:

        if task["completed"]:
            completed += 1

    pending = total - completed

    print("\n===== TASK STATISTICS =====")

    print("Total Tasks:", total)

    print("Completed Tasks:", completed)

    print("Pending Tasks:", pending)


def menu():
    # This is the Heart of the application

    while True:  # it means keep running forever

        print("\n")
        print("=" * 35)
        print("         TO-DO MANAGER")
        print("=" * 35)

        print("1. Add Task")
        print("2. View Tasks")
        print("3. Edit Task")
        print("4. Mark Completed")
        print("5. Delete Task")
        print("6. Search Task")
        print("7. Task Statistics")
        print("8. Exit")

        # Based on your choice a corresponding function is called

        choice = input("Enter Your Choice: ")

        if choice == "1":

            add_task()

        elif choice == "2":

            view_tasks()

        elif choice == "3":

            edit_task()

        elif choice == "4":

            mark_completed()

        elif choice == "5":

            delete_task()

        elif choice == "6":

            search_task()

        elif choice == "7":

            task_statistics()

        elif choice == "8":

            print("Goodbye!")

            break

        else:

            print("Invalid Choice!")


# Program starts from here

load_tasks()

menu()