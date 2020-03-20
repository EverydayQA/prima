#!/usr/bin/python3.5
import unittest
import sys
from nose_tests.lib import Interpreter
from unittest import mock
from io import StringIO
import io


class CmdUiTest(unittest.TestCase):

    def setUp(self):
        self.mock_stdin = mock.create_autospec(sys.stdin)
        self.mock_stdout = mock.create_autospec(sys.stdout)

    # not working
    def create(self):
        return Interpreter.Interpreter(stdin=self.mock_stdin, stdout=self.mock_stdout)

    # not working
    def _last_write(self, nr=None):
        """:return: last `n` output lines"""
        if nr is None:
            return self.mock_stdout.write.call_args[0][0]
        return "".join(map(lambda c: c[0][0], self.mock_stdout.write.call_args_list[-nr:]))

    def test_show_command(self):
        # Interpreter obj - mock
        cli = self.create()
        with mock.patch('sys.stdout', new=io.StringIO('xxx')) as fakeOutput:
            self.assertEqual('xxx', fakeOutput.getvalue().strip())


if __name__ == '__main__':
    unittest.main()
