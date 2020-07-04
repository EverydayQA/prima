from pprint import pprint
# import argparse


class ArgparseExample(object):

    def __init__(self):
        pass

    def args_to_passon(self):
        """
        passed on to another cli args to be parsed
        cli.py --cli_type="--house --semi"
        """
        pass

    def parser_athome(self):
        """
        store a one variable
        cli.py --stayhome --stay_home --stay-home --athome
        """
        pass


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
