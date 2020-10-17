from other.fsample import pop_item
import unittest


class TestPopItem(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.pop = pop_item.PopItem()

    def test_popitem(self):
        item = self.pop.popitem()
        self.assertTrue(item in (2, ('a', 'A'), ('b', 'B')))
