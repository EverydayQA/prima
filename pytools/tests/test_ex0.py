#!/usr/bin/python
import mock
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

    def test_mock_return(self):
        fake_input = mock.MagicMock()
        fake_input.ops.list.return_value = []

        result = check_method_return(fake_input)
        self.assertFalse(result)

    def test_mock_len(self):
        fake_input = mock.MagicMock()
        fake_input.ops.list.return_value = []

        result = check_method_len(fake_input)
        self.assertFalse(result)


if __name__ == '__main__':
    test_empty = []
    if not test_empty:
        print("empty list equals to False")

    unittest.main()
