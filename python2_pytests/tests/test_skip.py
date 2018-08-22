import pytest
import unittest


class TestSkipWithoutFixture(unittest.TestCase):

    def fixture_sometimes_suck():
        return "fail"

    @pytest.mark.skipif(fixture_sometimes_suck() == 'fail', reason='use good old method to skip')
    def test_setting_value(self):
        print("Hello I am in testcase")

    def test_to_pass(self):
        pass
