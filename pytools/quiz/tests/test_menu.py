import unittest
import mock
from myutils.menu import Menu


class MenuTest(unittest.TestCase):

    @mock.patch('myutils.menu.Menu.get_input')
    def test_select_from_menu(self, mock_get_input):
        mock_get_input.return_value = '2'
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

    def test_parse_selected_input(self):
        pass

    def test_get_input(self):
        """
        timeout
        """
        pass

    def test_pre_selection(self):
        # items, prompt):
        men = Menu()
        sth = men.pre_selection([1, 2], 'ok')
        self.assertEqual(sth, None)

    def select_once(self):
        # items, prompt, timeout=20):
        pass

    def test_get_valid_items2(self):
        # sels, items):
        pass

    def test_select_from_menu3(self):
        # items, prompt, cycle=3, timeout=30):
        pass
