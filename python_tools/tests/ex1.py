import mock
import unittest
import ex1

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

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestMockReturnValue)
    unittest.TextTestRunner(verbosity=2).run(suite)

