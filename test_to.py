import time
import unittest
import pytest


class TestDemo(unittest.TestCase):

    @pytest.mark.timeout(60)
    def test_01(self):
        time.sleep(2)
        assert "1"

    @pytest.mark.timeout(3)
    def test_02(self):
        time.sleep(5)
        # input("Please enter your name: ")
        self.assertEqual('a', 'b')

    @pytest.mark.timeout(3)
    def test_03(self):
        time.sleep(1)
        assert "1"
