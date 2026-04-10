user_email = "user1@gmail.com"
user_password = "Admin123"


task_list = []


def show_tasks():
    if task_list == []:
        print("You currently have no tasks.")

    else:
        print(f"Your current tasks are: {task_list}")
    return


def add_tasks(task_list):
    print("Add a Task")
    new_task = str(input("New Task: "))
    task_list.append(new_task)
    print(f"You have added {new_task} to your task list.")
    return task_list


def delete_tasks(task_list):
    print("Type Task for deletion")
    deleted_task = str(input("Delete Task: "))
    deletion_confirmation = str(input("Confirm deletion y/n: "))
    if deletion_confirmation == "y":
        task_list.remove(deleted_task)
        print(f"You have deleted {deleted_task} from your current tasks.")
        return task_list
    elif deletion_confirmation == "n":
        print("Deletion Cancelled")
        return task_list
    else:
        print("Invalid Input")
        return task_list


def mark_task(task_list):
    print("Which Task should be marked complete?")
    marked_task = str(input("Mark Task Complete: "))
    task_list.remove(marked_task)
    task_list.append(marked_task + " ✅ ")
    print("Task marked complete")
    return task_list


log_in_attempt = 0

while log_in_attempt <= 3:
    print("Welcome, please log in.")
    email_entry = str(input("Email: "))
    password_entry = str(input("Password: "))

    if email_entry == user_email and password_entry == user_password:
        print("Welcome")

        while True:
            print("' TASK MANAGER"
                  "-----------------"
                  " 1. Show Tasks"
                  " 2. Add Tasks"
                  " 3. Delete Tasks"
                  " 4. Mark Task as Complete"
                  " 5. Exit '")
            user_input = str(input("Enter command: "))
            if user_input == "1":
                show_tasks()

            elif user_input == "2":
                task_list = add_tasks(task_list)

            elif user_input == "3":
                task_list = delete_tasks(task_list)

            elif user_input == "4":
                task_list = mark_task(task_list)

            elif user_input == "5":
                print("Thank you for using Task Manager")
                print("Goodbye.")
                break

            else:
                print("Invalid command. Please choose between commands: 1, 2, 3, 4 or 5")

    else:
        print("Incorrect Credentials")
    log_in_attempt += 1
