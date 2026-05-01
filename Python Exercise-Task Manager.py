from Tasks import *

print("""Welcome to Task Manager 
Please Sign Up""")

user_email = input("Email: ")
user_password = input("Password: ")

task_manager = Tasks()

log_in_attempt = 0


while log_in_attempt < 3:
    print("Welcome, please log in.")
    email_entry = input("Email: ")
    password_entry = input("Password: ")

    if email_entry == user_email and password_entry == user_password:
        print("Welcome")

        while True:
            print(""" TASK MANAGER
                -----------------
                1. Show Tasks
                2. Add Tasks
                3. Delete Tasks
                4. Mark Task as Complete
                5. Exit """)
            user_input = input("Enter command: ")
            if user_input == "1":
                task_manager.show_tasks()

            elif user_input == "2":
                task_manager.add_tasks()

            elif user_input == "3":

                task_manager.delete_tasks()

            elif user_input == "4":

                task_manager.mark_task_complete()

            elif user_input == "5":
                print("Thank you for using Task Manager")
                print("Goodbye.")
                break

            else:
                print("Invalid command. Please choose between commands: 1, 2, 3, 4 or 5")

    else:
        print("Incorrect Credentials")
    log_in_attempt += 1
    if log_in_attempt == 3:
        print("""Maximum Attempts Reached
              Goodbye""")
