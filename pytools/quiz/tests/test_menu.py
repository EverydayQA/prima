#!/usr/bin/python
import unittest
import mock
from myutils.menu import Menu


class MenuTest(unittest.TestCase):

    @mock.patch('myutils.menu.Menu.get_input')
    def test_select_from_menu(self, mock_raw_input):
        mock_raw_input.return_value = '2'
        alist = ['aaa', 'bbb', 'ccc', 'ddd']
        menu = Menu()
        sels = menu.select_from_menu(alist, 'select')
        self.assertEqual(sels, ['ccc'])

    @mock.patch('myutils.menu.Menu.get_input')
    def test_select_from_menu2(self, mock_get_input):
        mock_get_input.return_value = '1 2'
        alist = ['aaa', 'bbb', 'ccc', 'ddd']
        menu = Menu()
        sels = menu.select_from_menu(alist, 'select')
        self.assertEqual(sels, ['bbb', 'ccc'])

    def test_get_valid_items(self):
        sels = [1, 3]
        alist = ['aaa', 'bbb', 'ccc', 'ddd']
        menu = Menu()
        selections = menu.get_valid_items(sels, alist)
        self.assertEqual(selections, ['bbb', 'ddd'])


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(MenuTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
