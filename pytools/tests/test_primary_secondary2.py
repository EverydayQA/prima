import unittest
import mock


class TestPrimaySeconday(unittest.TestCase):
    """
    This is a mock example
    patch mutiple classes using create_patch
    addCleanup() to replace tearDown()
    https://docs.python.org/3.3/library/unittest.mock-examples.html
    no need for with statement
    """

    def create_patch(self, name):
        patcher = mock.patch(name)
        thing = patcher.start()
        self.addCleanup(patcher.stop)
        return thing

    def test_mutiple_patches(self):
        """
        in case needed to patch multiple classes
        """
        mock_primary = self.create_patch('tests.lib.primary_secondary.Primary')
        mock_secondary = self.create_patch('tests.lib.primary_secondary.Secondary')
        from tests.lib import primary_secondary

        self.assertTrue(primary_secondary.Primary is mock_primary)
        self.assertTrue(primary_secondary.Secondary is mock_secondary)

    def test_mutiple_patches2(self):
        """
        using with statement
        """
        with mock.patch('tests.lib.primary_secondary.Primary') as mock_primary:
            with mock.patch('tests.lib.primary_secondary.Secondary') as mock_secondary:
                from tests.lib import primary_secondary
                self.assertTrue(primary_secondary.Primary is mock_primary)
                self.assertTrue(primary_secondary.Secondary is mock_secondary)
