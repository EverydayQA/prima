
class SomeClass(object):

    def __init__(self, param):
        self._param = param

    def process(self):
        if self._param == 1:
            self._do_intermediate_process()
        self._do_process()

    def _do_process(self):
        raise NotImplementedError

    def _do_intermediate_process(self):
        pass
