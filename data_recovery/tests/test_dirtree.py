import unittest
from unittest import mock

from backup_and_recovery.dir_tree import DPath
from backup_and_recovery.dir_tree import TreeInside

def local_walk():
    d = {}
    d['/home/joe'] = ['afile', 'bfile']
    d['/home/thomas'] = ['1.jpg', '3.png']
    return d


class TestDPath(unittest.TestCase):

    def test_d_walk(self):
        dt = DPath('/tmp')
        dpath = dt.dpath
        self.assertTrue(len(dpath.keys()) > 3)

    def test_d_walk_using_mock(self):
        with mock.patch('backup_and_recovery.dir_tree.DPath.d_walk') as mock_walk:
            mock_walk.return_value = local_walk()
            dt = DPath('/tmp')
            dpath = dt.dpath
            self.assertTrue(len(dpath.keys()) == 2)
            expect = ['/home/joe', '/home/thomas']
            self.assertEqual(list(dpath.keys()), expect)


class TestTreeInside(unittest.TestCase):

    def test_d_walk_using_mock(self):
        with mock.patch('backup_and_recovery.dir_tree.DPath.d_walk') as mock_walk:
            mock_walk.return_value = local_walk()
            dt = DPath('/tmp')
            dpath = dt.dpath
            self.assertTrue(len(dpath.keys()) == 2)
            expect = ['/home/joe', '/home/thomas']
            self.assertEqual(list(dpath.keys()), expect)
            ti = TreeInside('/tmp')
            self.assertEqual(list(ti.dpath.keys()), expect)
