import os


def work_on():
    path = os.getcwd()
    print("Working on {}".format(path))
    return path


def unpleasant_side_effect():
    raise Exception("I am an unpleasant side effect of importing this module")


# Note that this is called simply by importing this file
unpleasant_side_effect()
