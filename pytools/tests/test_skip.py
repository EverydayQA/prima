import pytest
import unittest


def skip_test():
    return 1


skipmeif = pytest.mark.skipif("skip_test()==1")


@skipmeif
class TestSkipWithoutFixture(unittest.TestCase):

    def fixture_sometimes_suck():
        return "fail"

    @pytest.mark.skipif(skip_test() == 0, reason='use good old method to skip')
    def test_setting_value(self):
        print("Hello I am in testcase")

    def test_to_pass(self):
        pass

    @skipmeif
    def test_to_pass2(self):
        pass

    @skipmeif
    def test_setting_value2(self):
        print("Hello I am in testcase")
