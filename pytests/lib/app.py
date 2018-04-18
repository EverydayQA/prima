

class Base(object):

    ccls_attr = 'cls_attr'

    def __init__(self):
        self.iinstance_attr = 'instance_attr'

    @property
    def ccls_property(self):
        return 'cls_property'

    def show(self):
        print(self.instance_attr)


class App(object):

    def __init__(self):
        self.bbase = Base()
