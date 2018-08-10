import mock
from python2_unittests.fsample.app import App
from python2_unittests.fsample.app import Base
import unittest
from StringIO import StringIO


class TestApp(unittest.TestCase):
    """
    Probably the best way of solving the problem is to add class attributes as default values for instance members initialised in __init__().
    Note that if you are only setting default attributes in __init__() then providing them via class attributes (shared between instances of course) is faster too. e.g.
    """
    @mock.patch('sys.stdout', new_callable=StringIO)
    def test_mock_instance_var(self, mocked_stdout):
        """
        test_mock_instance_var
        patch of sys.stdout is only for testing Base,show()
        cls_property is not changed, only instance_var is mocked
        """
        base = Base()
        app = App()

        mock_base = mock.MagicMock(name='Base', spec=Base)
        instance = mock_base.return_value
        instance.instance_var.return_value = 'mmm'
        base.instance_var = instance.instance_var.return_value
        self.assertEqual(base.instance_var, 'mmm')
        self.assertEqual(base.cls_property, 'cls_property')
        # Base class is mocked with instance_var changed only, others did not change
        app.ibase = base
        self.assertEqual(app.ibase.cls_attr, 'cls_attr')
        self.assertEqual(app.ibase.instance_var, 'mmm')
        app.ibase.show()
        self.assertEqual(mocked_stdout.getvalue(), 'mmm\n')

    @mock.patch('sys.stdout', new_callable=StringIO)
    def test_mock_instance_variable(self, mocked_stdout):
        """
        test_mock_instance_var
        patch of sys.stdout is only for testing Base,show()
        """
        mock_base = mock.MagicMock(name='Base', instance_var='mocked_iv', spec=Base)
        base = Base()
        app = App()

        self.assertEqual(base.instance_var, 'instance_var')
        self.assertEqual(base.cls_property, 'cls_property')
        # Base class is mocked with instance_var changed only, others did not change
        base.instance_var = mock_base.instance_var
        app.ibase = base
        self.assertEqual(app.ibase.cls_attr, 'cls_attr')
        self.assertEqual(app.ibase.instance_var, 'mocked_iv')
        app.ibase.show()
        self.assertEqual(mocked_stdout.getvalue(), 'mocked_iv\n')

    def test_mock_instance_var_2(self):
        """
        test_mock_instance_var_2
        The following patch will generator this error
        # AttributeError: <class 'python2_unittests.fsample.app.Base'> does not have the attribute 'instance_var'
        # with mock.patch.object(Base, 'instance_var') as mock_instance_var:
        # with mock.patch('python2_unittests.fsample.app.Base.instance_var') as mock_attr:
        This test will failed, and kept to show the scope is only in Base class, not App unless using self.ibase = base
        """

        patcher = mock.patch('python2_unittests.fsample.app.Base')
        mock_base = patcher.start()
        mock_base.instance_var = 'mmm'
        self.assertEqual(mock_base.instance_var, 'mmm')
        base = Base()
        # this is not mock, but reset the instance_var
        base.instance_var = mock_base.instance_var
        self.assertEqual(base.instance_var, 'mmm')
        app = App()
        app.ibase = base
        # AssertionError: <MagicMock name='Base().instance_var' id='139719873544400'> != 'mocked_instance_var'
        self.assertEqual(app.ibase.instance_var, 'mmm')
        patcher.stop()

    @mock.patch('sys.stdout', new_callable=StringIO)
    def test_instance4(self, mock_stdout):
        """
        """
        with mock.patch('python2_unittests.fsample.app.Base', autospec=True, instance_var='yyy', spec_set=None) as mock_base:
            # Base class not changed
            base = Base()
            self.assertEqual(base.instance_var, 'instance_var')
            # base.instance_var = mock_base.instance_var
            # base.instance_var = 'yyy'
            # but App class completed mocked, not just instance_var, why?
            app = App()
            app.ibase = base
            self.assertEqual(app.ibase.instance_var, 'yyy')
            # func being patched was well
            app.ibase.show()
            self.assertEqual(mock_stdout.getvalue(), 'yyy\n')
            self.assertEqual(app.ibase.cls_property, 'cls_property')
            self.assertEqual(app.ibase.cls_attr, 'cls_attr')

    @mock.patch('sys.stdout', new_callable=StringIO)
    def test_instance3(self, mock_stdout):
        """
        test_instace3
        Base is fully mocked in class App with instance_var mocked, others mocked
        The patch() decorators makes it easy to temporarily replace classes in a particular module with a Mock object. By default patch() will create a MagicMock for you.
        """
        with mock.patch('python2_unittests.fsample.app.Base', autospec=True, spec_set=None) as mock_base:
            # these return value set- not working, reason unknown
            # instance = mock_base.return_value
            # instance.instance_var = 'xxx'
            # mock_base.return_value = 'xxx'
            mock_base.instance_var = 'xxx'
            # Base class not changed
            base = Base()
            self.assertEqual(base.instance_var, 'instance_var')

            # but App class completed mocked, not just instance_var, why?
            app = App()
            app.ibase = base
            # self.assertEqual(app.ibase.instance_var, 'xxx')
            # func being patched was well
            app.ibase.show()
            self.assertEqual(mock_stdout.getvalue(), 'instance_var\n')
            self.assertEqual(app.ibase.cls_property, 'cls_property')
            self.assertEqual(app.ibase.cls_attr, 'cls_attr')

    def test_mock_cls_attr(self):
        """
        """
        with mock.patch.object(Base, 'cls_attr') as mock_cls_attr:
            mock_cls_attr.__get__ = mock.Mock(return_value='mocked_cls_attr')
            self.assertEqual(Base.cls_attr, 'mocked_cls_attr')
            base = Base()
            self.assertEqual(base.cls_attr, 'mocked_cls_attr')
            app = App()
            self.assertEqual(app.ibase.cls_attr, 'mocked_cls_attr')

    def test_cls_property(self):
        with mock.patch.object(Base, 'cls_property') as mock_cls_property:
            mock_cls_property.__get__ = mock.Mock(return_value='mocked_cls_property')
            base = Base()
            self.assertEqual(base.cls_property, 'mocked_cls_property')

    def test_cls_property_with_property_mock(self):
        """
        test_cls_property with mock.PropertyMock
        these will not work
        patch.object('python2_unittests.fsample.app.Base')
        patch('python2_unittests.fsample.app.Base')
        """
        prop_mock = mock.PropertyMock()
        with mock.patch.object(Base, 'cls_property', prop_mock):
            prop_mock.return_value = 'mocked_cls_property'
            base = Base()
            self.assertEqual(base.cls_property, 'mocked_cls_property')
            app = App()
            self.assertEqual(app.ibase.cls_property, 'mocked_cls_property')

    def test_cls_property_with_property_mock2(self):
        """
        """
        with mock.patch('python2_unittests.fsample.app.Base.cls_property', new_callable=mock.PropertyMock) as mock_cls_property:
            mock_cls_property.return_value = 'mocked_cls_property'
            base = Base()
            self.assertEqual(base.cls_property, 'mocked_cls_property')
            app = App()
            self.assertEqual(app.ibase.cls_property, 'mocked_cls_property')
            with self.assertRaises(Exception):
                app.ibase.cls_property()

    @mock.patch('python2_unittests.fsample.app.Base.static_add')
    def test_static_add_1(self, mock_add):
        mock_add.return_value = 23
        num = Base.static_add(12)
        self.assertEqual(num, 23)

    @mock.patch.object(Base, 'static_add')
    def test_static_add_2(self, mock_add):
        mock_add.return_value = 23
        base = Base()
        num = base.static_add(12)
        self.assertEqual(num, 23)


class TestAppPatch(unittest.TestCase):

    @mock.patch.object(Base, 'static_add')
    def test_clsp(self, mock_add):
        mock_add.return_value = 'xxxx'
        base = Base()
        self.assertEqual(base.cls_attr, 'cls_attr')
        self.assertEqual(base.cls_property, 'cls_property')
        self.assertEqual(base.instance_var, 'instance_var')
        num = base.static_add(12)
        self.assertEqual(num, 'xxxx')

    def test_2(self):
        base = Base()
        mock_base = mock.MagicMock(name='Base', instance_var='mocked_iv', spec=Base)
        self.assertEqual(base.cls_attr, 'cls_attr')
        self.assertEqual(base.cls_property, 'cls_property')
        self.assertEqual(mock_base.instance_var, 'mocked_iv')
        self.assertEqual(base.instance_var, 'instance_var')
        base.instance_var = 'mocked_iv'
        app = App()
        app.ibase = base
        self.assertEqual(app.ibase.cls_attr, 'cls_attr')
        self.assertEqual(app.ibase.cls_property, 'cls_property')
        self.assertEqual(app.ibase.instance_var, 'mocked_iv')
