
import mock, unittest
import base
class TestB(unittest.TestCase):
    @mock.patch("Base.__init__")
    def test_calls_init_routine_of_base(mock_super_init):
        base.Derived(1)
        assert (mock_super_init.called)



if __name__ == '__main__':
    unittest.main()
