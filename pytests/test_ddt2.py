import ddt
from ddt import file_data
import unittest


def test_load_yaml_without_yaml_support():
    """
    Test that YAML files are not loaded if YAML is not installed.
    """

    @ddt
    class NoYAMLInstalledTest(object):

        @file_data('test_data_dict.yaml')
        def test_file_data_yaml_dict(self, value):
            assert_true(has_three_elements(value))

    tests = filter(_is_test, NoYAMLInstalledTest.__dict__)

    obj = NoYAMLInstalledTest()
    for test in tests:
        method = getattr(obj, test)
        assert_raises(ValueError, method)
