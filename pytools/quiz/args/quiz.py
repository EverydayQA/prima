import argparse
import logging


class ArgsQuiz(object):

    def get_parser(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("-l", '--logging_level', type=int, default=logging.INFO, help='logging level')
        parser.add_argument('--take', type=str)
        parser.add_argument('--add', type=str)
        return parser

    def parse_args(self, argv):
        parser = self.get_parser()
        args = parser.parse_args(argv)
        return args
