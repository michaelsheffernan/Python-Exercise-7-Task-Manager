

class Tasks:
    def __init__(self):
        self.tasks = []

    def show_tasks(self):
        if self.tasks == []:
            print("You have no tasks.")

        else:
            print(f"Your current tasks are: {self.tasks}")

    def add_tasks(self):
        new_task = str(input("What task would you like to add: "))
        try:
            self.tasks.append(new_task)
            print(f"You have added {new_task} to your task list.")
            return self.tasks
        except ValueError:
            print("Invalid Input")
            return self.tasks

    def delete_tasks(self):
        delete_task = input("What task would like to delete: ")

        try:
            deletion_confirmation = input("Confirm deletion y/n : ")

        except ValueError:
            print("That task is not in your task list.")
            return self.tasks

        if deletion_confirmation == "n":
            print("Deletion cancelled")
            return self.tasks
        elif deletion_confirmation == "y":
            self.tasks.remove(delete_task)
            print(f"{delete_task} has been deleted.")
            return self.tasks

        else:
            print("Invalid Input")
            return self.tasks

    def mark_task_complete(self):
        marked_task = input("Which task do you want to mark: ")
        try:
            self.tasks.remove(marked_task)
            self.tasks.append(marked_task + " ✅ ")
            print(f"{marked_task} has been marked complete.")
            return self.tasks

        except ValueError:
            print("That task is not in your task list.")
            return self.tasks
