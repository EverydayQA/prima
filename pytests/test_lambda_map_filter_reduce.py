import unittest
import math


class LambdaFilterMapReduce(object):

    def __init__(self):
        pass

    def lambda_add(self, x, y):
        # lambda argument_list: expression
        f = lambda x, y: x + y
        return f(x, y)

    def map_add(self):
        # r = map(func, seq)
        lv = range(0, 5)
        return map(math.sqrt, lv)


class TestLambdaFilterMapReduce(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.lamb = LambdaFilterMapReduce()

    def test_lambda_add(self):
        v = self.lamb.lambda_add(3, 4)
        self.assertEqual(v, 7)

    def test_map_add(self):
        lv = self.lamb.map_add()
        self.assertEqual(lv, [0.0, 1.0, 1.4142135623730951, 1.7320508075688772, 2.0])
        lv = map(lambda x, y: x + y, range(0, 5), range(0, 5))
        self.assertEqual(lv, [0, 2, 4, 6, 8])
        lv = map(lambda x: math.sqrt(x), range(0, 5))
        self.assertEqual(lv, [0.0, 1.0, 1.4142135623730951, 1.7320508075688772, 2.0])
        lv = map(math.sqrt, range(0, 5))
        self.assertEqual(lv, [0.0, 1.0, 1.4142135623730951, 1.7320508075688772, 2.0])
