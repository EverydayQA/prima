import unittest
import os


class PathItems(object):

    def __init__(self, path):
        try:
            path = os.path.abspath(path)
        except:
            pass

        items = []
        try:
            items = path.strip('/').split('/')
        except:
            pass
        self.path = path
        self.items = items


class TestSplit(unittest.TestCase):

    def test_split(self):
        path = '/shared/xx/yy/zz/aa/bb/cc/'
        items = path.split('/')
        path_back = '/'.join(items)
        self.assertEqual(path, path_back)

    def test_split_append(self):
        path = '/shared/xx/yy/zz/aa/bb/cc/'
        items = path.strip('/').split('/')
        self.assertEqual(len(items), 7)
        items.append('')
        items.insert(1, 'level2')
        items.insert(0, '')
        path_back = '/'.join(items)
        self.assertEqual(path_back, path)
        items = []
        items.append('')
        items.insert(0, '')

    def test_split2(self):
        path = '/shared/xx/yy/zz/aa/bb/cc/'
        items = path.strip('/').split('/')
        self.assertEqual(len(items), 7)

        path2 = '/shared/xx//yy/zz/aa/bb/cc/'
        path2 = os.path.abspath(path2)
        items = path2.strip('/').split('/')
        self.assertEqual(len(items), 7)

    def test_split_path3(self):
        path = None
        pi = PathItems(path)
        self.assertEqual(len(pi.items), 0)
        self.assertEqual(pi.path, None)

    def test_split_path4(self):
        path = '/aa/./xx//yy/zz/aa/bb/cc/'
        pi = PathItems(path)
        self.assertEqual(len(pi.items), 7)
        self.assertEqual(pi.path, '/aa/xx/yy/zz/aa/bb/cc')

    def test_split_path5(self):
        path = '/aa/./xx//yy/zz/aa/bb/cc/..'
        pi = PathItems(path)
        self.assertEqual(len(pi.items), 6)
        self.assertEqual(pi.path, '/aa/xx/yy/zz/aa/bb')
