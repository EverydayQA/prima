import argparse
import sys


class ArgExample(object):
    """
    https://pymotw.com/2/argparse/#module-argparse
    """

    def get_parser(self):
        """
        """
        parser = argparse.ArgumentParser(description='Change the option prefix characters',
                                         prefix_chars='-+/',)

        parser.add_argument('-a', action="store_false", default=None,
                            help='Turn A off',)
        parser.add_argument('+a', action="store_true", default=None,
                            help='Turn A on',)
        parser.add_argument('//noarg', '++noarg', action="store_true", default=False)
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
