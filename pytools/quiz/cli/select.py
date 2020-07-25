#!/usr/bin/python
import sys
from utils import menu


class CliSelect(object):

    def __init__(self):
        pass

    def select(self):
        """
        demo a selection process
        add args for Menu class
        --timeout
        --min sels 1
        --max sels None
        --cycle how many times to choose if not chosen
        --redo option
        salesExamples could be used here for menu and Nestedcit app
        """
        # read 1 json file, 1 quiz from take_quiz()
        the_list = ['aaa', 'bbb', 'ccc', 'ddd']
        selections = menu.Menu().select_from_menu(the_list, "select")
        print(selections)


def main(argv):

    cli = CliSelect()
    cli.select()
    # menu.print_format_table()

    # user
    # time
    # category
    # number of questions
    # compare to answer
    # insert the result
    # take_quiz


if __name__ == '__main__':
    main(sys.argv[1:])
