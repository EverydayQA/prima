
# using module or class
DATA = 'data'
CLI = 'cli'


class ConstCourse(object):
    __slots__ = ()
    ENGLISH = 'English'
    MATH = 'Mathmatics'
    AI = 'Pytorch'


class SubdirConst(object):
    ARG = 'arg'

    def __init__(self):
        self.data = DATA

    @property
    def cli(self):
        return 'cli'

    @property
    def arg(self):
        return self.ARG
