#!/usr/bin/python
import sys
from myutils import menu


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
        # timeout cycle limit
        men = menu.Menu(cycle=10, limit=0, timeout=4)
        selections = men.select_from_menu(the_list, "select one or more")
        print(selections)

        men = menu.Menu(cycle=5, timeout=4, limit=1)
        selections = men.select_from_menu(the_list, "select only one item")
        print(selections)

        selections = men.select_from_menu(the_list, "select only one item with default", default='default')
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
