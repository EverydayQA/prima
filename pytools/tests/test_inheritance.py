#!/usr/bin/python
import mock
import unittest
from myutils import inheritance


class TestB(unittest.TestCase):

    @mock.patch("myutils.inheritance.A.method")
    def test_super_method(self, mock_super):
        inheritance.B(True).method()
        self.assertTrue(mock_super.called)

    @mock.patch("myutils.inheritance.A.method")
    def test_super_method2(self, mock_super):
        inheritance.B(False).method()
        self.assertFalse(mock_super.called)
