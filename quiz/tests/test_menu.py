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

    # menu.py - mock builtin function in other function
    @mock.patch('__builtin__.raw_input')
    def test_select_from_list(self, mock_raw_input):
        mock_raw_input.return_value = '1,2'
        alist=['aaa','bbb','ccc', 'ddd']
        sels = menu.select_from_list(alist)
        print sels
        self.assertEqual(sels,['bbb','ccc'])

    @mock.patch('lib.menu.get_input')
    def test_select_from_list2(self, mock_get_input):
        mock_get_input.return_value = '1 2'
        alist=['aaa','bbb','ccc', 'ddd']
        sels = menu.select_from_list(alist)
        print sels
        self.assertEqual(sels,['bbb','ccc'])
    @mock.patch('__builtin__.raw_input')
    def test_get_input(self, mock_raw_input):
        mock_raw_input.return_value='1,3'
        the_input = menu.get_input()
        self.assertEqual(the_input,'1,3')

    def test_selections_in_list(self):
        sels = [1,3]
        alist=['aaa','bbb','ccc', 'ddd']
        selections = menu.selections_in_list(sels, alist)
        self.assertEqual(selections,['bbb','ddd'])

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(MenuTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
