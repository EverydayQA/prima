from python2_unittests.fsample import pop_item
import unittest


class TestPopItem(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.pop = pop_item.PopItem()

    def test_popitem(self):
        ta = self.pop.popitem()
        self.assertEqual(ta, ())
