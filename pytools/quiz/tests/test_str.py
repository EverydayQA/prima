#!/usr/bnin/python
import unittest
import os
import re

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
    def test_compare_number(self):
        str1 = 'aaa.2016-06-07.12:22:34:34.abc'
        str2 = 'aaae.2016-06-08.11:22:34:34.abcd'
        str1_num = re.sub('\D','',str1)
        str2_num = re.sub('\D','',str2)
        self.assertTrue(str1_num<str2_num)
        self.assertTrue(int(str1_num)<int(str2_num))

    # test str keep alnumeric
    # test and get familiar with string manipulation
        
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSplit)
    unittest.TextTestRunner(verbosity=2).run(suite)

