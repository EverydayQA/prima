#!/usr/bin/python
import codecs
import sys
import gzip
import unittest
import io
class ReadUTF(object):
    def __init__(self):
        pass
    def Jochen_read(self, testdata):
        f = gzip.open(testdata,'rb')
        reader = codecs.getreader('utf-8')
        contents = list(f)
        return contents
    def Yurik_read(self, testdata):
        f = gzip.open(testdata,'rb')
        reader = io.BufferedReader()
        contents = io.TextIOWrapper(reader, encoding='utf8', errors='ignore')
        return contents
    def Gang_read(self, testdata):
        f = gzip.open(testdata,'r')
        contents = list(f)
        return contents

    def comp(self,list1, list2):

        a = list1.pop()
        b = list2.pop()
        return False

    def show_contents(self,contents):
        for line in contents:
            print (line)

    
class TestReadUTF(unittest.TestCase):
    def setUp(self):
        self.testdata = "./src/UTF-8-demo.txt.gz"

    def test_Jochen_read(self):
        reader = ReadUTF()
        contents = reader.Jochen_read(self.testdata)

    def test_Gang_read(self):
        reader = ReadUTF()
        contents = reader.Gang_read(self.testdata)
        expected = reader.Jochen_read(self.testdata)
        size = len(contents)
        size_expected = len(expected)
        self.assertEqual(size ,size_expected)

    def tearDown(self):
        pass

'''
    def test_Yurik_read(self):
        reader = ReadUTF()
        contents = reader.Yurik_read(self.testdata)
        reader.show_contents(contents)
'''

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestReadUTF)
    unittest.TextTestRunner(verbosity=2).run(suite)
        


