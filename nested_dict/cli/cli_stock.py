from pprint import pprint


class Exchange(object):
    pass


class Stock(object):

    def dividend(self):
        pass

    def volume(self):
        pass

    def description(self):
        pass

    def long_name(self):
        pass

    def exchange_name(self):
        pass

    def category(self):
        """
        oil/manufacture/edu/pharmaceutical/food/bank/financial/
        """
        pass

    def score(self):
        pass

    def value(self):
        pass

    def buy_at(self):
        pass

    def sell_at(self):
        pass


class CliStock(object):
    """
    class to calculate weight based on certain criteria
    Do not take it for real, this is used for practice
    """

    def save_stock(self, d):
        """
        save to a json file
        """
        pass

    def add_weight(self):
        """
        add sth to a stock
        exchange
        """


def main(argv=None):
    from arg.arg_example import ArgsExample
    arg = ArgsExample()
    args = arg.init_args(argv)
    pprint(args)

    # cli2 = ['--path', '/tmp', '--short', '--nohope']
    # cli2_ascii = arg.ord_args(args=cli2)
    # print(cli2_ascii)
    # cli2_list2 = arg.chr_args(args=cli2_ascii)
    # print(cli2_list2)

    default = args.default
    # or
    default = " --default  2  -m a b c"
    argv = default.split(' ')
    print(argv)
    argv = filter(None, argv)
    args2 = arg.init_args(argv)
    print(args2)


def howto(self):
    """
    PYTHONPATH=. python3 cli/cli_example.py -m a b c --a no --a yes --a nohold --a nrx3 -a b -m " --nohold"  " --nnn4" " --nocheck" " --job" " -j" --job 2 4 5 6
    ord_args() and chr_args are crazy but works
    " --nocheck" with a space does work and could lstrip() or no need
    PYTHONPATH=. python3 cli/cli_example.py --default="--nohold --nocheck"
    PYTHONPATH=. python3 cli/cli_example.py --default="--default  2  -m a b c"
    """
    pass


if __name__ == "__main__":
    import sys
    main(sys.argv[1:])
