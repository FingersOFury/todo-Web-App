FILEPATH = "Tasks.txt"


def get_tasks(filepath=FILEPATH):
    """ Reads the text file and returns a list of
    tasks inputted by the user
    """
    with open(filepath, "r") as file_local:
        tasklist_local = file_local.readlines()
    return tasklist_local


def write_tasks(tasklist_arg, filepath=FILEPATH):
    """ Writes the lists of tasks on the text file."""
    with open(filepath, "w") as file_local:
        file_local.writelines(tasklist_arg)


if __name__ == "__main__":
    print(get_tasks())