
import unittest
import click
from click.testing import CliRunner
import cli.CLI as a

class TestCLI(unittest.TestCase):
    def setUp(self):
        self.runner1 = CliRunner()
        self.runner2 = CliRunner()
        self.args1 = 'arguments 1'
        self.args2 = 'arguments 2'
    def tearDown(self):
        self.runner1 = None
        self.runner2 = None
        self.args1 = None
        self.args2 = None

    def test_1(self):
        result1 = self.runner1.invoke(a.startCLI, self.args1)
        print(result1.output)
        #print console output; is showed
        result2 = self.runner2.invoke(a.startCLI, self.args2)
        print(result2.output)
        #print console output; is blank
