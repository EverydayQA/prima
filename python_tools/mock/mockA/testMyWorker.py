# TestMyWorker.py
#!/usr/bin/python
import unittest
import mock

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

     # mock class object

     # with patch

     # mock.Mock

     # mock.MagicMock



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestWorker)
    unittest.TextTestRunner(verbosity=2).run(suite)
