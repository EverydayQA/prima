#!/usr/bin/python
import unittest
import mock
from mock import MagicMock

# myWorker.py MyWorker(class)
from myWorker import MyWorker

class TestWorker(unittest.TestCase):
    
    # myWorker.py - mock away sleep
    @mock.patch('myWorker.sleep')
    def test_my_worker(self,mock_sleep):
        # mock away the sleep()
        mock_sleep.return_value = False
        worker = MyWorker()
        # should run witout calling sleep()
        worker.run()
        self.assertFalse(mock_sleep.sleep.called,"Fail - sleep really called!")

    # autospec - run() actually being called as well as sleep - but test passed?why???
    # 
    def test_worker_with_autospec(self):
        mock_run = mock.create_autospec(MyWorker)
        mock_run.return_value = False
        worker = MyWorker()
        worker.run()
        self.assertFalse(mock_run.run.called,"Fail - autospec run really called!")

    # mock class object - cannot access sleep, can only access method run()
    @mock.patch.object(MyWorker,'run')
    def test_worker_obj(self, mock_run):
        mock_run.return_value = False
        worker = MyWorker()
        worker.run()
        self.assertFalse(mock_run.run.called,"Fail - run really called!")
        

    # with patch
    
    # mock.Mock
    def test_worker_magicMock(self):

        real_worker = MyWorker()
        real_worker.run = MagicMock(name='run')
        real_worker.return_value = False
        real_worker.run()
        self.assertFalse(real_worker.run.called,"Fail - run really called!")

    # mock.MagicMock



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestWorker)
    unittest.TextTestRunner(verbosity=2).run(suite)
