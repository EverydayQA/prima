import os


class DataDir(object):

    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def __repr__(self):
        return 'DataDir({0}, {1})'.format(self.jason_dir, self.jason_dir_to_delete)

    def __str__(self):
        return 'An instance of DataDir(json_dir: {0}, json_dir_to_delete: {1})'.format(self.json_dir, self.json_dir_to_delete)

    @property
    def json_dir(self):
        dirname = os.path.dirname(__file__)
        json_dir = os.path.join(dirname, '../data')
        return json_dir

    @property
    def json_dir_to_delete(self):
        return os.path.join(self.json_dir, 'to_delete')
