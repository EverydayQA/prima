import argparse
import sys


class ArgExample(object):
    """
    https://pymotw.com/2/argparse/#module-argparse
    """

    def get_parser(self):
        """
        using the GNU/POSIX syntax
        attention to the usage of '--witharg2=3'
        """
        parser = argparse.ArgumentParser(description='Example with long option names')

        parser.add_argument('--noarg', action="store_true", default=False)
        parser.add_argument('--witharg', action="store", dest="witharg")
        parser.add_argument('--witharg2', action="store", dest="witharg2", type=int)
        parser.add_argument('--witharg3', action="store", dest="witharg3", type=str)

        return parser


def main(argv):
    ex = ArgExample()
    parser = ex.get_parser()

    # example
    argv2 = ['--noarg', '--witharg', 'val', '--witharg2=3', '--witharg3=-s S --long LONG']
    print(argv2)
    args = parser.parse_args(argv2)
    print(args)

    # from cmd line
    print(argv)
    args = parser.parse_args(argv)
    print(args)


if __name__ == '__main__':
    main(sys.argv[1:])
