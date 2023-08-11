# main.py

from todo_list import ToDoList


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

