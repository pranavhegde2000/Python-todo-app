FILEPATH = "todos.txt"
def get_todos(filepath=FILEPATH):  # Create a custom function get_todos() to handle all the read file parts
    """Read a text file and return the list of to-do items """
    with open(filepath, 'r') as file_local:  # Implementing the above reading file code using "with context manager"
        todos_local = file_local.readlines()  # This is the recommended way to read files, file.close() not requried here as it gets automatically closed
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):  # Custom function for writing on to the files, todos_arg
    """Writes todos data onto a text file """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)  # No need to return anything as it just a file write

if __name__ == "__main__":  #this if block will execute only if this py file is being run directly, wont run if it has been called to some other function
    print("Hello from functions")
    print(get_todos())