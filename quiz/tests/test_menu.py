#!/usr/bin/python
import unittest
import os
import sys
import mock
# similar to findBin in Perl
pwd = os.path.dirname(os.path.realpath(__file__))
# 1 level up
base_dir = os.path.join(pwd,'..')
# add to sys.path
sys.path.append(base_dir)

from lib import menu
from lib import color_print

class MenuTest(unittest.TestCase):
    def test1(self):
        sels = menu.parse_input_string("1,2,3,4")
        self.assertEqual(len(sels),4)

    def test2(self):
        sels = menu.parse_input_string("1 2 3 4")
        cp = color_print.ColorPrint()

        for sel in sels:
            cp.printout(sel + '\n', cp.GREEN)
        self.assertEqual(len(sels),4)

    # menu.py has no class
    @mock.patch('__builtin__.raw_input')
    def test_select_from_list(self, mock_raw_input):
        mock_raw_input.return_value = '1,2'
        alist=['aaa','bbb','ccc', 'ddd']
        sels = menu.select_from_list(alist)
        print sels
        self.assertEqual(sels,['bbb','ccc'])

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(MenuTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
