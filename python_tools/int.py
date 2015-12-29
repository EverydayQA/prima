#!/usr/bin/python3.5
import unittest
import unittest.mock
import sys
import os
pwd = os.path.dirname(os.path.realpath(__file__))
sys.path.append(pwd)
import main_not
from unittest.mock import patch
from io import StringIO

class CmdUiTest(unittest.TestCase):
    def setUp(self):
        self.mock_stdin = unittest.mock.create_autospec(sys.stdin)
        self.mock_stdout = unittest.mock.create_autospec(sys.stdout)

    def create(self):
        return main_not.Interpreter(stdin=self.mock_stdin, stdout=self.mock_stdout)

    def _last_write(self, nr=None):
        """:return: last `n` output lines"""
        if nr is None:
            return self.mock_stdout.write.call_args[0][0]
        return "".join(map(lambda c: c[0][0], self.mock_stdout.write.call_args_list[-nr:]))

    def test_show_command(self):
        # Interpreter obj
        cli = self.create()
        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            #print ('hello world')
            self.assertFalse(cli.onecmd('show'))
        self.assertEqual('Hello World!', fakeOutput.getvalue().strip())

def main():
    unittest.main()

if __name__ == '__main__':
    main()

#print ("\n*** CmdUiTest\n")
#CmdUiTest('test_show_command').run() 

