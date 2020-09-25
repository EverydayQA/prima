import argparse
import sys


class ArgExample(object):
    """
    https://pymotw.com/2/argparse/#module-argparse
    """

    def get_parser(self):
        """
        using the GNU/POSIX syntax
        attention to the usage of '-bval'
        """
        parser = argparse.ArgumentParser(description='Short sample app')

        parser.add_argument('-a', action="store_true", default=False)
        parser.add_argument('-b', action="store", dest="b")
        parser.add_argument('-c', action="store", dest="c", type=int)
        return parser


def main(argv):
    ex = ArgExample()
    parser = ex.get_parser()

    # example
    argv2 = ['-a', '-bval', '-c', '3']
    print(argv2)
    args = parser.parse_args(argv2)
    print(args)

    # from cmd line
    print(argv)
    args = parser.parse_args(argv)
    print(args)


if __name__ == '__main__':
    main(sys.argv[1:])
