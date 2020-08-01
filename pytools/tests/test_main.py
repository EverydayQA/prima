from myutils.main import Main


def internal_side_effect(num):
    return num - num


def new_func(cls, *args, **kwargs):
    return 2


def test_main_mock(mocker):
    """
    mocker.patch.object(Main, 'internal_func')
    Main().test_func()
    assert Main.internal_func.assert_called_with(20)

    mocker = <pytest_mock.MockFixture object at 0x7f19400cd910>

    def test_main_mock(mocker):
        mocker.patch.object(Main, 'internal_func')
        Main().test_func()
    >       assert Main.internal_func.assert_called_with(20)
    E       AssertionError: assert None
    E        +  where None = <bound method MagicMock.wrap_assert_called_with of <MagicMock name='internal_func' id='139746425495056'>>(20)
    E        +    where <bound method MagicMock.wrap_assert_called_with of <MagicMock name='internal_func' id='139746425495056'>> = <MagicMock name='internal_func' id='139746425495056'>.assert_called_with
    E        +      where <MagicMock name='internal_func' id='139746425495056'> = Main.internal_func

    tests/test_main.py:11: AssertionError
    """
    pass


def test_main_mock2(mocker):
    mocked_internal = mocker.patch.object(Main, 'internal_func')
    # mocked_internal.side_effect = internal_side_effect
    mocked_internal.return_value = -10

    ma = Main()
    val = ma.test_func()

    assert val == 30
    mocked_internal.assert_called
    ma.internal_func.assert_called_with(20)
    mocked_internal.assert_called_with(20)
