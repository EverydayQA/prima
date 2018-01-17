#!/usr/bin/python3.5

import cmd
import sys


class Interpreter(cmd.Cmd):

    def __init__(self, stdin=sys.stdin, stdout=sys.stdout):
        cmd.Cmd.__init__(self, stdin=stdin, stdout=stdout)

    def do_show(self, args):
        print("Hello world!")


def main():
    interpreter = Interpreter()
    interpreter.onecmd('show')


if __name__ == "__main__":
    main()
