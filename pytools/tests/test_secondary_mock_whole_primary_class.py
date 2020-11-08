import mock
import unittest

# this cannot be imported and mock at the same time
# from tests.lib.primary_secondary import Primary
from tests.lib.primary_secondary import Secondary


@mock.patch('tests.lib.primary_secondary.Primary')
class TestSecondaryMockPrimary(unittest.TestCase):

    def test_method_d(self, MockPrimary):
        MockPrimary().process()
        MockPrimary().process.return_value = 1
        oc = Secondary()
        self.assertEqual(oc.method_d(), 1)
        import tests
        self.assertIs(tests.lib.primary_secondary.Primary, MockPrimary)
