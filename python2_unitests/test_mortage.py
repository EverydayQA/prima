import unittest
import math


class Mortgage(object):

    def __init__(self, principle_amount, rate_per_year):
        self.principle = principle_amount
        self.rate_per_year = rate_per_year

    @property
    def r(self):
        return self.rate_per_year / 12.0

    def pay_per_month(self, n):
        return self.principle * self.r * math.pow((1 + self.r), n) / (math.pow((1 + self.r), n) - 1)


class TestFixedPaymentMortgage(unittest.TestCase):

    def test_pay_per_month(self):
        mt = Mortgage(100000.00, 0.04)
        a = mt.pay_per_month(10 * 12)
        self.assertEqual(int(a), 1012)
        a = mt.pay_per_month(30 * 12)
        self.assertEqual(int(a), 477)
        a = mt.pay_per_month(25 * 12)
        self.assertEqual(int(a), 527)

    def test_dict_qual(self):
        x = {'type': 'example', 'color': 'blue', 'entries_dict':{'clock':'c', 'id': 1}}
        y = {'color': 'blue', 'entries_dict':{'id': 1, 'clock':'c'}, 'type': 'example'}
        self.assertDictEqual(x, y)
        self.assertEqual(x, y)
