#!/usr/bin/python
import unittest
import mock
from mock import MagicMock
# my_worker.py MyWorker(class)
from my_worker import MyWorker


def value_a():
    return 'a'


def another_method():
    return 'another_method'


def abcd_foo(a, b, c, d):
    value = another_method()
    return value


class TestWorker(unittest.TestCase):

    # my_worker.py - mock away sleep
    @mock.patch('my_worker.sleep')
    def test_my_worker(self, mock_sleep):
        # mock away the sleep()
        mock_sleep.return_value = False
        worker = MyWorker()
        # should run witout calling sleep()
        worker.run()
        self.assertFalse(mock_sleep.sleep.called, "Fail - sleep really called!")

    def test_worker_with_autospec_2(self):
        # no sleep, the mock_run.run.called?
        mock_run = mock.create_autospec(MyWorker)
        mock_run.return_value = False
        worker = MyWorker()
        worker.run = mock_run
        worker.run()
        self.assertFalse(mock_run.run.called, "Fail - autospec run really called!")

    def test_worker_with_autospec(self):
        # autospec - run() actually being called as well as sleep - but test passed?why???
        # not working
        mock_run = mock.create_autospec(MyWorker)
        mock_run.return_value = False
        worker = MyWorker()
        worker.run()
        self.assertFalse(mock_run.run.called, "Fail - autospec run really called!")

    # mock class object - cannot access sleep, can only access method run()
    @mock.patch.object(MyWorker, 'run')
    def test_worker_obj(self, mock_run):
        mock_run.return_value = False
        worker = MyWorker()
        worker.run()
        self.assertFalse(mock_run.run.called, "Fail - run really called!")

    def test_worker_magicMock(self):
        # using mock.MagicMock
        # not working
        real_worker = MyWorker()
        real_worker.run = MagicMock(name='run')
        real_worker.run()
        self.assertFalse(real_worker.run.called, "Fail - run really called!")

    def test_using_with_patch(self):
        # not working
        with mock.patch('MyWorker') as mock_worker:
            mock_worker.run = False
            worker = MyWorker()
            worker.run()
            self.assertFalse(worker.run.called, 'F called')

    # mock.Mock

    @mock.patch('test_my_worker.value_a', return_value='mocking_va')
    @mock.patch('test_my_worker.another_method', return_value='mocking_another')
    def test_result(self, mock_value_a, mock_another_method):
        """
        The return_value better to be defined outside the test function with multiple patch
        This is just an example show how multiple patch works
        """
        a = value_a()
        self.assertEqual(a, 'mocking_va')
        result = abcd_foo(a, 'b', 'c', 'd')
        self.assertEqual(result, 'mocking_another')


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestWorker)
    unittest.TextTestRunner(verbosity=2).run(suite)
