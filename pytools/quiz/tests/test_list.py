import unittest


class TestList(unittest.TestCase):

    def test_filter(self):
        path = '/shared/xx/yy/zz/aa/bb/cc/'
        items = path.split('/')
        items_new = filter(None, items)
        self.assertEqual(len(items_new), 7)

    # combine, set, sort, reverse
    def test_combine_lists(self):
        path = '/shared/xx/yy/zz/aa/bb/cc/'
        items = path.split('/')
        items2 = list(items)
        items_all = items + items
        self.assertEqual(len(items_all), len(items) + len(items2))

        items_all = list(set(items) | set(items))
        items_all.reverse()
        self.assertEqual(len(items_all), 8)
