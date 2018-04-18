import mock
from pytests.lib.app import App
from pytests.lib.app import Base
import unittest


class TestApp(unittest.TestCase):

    def test_mock_instance_attr(self):
        """
        not working
        """
        base = Base()
        app = App()
        base = mock.MagicMock(ccls_attr='mocked_cls_attr')
        self.assertEqual(base.ccls_attr, 'mocked_cls_attr')
        self.assertEqual(app.bbase.ccls_attr, 'mocked_cls_attr')

    def test_mock_cls_attr(self):
        """
        """
        with mock.patch.object(Base, 'ccls_attr') as mock_cls_attr:
            mock_cls_attr.__get__ = mock.Mock(return_value='mocked_cls_attr')
            self.assertEqual(Base.ccls_attr, 'mocked_cls_attr')
            base = Base()
            self.assertEqual(base.ccls_attr, 'mocked_cls_attr')
            app = App()
            self.assertEqual(app.bbase.ccls_attr, 'mocked_cls_attr')

    def test_cls_property(self):
        with mock.patch.object(Base, 'ccls_property') as mock_cls_property:
            mock_cls_property.__get__ = mock.Mock(return_value='mocked_cls_property')
            base = Base()
            self.assertEqual(base.ccls_property, 'mocked_cls_property')

    def test_cls_property_with_propery_mock(self):
        """
        test_cls_property with mock.PropertyMock
        these will not work
        patch.object('pytests.lib.app.Base')
        patch('pytests.lib.app.Base')
        """
        prop_mock = mock.PropertyMock()
        with mock.patch.object(Base, 'ccls_property', prop_mock):
            prop_mock.return_value = 'mocked_cls_property'
            base = Base()
            self.assertEqual(base.ccls_property, 'mocked_cls_property')
            app = App()
            self.assertEqual(app.bbase.ccls_property, 'mocked_cls_property')
