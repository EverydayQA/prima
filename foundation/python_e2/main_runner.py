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

    def testResize(self):
        self.widget.resize(100,100)
        self.assertEqual(self.widget.getSize(),(100,100))



if __name__ == "__main__":
    unittest.main()

