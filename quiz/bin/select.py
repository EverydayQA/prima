#!/usr/bin/python
import os
import sys

# similar to findBin in Perl
pwd = os.path.dirname(os.path.realpath(__file__))
# 1 level up
base_dir = os.path.join(pwd,'..')
# add to sys.path
sys.path.append(base_dir)

from lib import menu

def main(argv):
    # args
    # menu.print_format_table()

    # read 1 json file, 1 quiz from take_quiz()
    the_list = ['a','b','c','d']
    selections = menu.select_from_list(the_list)
    print selections

    # option to redo

    # compare to answer

    # insert the result

if __name__ == '__main__':
    main(sys.argv[1:])
