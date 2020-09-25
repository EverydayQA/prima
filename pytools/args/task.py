import argparse


class ArgTask(object):
    """
    using const in argument
    inherit ConstClass using const module

    argv to args to dict to full cmds
    1)
    for example purpose
    assume task parser will take known arguments first
    put back to argv if there is overalp
    2)
    passed on unknown arguments to another parser
    3)
    perl script to take parameters to run task cli with parameters? task_cli take arguments first, pass unknown arguments to bbb_cli
    """

    def parse_known_args(self, argv):
        """
        use parse_known_args() with caution, it is intend to be used
        when the first script take its own args and pass on the rest
        to the next script, the first script must have unique argments compared to the next script
        """
        parser = self.get_parser()
        # args and argv_left
        return parser.parse_known_args(argv)

    def parse_args(self, argv):
        """
        use parse_known_args() with caution, it is intend to be used
        when the first script take its own args and pass on the rest
        to the next script, the first script must have unique argments compared to the next script
        """
        parser = self.get_parser()
        return parser.parse_args(argv)

    def get_parser(self):
        """
        """
        parser = argparse.ArgumentParser()

        # an example of aliases and dest name
        parser.add_argument('-o', '--athome', '--at-home', '--at_home', '--home', dest='home', action='store_true', default=False)

        # positional argument
        parser.add_argument('action', choices=('start', 'stop', 'restart'))

        # choice - use subparser or not?
        parser.add_argument('--email_group',
                            default='all',
                            const='all',
                            nargs='?',
                            choices=['student', 'teacher', 'all'],
                            help='email to group student, teacher, or both (default: %(default)s)')
        # range
        parser.add_argument('-d', '--debug', nargs='?', metavar='1..5', type=int,
                            choices=range(1, 5), default=2,
                            help='Debug level is a value between 1 and 5')

        # mutual exclusive group
        # GNU convention -m short --multiple for long -multiple does not make sense
        group = parser.add_mutually_exclusive_group()
        group.add_argument('-c', '--create', action='store_true', help="create a task")
        group.add_argument('-r', "--remove", action='store_true', help="remove a task")
        group.add_argument('-u', '--update', action='store_true', help="update a task")

        # is it possible to use pyplot instead of termplot? initiated by cli?
        parser.add_argument('-g', '--gui', action='store_true',
                            help='Start in graphical mode if given')

        parser.add_argument('-o', '--output', nargs='?', metavar='path',
                            type=str, default="/tmp/output.txt",
                            help='Store program output in the file passed after -o')

        # copy from others -- refactor and remove later
        # By default it will fail with multiple arguments.
        parser.add_argument('--default')

        parser.add_argument('--add', action='store_true', default=False)

        parser.add_argument('--update', type=str, default=None, help='search string to update a stock')

        # This is the correct way to handle accepting multiple arguments.
        # '+' == 1 or more.
        # '*' == 0 or more.
        # '?' == 0 or 1.

        # An alternate way to accept multiple inputs, but you must
        # provide the flag once per input. Of course, you can use
        # type=int here if you want.
        parser.add_argument('-a', '--append', dest='appending', action='append')
        return parser
