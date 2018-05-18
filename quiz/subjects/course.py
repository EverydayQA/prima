from pprint import pprint
from argparse import Namespace


class Course(object):

    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        pprint(self.kwargs)

    @property
    def ns(self):
        """
        restore namespace from cli
        """
        d = self.kwargs.get('d_cli', {})
        return Namespace(**d)

    @property
    def semester(self):
        return 'fall'

    @property
    def year(self):
        return '2018'
