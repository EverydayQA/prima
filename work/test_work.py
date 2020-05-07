from unittest import TestCase, mock
from pprint import pprint
import sys

class TestWorkMockingModule(TestCase):
    def test_workcaller(self):
        # with mock.patch.dict('sys.modules', **{'work.workm': module_mock}):
        import work
        # sys.modules['work.workm'] = mock.Mock()
        with mock.patch("work.workm.unpleasant_side_effect", side_effect=Exception('boo')) as mocked_function:
            work.workm.unpleasant_side_effect()
            # from work.work_caller import WorkCaller

            # sut = WorkCaller()
            # sut.call_work()


