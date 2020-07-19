import unittest
import a


class TestA(unittest.TestCase):

    def test_hello(self):
        self.assertEqual(a.hello(), None)
