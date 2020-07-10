from pprint import pprint
import os


class CliStock(object):
    """
    class to calculate weight based on certain criteria
    Do not take it for real, this is used for practice
    """

    def create_a_stock(self):
        print('create a stock with what? prompt to type:/select from list/read from files')
        d = {}
        return d

    def save_stock(self, d):
        """
        save to a json file
        """
        print('save a stock')

    def jsonfile(self, exchange, stock):
        log = '{}_{}.json'.format(exchange, stock)
        log = os.path.join(self.logdir(), log)
        return log

    def logdir(self):
        return '/tmp'

    def add_weight(self):
        """
        add sth to a stock
        exchange
        """
        pass


def main(argv=None):
    from arg_stock import ArgsExample
    arg = ArgsExample()
    args = arg.init_args(argv)
    pprint(args)
    cli = CliStock()
    d = cli.create_a_stock()
    cli.save_stock(d)


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
