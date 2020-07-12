from pprint import pprint


class CliStock(object):
    """
    class to calculate weight based on certain criteria
    Do not take it for real, this is used for practice
    """

    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        self.ns = self.get_ns()

    def get_ns(self):
        from args.arg_stock import ArgStock
        arg = ArgStock()
        args = arg.init_args(self.args)
        return args

    def action(self):
        pprint(self.ns)
        from lib.stock_wrapper import StockWrapper
        wrapper = StockWrapper(**vars(self.ns))
        wrapper.action()


def main(argv=None):

    # feed into class
    cli = CliStock(*argv)
    cli.action()


def howto(self):
    """
    PYTHONPATH=. python3 cli/cli_example.py -m a b c --a no --a yes --a nohold --a nrx3 -a b -m " --nohold"  " --nnn4" " --nocheck" " --job" " -j" --job 2 4 5 6
    ord_args() and chr_args are crazy but works
    " --nocheck" with a space does work and could lstrip() or no need
    PYTHONPATH=. python3 cli_stock.py --default="--default  2  -m a b c"
    """
    pass


if __name__ == "__main__":
    import sys
    main(sys.argv[1:])
