#!/usr/bin/python
import mock, unittest
import sys
import os
pwd = os.path.dirname(os.path.realpath(__file__))
basedir = os.path.join(pwd,'..')
sys.path.append(basedir)
from lib import Derived

# this example has not been sorted out yet
# do not use it !!! some concetps are wrong
# 
class TestB(unittest.TestCase):
    # mock Base.__init__ which should not?!
    @mock.patch("Base.__init__")
    def test_calls_init_routine_of_base(mock_super_init):
        Derived.Derived(1)
        assert (mock_super_init.called)



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestB)
    unittest.TextTestRunner(verbosity=2).run(suite)

