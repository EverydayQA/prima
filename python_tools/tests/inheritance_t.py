#!/usr/bin/python
import mock, unittest
import os,sys
pwd = os.path.dirname(os.path.realpath(__file__))
basedir = os.path.join(pwd,'..')
sys.path.append(basedir)
from lib import inheritance

class TestB(unittest.TestCase):

    @mock.patch("lib.inheritance.A.method")
    def test_super_method(self, mock_super):
        B(True).method()
        self.assertTrue(mock_super.called)

    @mock.patch("lib.inheritance.A.method")
    def test_super_method(self, mock_super):
        inheritance.B(False).method()
        self.assertFalse(mock_super.called)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestB)
    unittest.TextTestRunner(verbosity=2).run(suite)
