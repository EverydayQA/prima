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
        parser = argparse.ArgumentParser(description='Example with non-optional arguments')
        parser.add_argument('count', action="store", type=int)
        parser.add_argument('units', action="store")
        return parser


def main(argv):
    ex = ArgExample()
    parser = ex.get_parser()

    # from cmd line
    print(argv)
    args = parser.parse_args(argv)
    print(args)


if __name__ == '__main__':
    main(sys.argv[1:])
