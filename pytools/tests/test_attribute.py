#!/usr/bin/env python
import unittest
import re

class Attribute(object):
    def __init__(self):
        self.fulltext = 'a\nb\nc\n\n1\n2\n'

    def remove_newline(self, text):
        txt_new = text
        txt_new = re.sub('\n+', '', txt_new)
        return txt_new

    def remove_newline_class_attr(self):
        self.fulltext = re.sub('\n+', '', self.fulltext)
        return self.fulltext

class TestAttribute(unittest.TestCase):

    def setUp(self):
        attr = Attribute()
        self.attr = attr
        self.txt_wo_newline = 'abc12'

    def test_remove_newline(self):
        fulltext = self.attr.fulltext
        txt = self.attr.remove_newline(fulltext)
        self.assertEquals(txt, self.txt_wo_newline)
        
    def test_property_no_change(self):
        fulltext = self.attr.fulltext
        txt = self.attr.remove_newline_class_attr()
        self.assertEquals(txt, self.attr.fulltext)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestAttribute)
    unittest.TextTestRunner(verbosity=2).run(suite)
    
