#!/usr/bin/python
import argparse
from pprint import pprint
import sys


def get_parser():
    parser = argparse.ArgumentParser(description='example of argparse')
    parser.add_argument('--foo', action='store_true')
    parser.add_argument('--run', action='store_true')
    parser.add_argument('--email', action='store_true')
    parser.add_argument('--high', action='store_true')
    parser.add_argument('--remove_index', type=int, help='remove index')
    parser.add_argument('--remove', help='remove path or search_string')
    parser.add_argument('--search', help='define search string')
    parser.add_argument('--d', type=str, nargs=2, help='2 files')
    return parser


def remove_index(index):
    print index
    return index


def remove_path(path):
    print path
    return path


def remove_string(string):
    print string
    return string


def search_string(string):
    print string
    return string


def assign_uid(uid):
    print uid
    return uid


def assign_group(group):
    print group
    return group


def add_comments(comment):
    print comment
    return comment


def main():
    class C(object):
        pass

    c = C()
    parser = get_parser()
    args = parser.parse_args(namespace=c)
    parser.print_help()
    # print args.accumulate(args.integers)

    if c.email is True:
        print "email true"
    print c.high
    print c.run
    print c.email
    print c.remove
    print c.search
    print (vars(args))
    # search_string("Email")
    # print type(C())
    # print C().__class__.__name__


if __name__ == '__main__':
    parser = get_parser()
    args = parser.parse_args(sys.argv[1:])
    pprint(args)
