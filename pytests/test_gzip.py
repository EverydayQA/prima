#!/usr/bin/python
import os
import codecs
import gzip
import unittest
import io


class ReadUTF(object):

    def __init__(self):
        pass

    def Jochen_read(self, testdata):
        f = gzip.open(testdata, 'rb')
        reader = codecs.getreader('utf-8')
        contents = list(f)
        return contents

    def Yurik_read(self, testdata):
        f = gzip.open(testdata, 'rb')
        reader = io.BufferedReader()
        contents = io.TextIOWrapper(reader, encoding='utf8', errors='ignore')
        return contents

    def Gang_read(self, testdata):
        f = gzip.open(testdata, 'r')
        contents = list(f)
        return contents

    def comp(self, list1, list2):
        list1.pop()
        list2.pop()
        return False

    def show_contents(self, contents):
        for line in contents:
            print (line)


class TestReadUTF(unittest.TestCase):

    def setUp(self):
        path = os.path.dirname(__file__)
        self.testdata = os.path.join(path, "./data/empty.txt")

    def test_Jochen_read(self):
        reader = ReadUTF()
        contents = reader.Jochen_read(self.testdata)

    def test_Gang_read(self):
        reader = ReadUTF()
        contents = reader.Gang_read(self.testdata)
        expected = reader.Jochen_read(self.testdata)
        size = len(contents)
        size_expected = len(expected)
        self.assertEqual(size, size_expected)
