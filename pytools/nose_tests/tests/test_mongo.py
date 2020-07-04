import unittest
import mock


class Mongo(object):

    def __init__(self, *args, **kwargs):
        # doing nothing for demo
        pass

    def get_collection(self, input1):
        # return fixed list for demo
        return [1, 3, 5]

    def from_report(self, input_a, input_b):
        collection_a = self.get_collection(input_a)
        collection_b = self.get_collection(input_b)
        return collection_a + collection_b


class TestMongo(unittest.TestCase):

    def setUp(self):
        self.expected = [2, 4, 6, 2, 4, 6]
        self.mock_value = [2, 4, 6]

    def tearDown(self):
        pass

    @mock.patch("nose_tests.tests.test_mongo.Mongo.get_collection")
    def test_using_mock_patch(self, mock_get_collection):
        """
        the patch is in the format of file_name.class_name.method_name
        If the class being patched is the in same file, without quote?!
        patch.object with a class name without quote, a simple patch will always require quote
        """
        mock_get_collection.return_value = self.mock_value
        mongo = Mongo()
        mongo.get_collection = mock_get_collection
        result = mongo.from_report('any', 'where')
        self.assertEquals(result, self.expected)

    # mock.MagicMock
    def test_mongo_get_collection_using_magicMock(self):
        mock_mongo = mock.MagicMock(name='get_collection')
        mock_mongo.get_collection.return_value = self.mock_value
        mongo = Mongo()
        mongo.get_collection = mock_mongo.get_collection
        result = mongo.from_report('any', 'where')
        self.assertEquals(result, self.expected)

    # mock.Mock
    def test_mongo_get_collection_using_Mock(self):
        mock_mongo = mock.Mock(name='get_collection')
        mock_mongo.get_collection.return_value = self.mock_value
        mongo = Mongo()
        mongo.get_collection = mock_mongo.get_collection
        result = mongo.from_report('any', 'where')
        self.assertEquals(result, self.expected)
