#!/usr/bnin/python
import unittest
import os


class TestSplit(unittest.TestCase):

    def test_split2(self):
        path = '/shared/xx/yy/zz/aa/bb/cc/'
        items = path.strip('/').split('/')
        print items
        self.assertEqual(len(items), 7)

        path2 = '/shared/xx//yy/zz/aa/bb/cc/'
        path2 = os.path.abspath(path2)
        items = path2.strip('/').split('/')
        print items
        self.assertEqual(len(items), 7)

    # test str keep alnumeric
    # test and get familiar with string manipulation
        
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSplit)
    unittest.TextTestRunner(verbosity=2).run(suite)

