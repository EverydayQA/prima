#!/usr/bin/python
import unittest
from tip import tip_amount

class TipTest(unittest.TestCase):
    def test1(self):
        # comment - 20% tip for 20 dollar
        tip = tip_amount(20,0.2)
        self.assertEqual(tip,4)

    def test2(self):
        # 15% tip of 40 dollar
        tip = tip_amount(40,0.15)
        self.assertEqual(tip,8)


if __name__ == '__main__':
    unittest.main()


