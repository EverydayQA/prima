#!/usr/bin/python
import mock
import unittest
from python2_unittests.fsample import base


class TestB(unittest.TestCase):

    def setUp(self):
        pass

    def test_base(self):
        b = base.Base()
        b.method()
        self.assertEquals('a', 'a')

    # inappropriate call here for the structure
    # Base is a Class - cannot use this way
    # mock.path(file_name.class_name.method_name)
    @mock.patch('python2_unittests.fsample.base.Base.method')
    def test_super_method(self, mock_super):
        b = base.Base()
        b.method()
        self.assertTrue(mock_super.called)

    # fsample dir
    # base.py
    # Base Class
    # method in Class Base in file base.py in dir.fsample

    @mock.patch("python2_unittests.fsample.base.Base.method")
    def test_super_method2(self, mock_super):
        base.Dase(False).method()
        self.assertFalse(mock_super.called)
        base.Dase(True).method()
        self.assertFalse(mock_super.called)
