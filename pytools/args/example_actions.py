import argparse
import sys


class ArgExample(object):
    """
    https://pymotw.com/2/argparse/#module-argparse
    """

    def get_parser(self):
        """
        never used
        store_false

        and do not know when to use
        store_const
        append_const
        """
        parser = argparse.ArgumentParser(description='Example with different actions')

        parser.add_argument('-s', action='store', dest='simple_value',
                            help='Store a simple value')

        parser.add_argument('-c', action='store_const', dest='constant_value',
                            const='value-to-store',
                            help='Store a constant value')

        parser.add_argument('-t', action='store_true', default=False,
                            dest='boolean_switch',
                            help='Set a switch to true')
        parser.add_argument('-f', action='store_false', default=False,
                            dest='boolean_switch',
                            help='Set a switch to false')

        parser.add_argument('-a', action='append', dest='collection',
                            default=[],
                            help='Add repeated values to a list',)

        parser.add_argument('-A', action='append_const', dest='const_collection',
                            const='value-1-to-append',
                            default=[],
                            help='Add different values to list')
        parser.add_argument('-B', action='append_const', dest='const_collection',
                            const='value-2-to-append',
                            help='Add different values to list')

        parser.add_argument('--version', action='version', version='%(prog)s 1.0')

        return parser


def main(argv):
    ex = ArgExample()
    parser = ex.get_parser()

    print(argv)
    args = parser.parse_args(argv)
    print(args)


if __name__ == '__main__':
    main(sys.argv[1:])
