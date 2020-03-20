import os


def work_on():
    path = os.getcwd()
    print(f"Working on {path}")
    return path

def unpleasant_side_effect():
    print("I am an unpleasant side effect of importing this module")

# Note that this is called simply by importing this file
unpleasant_side_effect()
