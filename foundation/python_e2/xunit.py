#!/usr/bin/python
from widget import Widget
import unittest

class WidgetTestCase(unittest.TestCase):
    def setUp(self):
        self.widget = Widget()
    def tearDown(self):
        self.widget = None

    def testSize(self):
        self.assertEqual(self.widget.getSize(),(40,40))

def suite():
    suite = unittest.TestSuite()
    suite.addTest(WidgetTestCase("testSize"))
    return suite

if __name__ == "__main__":
    unittest.main(defaultTest ='suite')

