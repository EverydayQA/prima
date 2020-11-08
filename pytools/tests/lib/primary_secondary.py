
class Primary(object):

    def __init__(self, param):
        self._param = param

    def process(self):
        if self._param == 1:
            self._do_intermediate_process()
        self._do_process()

    def _do_process(self):
        raise NotImplementedError

    def _do_intermediate_process(self):
        return 'aaa'


class Secondary(object):

    def __init__(self):
        self.scl = Primary(1)

    def method_d(self):
        return self.scl.process()

    def method_a(self, a, b):
        raise Exception('method_a')

    def method_b(self, b):
        raise Exception('method_b')
