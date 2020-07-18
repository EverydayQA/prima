import argparse


class ArgsTmpDir(object):
    """
    example of subcmd args
    """

    def get_me_parser(self):
        parser = argparse.ArgumentParser(prog='tmpdir')
        group = parser.add_mutually_exclusive_group(required=True)
        # must --cwd or --path, not both
        group.add_argument('--cwd')
        group.add_argument('--path')
        return parser

    def get_parser2(self):
        """
        Example of args of subcmds
        # help of subcmd clean
        tmpdir clean -h
        """
        parser = argparse.ArgumentParser(prog='tmpdir')
        # default cmd is tmpdir
        parser.set_defaults(cmd="tmpdir")
        parser.add_argument('--path', action='store_true', default='/tmp', help='path to profile, createsubdir or cleanup')

        subparsers = parser.add_subparsers(help='subparser')

        # subcmd create_tmpdir
        sp = subparsers.add_parser('create', help='positional arg')
        sp.set_defaults(cmd='create_tmpdir')
        sp.add_argument('--name', type=str, help='name of subdir')

        # subcmd clean
        sp = subparsers.add_parser('clean', help='this cli is positional args, cleanup subdirs and files')
        sp.set_defaults(cmd='clean')
        sp.add_argument('-user', '--user', type=str, help='user of subdir or file')
        sp.add_argument('-days', type=str, action='store', default='7 days', help='remove files if more than 7 days')

        # wrapper_cli with extra argments, does not make sense
        # to demonstrate wrapper options
        # --all
        # --files
        # --days
        sp = subparsers.add_parser('wrapper_cli')
        sp.add_argument('--days')
        return parser

    def get_parser(self):
        """
        Example of args of subcmds
        # help of subcmd clean
        tmpdir clean -h
        """
        parser = argparse.ArgumentParser(prog='tmpdir')
        parser.add_argument('--path', action='store_true', default='/tmp', help='path to profile, createsubdir or cleanup')

        subparsers = parser.add_subparsers(help='subparser')

        # create tmpdir with special convention
        parser_create = subparsers.add_parser('create', help='positional arg')

        parser_create.add_argument('--name', type=str, help='name of subdir')

        # should be just --clean in tmpdir cli, this is to show subcmds args
        parser_clean = subparsers.add_parser('clean', help='this cli is positional args, cleanup subdirs and files')
        parser_clean.add_argument('-user', '--user', type=str, help='user of subdir or file')
        parser_clean.add_argument('-days', type=str, action='store', default='7 days', help='remove files if more than 7 days')
        return parser

    def parse_argv(self, argv):
        parser = self.get_parser()
        args = parser.parse_args(argv)
        return args
