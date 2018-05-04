from pytests import test_hello


def bonjour(name):
    return 'bonjour {}'.format(name)


def hello(name):
    return 'Hello {}'.format('Sam')


def my_function():
    return hello('Sam')


def test_hellow(mocker):
    mocked_hello = mocker.patch('pytests.test_hello.hello')
    mocked_hello.side_effect = test_hello.bonjour
    assert mocked_hello('Sam') == 'bonjour Sam'
    mocked_hello.assert_called_with('Sam')


def test_my_function(mocker):
    with mocker.patch('pytests.test_hello.hello', side_effect=test_hello.bonjour) as mocked_hello:
        mocked_hello.side_effect = test_hello.bonjour
        assert mocked_hello('Sam') == 'bonjour Sam'
        assert test_hello.hello('Sam') == 'bonjour Sam'
        mf = test_hello.my_function()
        assert mf == 'bonjour Sam'


def test_my_function2(mocker):
    mocked_hello = mocker.patch('pytests.test_hello.hello', side_effect=test_hello.bonjour)
    assert mocked_hello('Sam') == 'bonjour Sam'
    assert test_hello.hello('Sam') == 'bonjour Sam'
    mf = test_hello.my_function()
    assert mf == 'bonjour Sam'


def test_my_function3(mocker):
    mocker.patch('pytests.pyt.hello', side_effect=bonjour)
    mf = my_function()
    hello.assert_called_with('Sam')
    assert mf == 'bonjour Sam'


def test_e():
    import pytest
    with pytest.raises(Exception):
        raise Exception
