#!/usr/bin/python
import unittest
import mock
import sys
import os
import array
pwd = os.path.dirname(os.path.realpath(__file__))
basedir = os.path.join(pwd,'..')
sys.path.append(basedir)
from lib import mqueue

class EnqueueTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_enqueue(self):
        queue = mqueue.MQueue(3)
        actual_result = queue.enqueue(2)
        self.assertTrue(actual_result is True)
        self.assertTrue(queue.size ==1) 
        self.assertTrue(queue.head ==0) 
        self.assertTrue(queue.tail ==1) 

class DequeueTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_dequeue(self):
        queue = mqueue.MQueue(3)
        #dequeue an empty queue
        actual_result = queue.dequeue()
        self.assertTrue(actual_result is True)
        self.assertTrue(queue.size ==1) 
        self.assertTrue(queue.head ==0) 
        
        

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(EnqueueTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
    suite = unittest.TestLoader().loadTestsFromTestCase(DequeueTest)
    unittest.TextTestRunner(verbosity=2).run(suite)

