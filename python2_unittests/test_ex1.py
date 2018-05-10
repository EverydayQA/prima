import mock
import sys
import unittest


def check_method_return(input):
    return_value = input.ops.list()
    if not return_value:
        return False
    return return_value


def check_method_len(input):
    return_value = input.ops.list()
    if len(return_value) < 1:
        return False
    return return_value


class TestMockReturnValue(unittest.TestCase):

    def test_mock_input(self):
        # mock input
        fake_input = mock.MagicMock(name='input')
        # set mock_input.ops.list.return_value to empty
        fake_input.ops.list.return_value = []
        # use mock_input as parameter
        result = check_method_return(fake_input)
        self.assertFalse(result)

    def test_mock_len(self):
        fake_input = mock.MagicMock()
        fake_input.ops.list.return_value = []
        result = check_method_len(fake_input)
        self.assertFalse(result)


class MyResult(unittest.runner.TextTestResult):
    items = ['xxx']

    def __init__(self, *args, **kwargs):
        super(MyResult, self).__init__(*args, **kwargs)

    def addError(self, test, err):
        self.call_web_api(test, err)
        return super(MyResult, self).addError(test, err)

    def addFailure(self, test, err):
        self.call_web_api(test, err)
        return super(MyResult, self).addFailure(test, err)

    def call_web_api(self, test, err):
        print('***', test, err)

    def addSuccess(self, test):
        super(MyResult, self).addSuccess(test)
        self.items.append(test)


class MyOwnResultClass(unittest.runner.TextTestResult):
    foo = None

    def __init__(self, foo):
        self.foo = foo

    def __iter__(self):
        yield "Result: {f}".format(f=self.foo)

    def MyOwnResult(self, foo):
        yield "Result: {f}".format(f=foo)


if __name__ == '__main__':
    """
    None of the resultclass works!?
    """
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestMockReturnValue))
    runner = unittest.TextTestRunner()
    runner.resultclass = MyResult
    runner.verbosity = 2
    testResult = runner.run(suite)
    for t in testResult.failures:
        print t[0].id()
        print t[1]
    print
    for t in testResult.errors:
        print t[0].id()
        print t[1]
    print
    for t in testResult.items:
        print t
    print
    sys.exit(0)
