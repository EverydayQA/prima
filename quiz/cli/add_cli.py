#!/usr/bin/python
import sys
import argparse
from ..add.add_wrapper import AddWrapper
from pprint import pprint


def init_args_addquiz():
    parser = argparse.ArgumentParser()
    parser.add_argument('--logging', type=int, default=20, help='logging level')
    parser.add_argument('--category', type=str, default='QC', help='Category')

    args, args_extra = parser.parse_known_args(sys.argv[1:])
    return args, args_extra


def main():
    args, args_extra = init_args_addquiz()
    kwargs = vars(args)
    pprint(kwargs)
    print('\n\n*** add_cli.main()')
    aw = AddWrapper(args_extra, **vars(args))
    # dispatch handover to AddQuiz?
    aw.dispatch()
    print('\n\n*** add_cli.main()')


if __name__ == '__main__':
    main()
