
class Main(object):

    def __init__(self, my_var=None):
        self.var = my_var

    def internal_func(self, var=10):
        my_var = var + 20
        return my_var

    def test_func(self):
        val = self.internal_func(20)
        return val + 40
