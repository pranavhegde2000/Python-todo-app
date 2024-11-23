from functions import get_todos, write_todos
import time
# import functions

now = time.strftime("%b %d,%Y %H:%M:%S")
print("It is now ",now)

while True:
    user_action = input(
        "Type add, show, edit, complete or exit: ")  # input() function will convert the input from the user into string
    user_action = user_action.strip()  # strip() function will remove white spaces in the beginning and end

    if user_action.startswith('add'):
        todo = user_action[4:]
        # file = open('todos.txt', 'r')
        # todos = file.readlines()
        # file.close()
        todos = get_todos()  # functions.get_todos() can be used if we only import functions module, usefule when a module as many functions

        todos.append(todo + '\n')
        # file = open('todos.txt','w') #Open the todos.txt file in write mode
        # file.writelines(todos) #Write multiple lines from the todos list into the tods.txt file
        '''The function writelines('todos.txt','w') will create a new file todos.txt to write data, if that file
            already exists then it get overridden, and all the data in it, so it is better to have a readline()
            function beforehand that appends the data in that file into todosshow
        '''
        # file.close()
        write_todos(todos)

    elif user_action.startswith('show'):
        todos = get_todos()

        # new_todos = [item.strip('\n') for item in todos]
        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1
            todos = get_todos()
            print("Here is how it looks like now", todos)
            new_todo = input("Enter the new todo: ")
            todos[number] = new_todo + "\n"
            print("Here is how it will look after the edit", todos)
            write_todos(todos)
        except ValueError:
            print("Your command is not valid.")
            continue
    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])
            todos = get_todos()
            index = number - 1
            todo_to_remove = todos[index]
            todos.pop(index)
            write_todos(todos)

            message = f"Todo {todo_to_remove} was removed from the list \n"
            print(message)
        except IndexError:
            print("There is no item with that number")
            continue
    elif user_action.startswith('exit'):
        break
    else:
        print("Command is not valid")
print("Bye!")