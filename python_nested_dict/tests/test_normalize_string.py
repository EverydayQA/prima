import unittest
from python_nested_dict.src.normalize_string import NormalizeString


class TestNormalizeString(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.nm = NormalizeString()

    def test_r_strip(self):
        key = ' 1234 ]-: '
        nkey = self.nm.r_strip(key)
        self.assertEqual(nkey, '1234 ]-')

    def test_normalize_key(self):
        key = ' 1234 ]-: '
        nkey = self.nm.normalize_key(key)
        self.assertEqual(nkey, '1234-]-')

    def test_normalize_value(self):
        v = '    sth stupid ;'
        nv = self.nm.normalize_value(v)
        self.assertEqual(nv, 'sth stupid')
