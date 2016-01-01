#!/usr/bin/python
import unittest
from mock import patch
import sys,os
pwd = os.path.dirname(os.path.realpath(__file__))
basedir = os.path.join(pwd,'..')
print basedir
sys.path.append(basedir)
from lib import MyWorker

class TestWorker(unittest.TestCase):
    def setUp(self):
        self.patcher = patch('MyWorker.sleep')
        self.patcher.start()

    def tearDown(self):
        self.patcher.stop()

    def Test_my_worker(self):
        self.assertTrue(TestWorker.run()) 

# this example is fishy in the usage of mock patch,why and how?!
# gliang Dec 12, 31, 2015
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestWorker)
    unittest.TextTestRunner(verbosity=2).run(suite)
