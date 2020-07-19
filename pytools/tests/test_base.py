#!/usr/bin/python
import mock
import unittest
from nose_tests.fsample import base


class TestB(unittest.TestCase):

    def setUp(self):
        pass

    def test_base(self):
        b = base.Base()
        b.method()
        self.assertEquals('a', 'a')

    # mock.path(file_name_or_module_name.class_name.method_name)
    @mock.patch('nose_tests.fsample.base.Base.method')
    def test_super_method(self, mock_method):
        """
        method being called at base class, not Dase()
        """
        b = base.Base()
        b.method()
        self.assertTrue(mock_method.called)

    # fsample dir
    # base.py
    # Base Class
    # method in Class Base in file base.py in dir.fsample

    @mock.patch("nose_tests.fsample.base.Base.method")
    def test_super_method2(self, mock_super):
        """
        When Dase(True) -- the method() at Dase being called
        """
        base.Dase(test=False).method()
        self.assertFalse(mock_super.called)
        base.Dase(test=True).method()
        self.assertTrue(mock_super.called)
