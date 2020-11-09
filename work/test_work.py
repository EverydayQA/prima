import unittest
import mock


class TestWorkMockingModule(unittest.TestCase):

    def workcaller(self):
        # with mock.patch.dict('sys.modules', **{'work.workm': module_mock}):
        # sys.modules['work.workm'] = mock.Mock()
        with mock.patch("workm.unpleasant_side_effect", side_effect=Exception('boo')) as mocked_function:
            # work.workm.unpleasant_side_effect()
            mocked_function.return_value = 3
            from work_caller import WorkCaller
            sut = WorkCaller()
            sut.call_work()


@mock.patch("workm")
class TestWorkMockingModule2(unittest.TestCase):

    def test_workcaller(self, mock_module):
        mock_module.unpleasant_side_effect()
        mock_module.unpleasant_side_effect.return_value = 1

        mock_module.workon()
        mock_module.workon.return_value = 2

        from work_caller import WorkCaller
        sut = WorkCaller()
        sut.call_work()
