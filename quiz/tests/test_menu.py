#!/usr/bin/python
import unittest
import os
import sys
# similar to findBin in Perl
pwd = os.path.dirname(os.path.realpath(__file__))
# 1 level up
base_dir = os.path.join(pwd,'..')
# add to sys.path
sys.path.append(base_dir)

from lib import menu

class MenuTest(unittest.TestCase):
    def test1(self):
        sels = menu.parse_input_string("1,2,3,4")
        self.assertEqual(len(sels),4)

    def test2(self):
        sels = menu.parse_input_string("1 2 3 4")
        self.assertEqual(len(sels),4)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(MenuTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
