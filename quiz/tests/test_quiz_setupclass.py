#!/usr/bin/python
import unittest
import os
import sys
import mock
import argparse
from ..lib import menu
from ..lib import color_print

def setUpModule():
    pass
def tearDownModule():
    pass

class QuizUnitTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print 'setup once'
        cls._testdir = '/tmp/testdir'
        cls._testfile = 'test.json'
    @classmethod
    def tearDownClass(cls):
        cls._testdir = ''
        cls._testfile =''

class QuizQATest(QuizUnitTest):
    @classmethod
    def setUpClass(cls):
        super(QuizQATest, cls).setUpClass()
        cls._img = 'test.png'
        print 'setup img once'

    @classmethod
    def tearDownClass(cls):
        super(QuizQATest, cls).tearDownClass()
        cls._img = ''

    def setUp(self):
        print 'setup'

    def tearDown(self):
        print 'tear donw'

    def test_testdir(self):
        self.assertEqual(self._testdir, '/tmp/testdir')

    def test_testfile(self):
        self.assertEqual(self._testfile, 'test.json')
    def test_testimg(self):
        self.assertEqual(self._img, 'test.png')

