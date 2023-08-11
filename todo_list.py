#todo_list.py

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
