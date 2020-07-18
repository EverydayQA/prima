from ..src.parse_line import DParseLine
import unittest


class TestDparseLine(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.line1 = '		dicom_0x0028:el_0x0030 = "0.859375\\0.859375 " ;'
        cls.dpl = DParseLine(cls.line1)
        pass

    def test_deep_set(self):
        pass

    def test_d_keys_value(self):
        d = self.dpl.d_keys_value(self.line1)
        keys = d.get('subkeys', [])
        self.assertEqual(keys, ['dicom_0x0028', 'el_0x0030'])
        value = d.get('value', None)
        self.assertEqual(value, '0.859375\\0.859375')

    def test_d_deep_set_keys_value(self):
        """
        a test file with expected results
        """
        d = self.dpl.d_keys_value(self.line1)
        from ..src.nested_dict import NestedDict
        nd = NestedDict()
        dd = self.dpl.d_deep_set_keys_value(d.get('subkeys', []), d.get('value', None))
        self.assertEqual(dd, {'dicom_0x0028': {'el_0x0030': '0.859375\\0.859375'}})
