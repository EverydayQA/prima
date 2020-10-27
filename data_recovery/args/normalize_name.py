import argparse
import os


class ArgNormalizeName(object):

    def get_parser(self):
        parser = argparse.ArgumentParser()

        parser.add_argument('--run', action='store_true', default=False)
        parser.add_argument('--path', dest='path', type=str, default=os.getcwd())
        parser.add_argument('--logging_level', default=10, type=int)

        return parser

    def parse_args(self, argv):
        parser = self.get_parser()
        return parser.parse_args(argv)
