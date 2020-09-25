import argparse
import sys
from configparser import ConfigParser
import shlex
import os


class ArgExample(object):
    """
    https://pymotw.com/2/argparse/#module-argparse
    """

    def get_parser(self):
        """
        using the GNU/POSIX syntax
        attention to the usage of '--witharg2=3'
        """

        parser = argparse.ArgumentParser(description='Short sample app')

        parser.add_argument('-a', action="store_true", default=False)
        parser.add_argument('-b', action="store", dest="b")
        parser.add_argument('-c', action="store", dest="c", type=int)

        return parser


def main(argv):
    ex = ArgExample()
    parser = ex.get_parser()

    config = ConfigParser()
    conf_file = 'argparse_with_shlex.ini'
    dirname = os.path.dirname(os.path.realpath(__file__))
    conf_file = os.path.join(dirname, conf_file)
    print(conf_file)
    config.read(conf_file)
    config_value = config.get('cli', 'options')
    print('Config  : {}'.format(config_value))
    argument_list = shlex.split(config_value)
    print('Arg List:'.format(argument_list))
    args = parser.parse_args(argument_list)
    print(args)


if __name__ == '__main__':
    main(sys.argv[1:])
