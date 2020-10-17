import unittest
import mock
from other.fsample.child import Child
from StringIO import StringIO


class TestChild(unittest.TestCase):

    def test_age(self):
        ch = Child('bob', 2)
        self.assertEqual(ch.age, 2)

    def test_check(self):
        ch = Child('bob', 2)
        self.assertEqual(ch._Child__check(), None)
        with mock.patch('sys.stdout', new_callable=StringIO) as mock_out:
            ch = Child('bob', 2)
            self.assertEqual(ch._Child__check(), None)
            self.assertEqual(mock_out.getvalue(), '2\n')
