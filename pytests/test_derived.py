#!/usr/bin/python
import mock
import unittest
from pytests.lib import derived

# this example has not been sorted out yet
# do not use it !!! some concetps are wrong


class TestB(unittest.TestCase):
    # mock Base.__init__ which should not?!
    # even it can be called? what is the name it should be?
    # hold for now as I do not see any real usage of it
    #

    @mock.patch("pytests.lib.derived.Derived.__init__")
    def test_calls_init_routine_of_base(self, mock_init):
        derived.Derived(1)
        self.assertTrue(mock_init.called)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestB)
    unittest.TextTestRunner(verbosity=2).run(suite)
