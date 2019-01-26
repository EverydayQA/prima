import unittest
import b


class TestB(unittest.TestCase):

    def test_bye(self):
        self.assertEqual(b.bye(), None)
