#!/usr/bin/python
import argparse
from pprint import pprint

"""
            class FooBar def __init__(self, args, kwargs):

            # define a dict
            d = {}
            d['foo'] = 111
            d['bar'] = ['a', 'b']

            # pass dict as kwargs
            fb = FooBar(**d)

"""


class User(object):

    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        pprint(args)
        pprint(kwargs)

    def set_exam(self):
        exam = Exam(*self.args, **self.kwargs)
        return exam


class Exam(object):

    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        pprint(args)
        pprint(kwargs)


def init_args():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("-?", '--help', action="help", help='xxx')
    parser.add_argument("-category", '--category', type=str, default=None, dest='category', help='category')
    parser.add_argument("-run", '--run', action='store_true', dest='run', help='run')
    parser.add_argument("-logging", '--logging', type=int, default=30, dest='logging', help='logging level 0 10 20')
    args, args_extra = parser.parse_known_args()
    return args, args_extra


def main():
    args, args_extra = init_args()
    u = User(*args_extra, **vars(args))
    u.set_exam()


if __name__ == '__main__':
    main()
