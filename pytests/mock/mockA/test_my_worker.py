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
        # should nap witout calling sleep()
        worker.nap(5)
        self.assertFalse(mock_sleep.sleep.called, "Fail - sleep really called!")

    def test_worker_with_autospec_2(self):
        # no sleep, the mock_nap.nap.called?
        mock_nap = mock.create_autospec(MyWorker)
        mock_nap.return_value = False
        worker = MyWorker()
        worker.nap = mock_nap
        worker.nap(5)
        self.assertFalse(mock_nap.nap.called, "Fail - autospec nap really called!")

    def test_worker_with_autospec(self):
        mock_worker = mock.create_autospec(MyWorker)
        mock_worker.return_value = False
        mock_worker.nap.return_value = 8
        worker = MyWorker()
        worker.nap = mock_worker.nap
        # test the nap is mock away
        self.assertEqual(worker.nap(5), 8)
        # mock away nap() -- no need to sleep() and test working()
        # sleep n * 4 jogging n * 3, working = sleep + jogging
        # nap 8 (mocked) + jogging n * 3 = 23
        self.assertEqual(worker.working(5), 23)

    # mock class object - cannot access sleep, can only access method.nap(5)
    @mock.patch.object(MyWorker, 'nap')
    def test_worker_obj(self, mock_nap):
        mock_nap.return_value = False
        worker = MyWorker()
        worker.nap(5)
        self.assertFalse(mock_nap.nap.called, "Fail - nap really called!")

    def test_worker_magicMock(self):
        # using mock.MagicMock
        # mock sleep inside.nap(5)
        worker = MyWorker()
        worker.nap = MagicMock(name='nap')
        worker.nap.return_value = 100
        self.assertTrue(worker.nap(5), 100)

    def test_using_with_patch(self):
        with mock.patch('my_worker.MyWorker.nap') as mock_nap:
            mock_nap.return_value = 1000
            worker = MyWorker()
            self.assertEqual(worker.nap(300), 1000)

    def test_using_with_patch_sleep(self):
        # mock away sleep in the module, not the class
        with mock.patch('my_worker.sleep') as mock_sleep:
            mock_sleep.return_value = False
            worker = MyWorker()
            self.assertEqual(worker.nap(10), 10 * 5)

    def test_using_with_patch_gevent_sleep(self):
        # mock away module.sleep(since from gevent import sleep)
        with mock.patch('my_worker.sleep') as mock_sleep:
            mock_sleep.return_value = False
            worker = MyWorker()
            self.assertEqual(worker.nap(10), 10 * 5)

    def test_using_with_patch_gevent_nap(self):
        # mock away gevent.sleep
        with mock.patch('gevent.sleep') as mock_sleep:
            # true/false does not matter, it will bypass the sleep
            mock_sleep.return_value = True
            worker = MyWorker()
            # sleep or not, the value stay the same, this is not the right way to evaluate
            self.assertEqual(worker.gevent_nap(10), 10 * 5)
            mock_sleep.assert_called_with(5)

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
