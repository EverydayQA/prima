OTHER_VAR = 'other_var'


class Base(object):
    """"
    Probably the best way of solving the problem is to add class attributes as default values for instance members initialised in __init__(). Note that if you are only setting default attributes in __init__() then providing them via class attributes (shared between instances of course) is faster too. e.g.
    """

    cls_attr = 'cls_attr'

    def __init__(self):
        # instance_member - hardest to patch or mock
        self.instance_var = 'instance_var'

    @property
    def cls_property(self):
        return 'cls_property'

    def show(self):
        # hard to test
        # mock print and assert_called_with?
        print(self.instance_var)

    @staticmethod
    def static_add(x):
        return x * x


class App(object):
    # class attribute, without reference to args/kwargs
    cbase = Base()

    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        # instance member/instance variable
        self.ibase = Base(*args, **kwargs)

    @property
    def pbase(self):
        # class property
        return Base(*self.args, **self.kwargs)
