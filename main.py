from functions import get_todos, write_todos

import time

now = time.strftime("%d %b, %Y - %H:%M:%S")
print("The date is below:")
print("It is ", now)

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]

        todos = get_todos()

        todos.append(todo + "\n")

        write_todos(todos)

    elif user_action.startswith('show'):

        todos = get_todos()

        item: str
        for index, item in enumerate(todos):
            item = item.strip("\n")
            row = f"{index + 1}. {item}"
            print(row)

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1
            todos = get_todos()
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + "\n"

            write_todos(todos)

        except ValueError:
            print("Invalid command!")
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])
            todos = get_todos()
            index = number - 1
            todos_to_remove = todos[index].strip("\n")
            todos.pop(index)

            write_todos(todos)

            message = f"Todo '{todos_to_remove}' has been removed from the list."
            print(message)

        except IndexError:
            print("There is no item with that number!")
            continue

    elif user_action.startswith('exit'):
        break

    else:
        print("Invalid command!")
print("Bye!")
