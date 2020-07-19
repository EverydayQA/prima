from tests import test_hello


def bonjour(name):
    return 'bonjour {}'.format(name)


def hello(name):
    return 'Hello {}'.format('Sam')


def my_function():
    return hello('Sam')


def test_hellow(mocker):
    mocked_hello = mocker.patch('tests.test_hello.hello')
    mocked_hello.side_effect = test_hello.bonjour
    assert mocked_hello('Sam') == 'bonjour Sam'
    mocked_hello.assert_called_with('Sam')


def test_my_function(mocker):
    with mocker.patch('tests.test_hello.hello', side_effect=test_hello.bonjour) as mocked_hello:
        mocked_hello.side_effect = test_hello.bonjour
        assert mocked_hello('Sam') == 'bonjour Sam'
        assert test_hello.hello('Sam') == 'bonjour Sam'
        mf = test_hello.my_function()
        assert mf == 'bonjour Sam'


def test_my_function2(mocker):
    mocked_hello = mocker.patch('tests.test_hello.hello', side_effect=test_hello.bonjour)
    assert mocked_hello('Sam') == 'bonjour Sam'
    assert test_hello.hello('Sam') == 'bonjour Sam'
    mf = test_hello.my_function()
    assert mf == 'bonjour Sam'


def test_my_function3(mocker):
    mocker.patch('tests.test_using_mocker.hello', side_effect=bonjour)
    mf = my_function()
    hello.assert_called_with('Sam')
    assert mf == 'bonjour Sam'


def test_e():
    import pytest
    with pytest.raises(Exception):
        raise Exception


def test_os_path_isfile():
    import mock
    import pytest
    from os import path
    with mock.patch('os.path.isfile', side_effect=Exception('boo')):
        with pytest.raises(Exception):
            path.isfile('/tmp')


def test_f():
    import mock
    import pytest
    with mock.patch('utils.utils.helper', side_effect=Exception('fail to call helper')):
        from utils import funcA
        with pytest.raises(Exception):
            funcA.f()


def test_f2():
    import mock
    import pytest
    from src import funcA
    with mock.patch('utils.funcA.helper', side_effect=Exception('fail to call helper')):
        with pytest.raises(Exception):
            funcA.f()
