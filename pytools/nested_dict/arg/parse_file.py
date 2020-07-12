import argparse
import sys


class ArgParseFile(object):

    def __init__(self):
        pass

    def get_args(self, argv):
        parser = self.get_parser()
        args = parser.parse_args(sys.argv[1:])
        return args

    def get_parser(self):
        parser = argparse.ArgumentParser(description='parsefile')
        parser.add_argument('--run', action='store_true')
        requiredNamed = parser.add_argument_group('required named arguments')
        requiredNamed.add_argument('-f', '--file', help='Input file name', required=True)
        return parser
