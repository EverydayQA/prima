import os
import subprocess
globalvar = 'original'


def calc(keys, values):
    if globalvar == "calc":
        return sum(keys)
    else:
        return sum(values)


def rm(filename):
    if os.path.isfile(filename):
        os.remove(filename)


def do_cmd(command):
    """
    For test purpose only
    """
    process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    output = process.communicate()
    d = {}
    d['returncode'] = process.returncode
    d['output'] = output
    if process.returncode != 0:
        pass
    return d
