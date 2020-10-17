import argparse


class ArgTask(object):
    """
    """

    def parse_known_args(self, argv):
        """
        """
        parser = self.get_parser()
        return parser.parse_known_args(argv)

    def parse_args(self, argv):
        """
        """
        parser = self.get_parser()
        return parser.parse_args(argv)

    def get_parser(self):
        """
        example on how to use to use subparser
        https://pymotw.com/2/argparse/
        """
        parser = argparse.ArgumentParser()
        subparsers = parser.add_subparsers(help='commands')
        # A list command
        list_parser = subparsers.add_parser('list', help='List contents')
        list_parser.add_argument('dirname', action='store', help='Directory to list')

        # A create command
        create_parser = subparsers.add_parser('create', help='Create a directory')
        create_parser.add_argument('dirname', action='store', help='New directory to create')
        create_parser.add_argument('--read-only', default=False, action='store_true',
                                   help='Set permissions to prevent writing to the directory')
        # A delete command
        delete_parser = subparsers.add_parser('delete', help='Remove a directory')
        delete_parser.add_argument('dirname', action='store', help='The directory to remove')
        delete_parser.add_argument('--recursive', '-r', default=False, action='store_true',
                                   help='Remove the contents of the directory, too',)

        return parser
