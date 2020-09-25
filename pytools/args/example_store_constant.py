import argparse
import sys


class ArgExample(object):
    """
    """

    def get_parser(self):
        """
        """
        parser = argparse.ArgumentParser(description='Process some integers.')
        parser.add_argument('integers', metavar='N', type=int, nargs='+',
                            help='an integer for the accumulator')
        parser.add_argument('--sum', dest='accumulate', action='store_const',
                            const=sum, default=max,
                            help='sum the integers (default: find the max)')

        return parser


def main(argv):
    ex = ArgExample()
    parser = ex.get_parser()

    args = parser.parse_args(argv)
    print(args.integers)
    print(args.accumulate(args.integers))


if __name__ == '__main__':
    # 1 2 3 4 --sum
    # --sum 1 2 3 4
    main(sys.argv[1:])
