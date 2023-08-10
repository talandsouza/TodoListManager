class ToDoList:

  def __init__(self):
    self.tasks = []

  def add_task(self, task):
    self.tasks.append(task)
    print(f"Task '{task}' added to the list.")

  def view_tasks(self):
    if self.tasks:
      print("Your To-Do List:")
      for index, task in enumerate(self.tasks, start=1):
        print(f"{index}. {task}")
    else:
      print("Your To-Do List is empty.")

  def remove_task(self, index):
    if 1 <= index <= len(self.tasks):
      removed_task = self.tasks.pop(index - 1)
      print(f"Task '{removed_task}' removed from the list.")
    else:
      print("Invalid task index.")

  def check_tasks(self):
    if self.tasks:
      return 0
    else:
      return 1


def main():
  todo_list = ToDoList()

  while True:
    print("\nMenu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("\nEnter your choice (1/2/3/4): ")

    if choice == "1":
      task = input("\nEnter the task: ")
      todo_list.add_task(task)
    elif choice == "2":
      todo_list.view_tasks()
    elif choice == "3":
      if todo_list.check_tasks():
        print("\nYour To-Do List is empty.")
      else:
        index = int(input("\nEnter the task index to remove: "))
        todo_list.remove_task(index)
    elif choice == "4":
      print("\nExiting the To-Do List application.")
      break
    else:
      print("\nInvalid choice. Please select a valid option.")


if __name__ == "__main__":
  main()

