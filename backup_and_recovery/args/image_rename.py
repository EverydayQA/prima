import argparse
import os


class ArgImageRename(object):

    def get_parser(self):
        parser = argparse.ArgumentParser()

        parser.add_argument('--run', action='store_true', default=False)
        parser.add_argument('--new', '--newpath', '--new_path', dest='newpath', required=True, default=None)
        parser.add_argument('--path', dest='path', type=str, default=os.getcwd())

        return parser

    def parse_args(self, argv):
        parser = self.get_parser()
        return parser.parse_args(argv)
