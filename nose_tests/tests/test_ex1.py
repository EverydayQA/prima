import mock
import sys
import unittest
from python2_unittests.fsample.input_cls import GameDisplay
from StringIO import StringIO


def get_input():
    a = input('please type:')
    return a


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

    @mock.patch('__builtin__.input')
    def test_get_input(self, mock_input):
        mock_input.return_value = 'mocked_input'
        a = get_input()
        self.assertEqual(a, 'mocked_input')

    @mock.patch('sys.stdout', new_callable=StringIO)
    @mock.patch('__builtin__.raw_input', lambda _: 'a')
    def test_prompt_output4(self, mock_input, mock_stdout):
        """
        Test the terminal print
        """
        p = GameDisplay.prompt2('Choose 0: ')
        self.assertEqual(p, 'a')
        self.assertEqual(mock_stdout.getvalue(), 'Choose 0: \n')

    @mock.patch('__builtin__.input', return_value='0')
    def skip_prompt_output3(self, mock_input):
        """
        This is an example code that should not work
        """
        p = GameDisplay.prompt('Choose 0: ')
        self.assertEqual(p, '0')
        self.assertEqual(sys.stdout.getvalue(), 'Choose 0: \n')

    @mock.patch('__builtin__.input', return_value='0')
    def skip_prompt_output(self, mock_input):
        """
        Not working example, mock_stdout cannot catch the output
        """
        with mock.patch('sys.stdout', new=StringIO()) as mock_stdout:
            p = GameDisplay.prompt('Choose 0: ')
            self.assertEqual(p, '0')
            self.assertEqual(mock_stdout.getvalue(), 'Choose 0: \n')

    @mock.patch('python2_unittests.fsample.input_cls.GameDisplay.prompt', return_value='0')
    def test_prompt_output2(self, mock_prompt):
        """
        prompt being mocked, the return value should be xxx
        """
        with mock.patch('sys.stdout', new=StringIO("xxx")) as mock_stdout:
            p = GameDisplay.prompt('Choose 0: ')
            self.assertEqual(p, '0')
            self.assertEqual(mock_stdout.getvalue(), 'xxx')

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
