
import mock, unittest
import inhe;

class TestB(unittest.TestCase):

    @mock.patch("inhe.A.method")
    def test_super_method(self, mock_super):
        B(True).method()
        self.assertTrue(mock_super.called)

    @mock.patch("inhe.A.method")
    def test_super_method(self, mock_super):
        inhe.B(False).method()
        self.assertFalse(mock_super.called)


if __name__ == '__main__':
    unittest.main()
