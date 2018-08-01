#!/usr/bin/python
import mock
import unittest
from pytools.lib import inheritance


class TestB(unittest.TestCase):

    @mock.patch("pytools.lib.inheritance.A.method")
    def test_super_method(self, mock_super):
        inheritance.B(True).method()
        self.assertTrue(mock_super.called)

    @mock.patch("pytools.lib.inheritance.A.method")
    def test_super_method2(self, mock_super):
        inheritance.B(False).method()
        self.assertFalse(mock_super.called)
