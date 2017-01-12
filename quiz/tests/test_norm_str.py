#!/usr/bin/python
import unittest
import os
import sys
import mock
import argparse
from ..lib import menu
from ..lib import color_print

class NormStr(object):
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
    @property
    def str_org(self):
        return self.kwargs.get('org', None)
    @property
    def levels(self):
        return self.kwargs.get('levels', None)

    def norm_str(self, org, order):
        pass

class TestNormStr(unittest.TestCase):
    def test_to_pass(self):
        self.assertTrue(True)
    

