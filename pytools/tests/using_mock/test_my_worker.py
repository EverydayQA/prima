#!/usr/bin/python
import unittest
import mock
from mock import MagicMock
from other.my_worker import MyWorker


def get_value_a():
    return 'a'


def another_method():
    return 'another_method'


def abcd_foo(a, b, c, d):
    value = another_method()
    return value


class TestWorker(unittest.TestCase):

    # my_worker.py - mock away sleep
    @mock.patch('other.my_worker.sleep')
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
        with mock.patch('other.my_worker.MyWorker.nap') as mock_nap:
            mock_nap.return_value = 1000
            worker = MyWorker()
            self.assertEqual(worker.nap(300), 1000)

    def test_using_with_patch_sleep(self):
        # mock away sleep in the module, not the class
        with mock.patch('other.my_worker.sleep') as mock_sleep:
            mock_sleep.return_value = False
            worker = MyWorker()
            self.assertEqual(worker.nap(10), 10 * 5)

    def test_using_with_patch_gevent_sleep(self):
        # mock away module.sleep(since from gevent import sleep)
        with mock.patch('other.my_worker.sleep') as mock_sleep:
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

    @mock.patch('tests.using_mock.test_my_worker.get_value_a')
    def test_get_value_a(self, mock_get_value_a):
        """
        mock does not take effect if method is in the module as the test module? why?
        """
        mock_get_value_a.return_value = 'mocka'
        a = get_value_a()
        self.assertEqual(a, 'a')

    @mock.patch('other.some_methods.get_value_a')
    def test_get_value_a_other(self, mock_get_value_a):
        """
        mock get_value_a() in other module is fine
        this only exists after mock failed if get_value_a() in this test module
        """
        mock_get_value_a.return_value = 'mocka'
        # the import is fine to be here or at top of the module
        from other import some_methods
        a = some_methods.get_value_a()
        self.assertEqual(a, 'mocka')

    @mock.patch('other.some_methods.get_value_a')
    @mock.patch('other.some_methods.another_method', return_value='mocking_another')
    def test_result_other(self, mock_another_method, mock_get_value_a):
        """
        The innermost patch should be the first parameter

        The return_value better to be defined outside the test function with multiple patch
        This is just an example show how multiple patch works
        """
        mock_get_value_a.return_value = 'mocka'
        from other import some_methods as sm
        a = sm.get_value_a()
        self.assertEqual(a, 'mocka')
        result = sm.another_method()
        self.assertEqual(result, 'mocking_another')

    @mock.patch('tests.using_mock.test_my_worker.get_value_a', return_value='mocking_va')
    @mock.patch('tests.using_mock.test_my_worker.another_method', return_value='mocking_another')
    def test_result(self, mock_another_method, mock_get_value_a):
        """
        The innermost patch should be the first parameter
        mock does not take effect if the functions being tested is in the same module as test modle?
        """
        mock_get_value_a.return_value = 'mocka'
        a = get_value_a()
        self.assertEqual(a, 'a')
        result = abcd_foo(a, 'b', 'c', 'd')
        self.assertEqual(result, 'another_method')
