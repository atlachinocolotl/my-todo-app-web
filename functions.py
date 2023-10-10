FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """ Opens file and reads each line . Returns the list of
    to-do items
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """Write a to-do items list in the text file."""
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)
    return None
