#!/usr/bnin/python
import unittest
import os


class TestList(unittest.TestCase):

    def test_filter(self):
        path = '/shared/xx/yy/zz/aa/bb/cc/'
        items = path.split('/')
        print items
        items_new = filter(None, items)
        print items_new
        self.assertEqual(len(items_new), 7)

    # combine, set, sort, reverse
    def test_combine_lists(self):
        path = '/shared/xx/yy/zz/aa/bb/cc/'
        items = path.split('/')
        items2 = list(items)
        items_all = items + items
        self.assertEqual(len(items_all), len(items) + len(items2))
        print items_all

        items_all = list(set(items) | set(items))
        print items_all
        items_all.reverse()
        print items_all
        self.assertEqual(len(items_all), 8)
        
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestList)
    unittest.TextTestRunner(verbosity=2).run(suite)
