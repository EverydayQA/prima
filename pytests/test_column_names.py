import unittest
from .lib import column_names
from pyspark import SparkContext, SparkConf
from pyspark.sql import HiveContext
conf = SparkConf()
sc = SparkContext(conf=conf)
sqlContext = HiveContext(sc)

cols = ['ID', 'NAME', 'last.name', 'abc test']
val = [(1, 'Sam', 'SMITH', 'eng'), (2, 'RAM', 'Reddy', 'turbine')]
df = sqlContext.createDataFrame(val, cols)


class RenameColumnNames(unittest.TestCase):

    def test_column_names(self):
        df1 = column_names(df)
        result = df1.schema.names
        expected = ['ID', 'NAME', 'last_$name', 'abc_&test']
        self.assertEqual(result, expected)
