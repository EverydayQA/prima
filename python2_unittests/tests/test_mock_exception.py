import mock
import math
import unittest


class MathOverFlow(object):

    def cal_exp(self, num):
        try:
            ans = math.exp(num)
        except OverflowError:
            ans = 999
        return ans


class TestMathOverFlow(unittest.TestCase):

    def test_cal_exp(self):
        mo = MathOverFlow()
        ans = mo.cal_exp(2222222)
        self.assertEqual(ans, 999)

    def test_cal_exp2(self):
        with self.assertRaises(OverflowError):
            mock_args = {'side_effect': OverflowError}
            with mock.patch('python2_unittests.tests.test_mock_exception.MathOverFlow.cal_exp', **mock_args):
                MathOverFlow().cal_exp(2)

    def test_cal_exp3(self):
        mock_args = {'side_effect': OverflowError}
        with mock.patch('python2_unittests.tests.test_mock_exception.MathOverFlow.cal_exp', **mock_args):
            self.assertRaises(OverflowError, MathOverFlow().cal_exp, 2)
