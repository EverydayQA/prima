import pytest
import unittest


@pytest.fixture(scope='module', autouse=True)
def skip_if_this_condition():
    # not the scope usage here
    # the same condtion will appy to all tests if specified
    return 'skipIfCertainCondtion'


skipif = pytest.mark.skipif(func_fixture='skipIfCertainCondition')


class TestSkipWithoutFixture(unittest.TestCase):

    def fixture_sometimes_suck():
        return "fail"

    @pytest.mark.skipif(fixture_sometimes_suck() == 'fail', reason='use good old method to skip')
    def test_setting_value(self):
        print("Hello I am in testcase")

    def test_to_pass(self):
        pass

    @skipif
    def test_to_pass2(self):
        pass

    @pytest.fixture(scope='class', autouse=True)
    def fixture_scope_class(self):
        return 'skipp'

    @skipif
    def test_setting_value2(self):
        print("Hello I am in testcase")
