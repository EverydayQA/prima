import argparse
import datetime


class ArgStock(object):

    def ord_args(self, args):
        """
        a list of int to pass a list
        """
        argstr = ' '.join(args)
        return [str(ord(char)) for char in argstr]

    def chr_args(self, args):
        cli2 = []
        for item in args:
            cli2.append(chr(int(item)))
        return ''.join(cli2)

    def get_parser(self):
        parser = argparse.ArgumentParser()

        # By default it will fail with multiple arguments.
        parser.add_argument('--default')

        # datetime
        parser.add_argument('--now', default=datetime.datetime.now(), help="It should not be a arg, but did anyway")

        # Telling the type to be a list will also fail for multiple arguments,
        # but give incorrect results for a single argument.
        parser.add_argument('--list-type', type=list)

        # This will allow you to provide multiple arguments, but you will get
        # a list of lists which is not desired.
        parser.add_argument('--list-type-nargs', type=list, nargs='+')

        # This is the correct way to handle accepting multiple arguments.
        # '+' == 1 or more.
        # '*' == 0 or more.
        # '?' == 0 or 1.
        # An int is an explicit number of arguments to accept.
        parser.add_argument('-m', '--multiple', nargs='+')

        # To make the input integers
        parser.add_argument('-j', '--job', nargs='+', type=int)

        # An alternate way to accept multiple inputs, but you must
        # provide the flag once per input. Of course, you can use
        # type=int here if you want.
        parser.add_argument('-a', '--append', dest='appending', action='append')
        return parser

    def init_args(self, argv):
        parser = self.get_parser()
        return parser.parse_args(argv)
