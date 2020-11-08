import mock
import unittest
from tests.lib import primary_secondary


class TestPrimarySecondary(unittest.TestCase):
    """
    mixed mock on every methods, creating problems
    """

    @mock.patch.object(primary_secondary.Primary, '_do_process')
    @mock.patch.object(primary_secondary.Primary, '_do_intermediate_process')
    def test_process(self, mocked_do_intermediate_process, mocked_do_process):
        instance = primary_secondary.Primary(0)
        instance.process()
        mocked_do_intermediate_process.assert_not_called()
        mocked_do_process.assert_called_once()
        mocked_do_process.assert_has_calls([mocked_do_process])

    def test_mock_whole_class(self):
        """
        not very useful, for the concept
        with mock_crete_autospec, mock object has the properties(methods) of Secondary
        There is no need to make another MockClass
        """
        m = mock.create_autospec(primary_secondary.Secondary)
        m.method_a(1, 2)
        # m.method_a.assert_called_once()
        m.method_a.assert_called_once_with(1, 2)

        m.method_b.return_value = 3
        self.assertEqual(m.method_b(99), 3)

        # no method c
        with self.assertRaises(Exception) as context:
            m.method_c('c')
        self.assertEqual(("Mock object has no attribute 'method_c'",), context.exception.args)

    def test_mock_method_a(self):
        """
        mock method_a of the Secondary, this is more useful in reality
        method_a is mocked and does not matter how many parameters
        """
        patcher = mock.patch.object(primary_secondary.Secondary, "method_a", return_value='aaa')
        patcher.start()
        cls = primary_secondary.Secondary()
        result = cls.method_a(1)
        self.assertEqual(result, 'aaa')

        with self.assertRaises(TypeError):
            cls.method_b()
        patcher.stop()

    @mock.patch('tests.lib.primary_secondary.Primary')
    def test_mock_cls(self, MockClass):
        MockClass().process()
        MockClass().process.return_value = 1
        sc = primary_secondary.Primary('a')
        self.assertEqual(sc.process(), 1)
        self.assertTrue(MockClass.called)
        self.assertIs(primary_secondary.Primary, MockClass)

    def test_method_d(self):
        with mock.patch('tests.lib.primary_secondary.Primary') as MockSome:
            MockSome().process()
            MockSome().process.return_value = 1
            value = primary_secondary.Secondary().method_d()
            self.assertEqual(value, 1)

    def test_method_d2(self):
        patcher = mock.patch('tests.lib.primary_secondary.Primary')
        patcher.start()
        cls = primary_secondary.Secondary()
        result = cls.method_d()
        self.assertEqual(result, 'aaa')
