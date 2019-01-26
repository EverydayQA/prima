import sqlite3
import unittest


class Database:
    """ it has more methods but I show only the most important """

    def __init__(self, name):
        # let's think the db-file exists with tables
        self.conn = sqlite3.connect(name)
        self.cursor = self.conn.cursor()

    def create_table(self):
        # Create table
        self.cursor.execute('''CREATE TABLE stocks(date text, trans text, symbol text, qty real, price real)''')

    def __del__(self):
        """ Here I close connection if the object was destroyed """
        self.conn.close()

    def insert(self):
        """ The key method where problem is """
        self.cursor.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")
        self.conn.commit()  # here I do commit to apply changes with DB


class DatabaseTestCase(unittest.TestCase):
    """ it has other methods but the problem is here """

    @classmethod
    def setUpClass(cls):
        pass

    def test_db_insert(self):
        db = Database("test1.db")
        # db.create_table()

        # insert with commit (see Database example above)
        db.insert()

        # delete object and close connection
        del db

        # recreate the object to get sure my data was added and
        # the changes were commited
        db = Database("test1.db")

        # I use the way not to use my own methods of Database object
        t = ('RHAT',)
        db.cursor.execute('SELECT * FROM stocks WHERE symbol=?', t)
        result = db.cursor.fetchone()
        self.assertEqual(result, (u'2006-01-05', u'BUY', u'RHAT', 100.0, 35.14))
        # close connection with deleting of the db object
        del db

    def test_db_insert2(self):
        db = Database("test.db")
        # db.create_table()

        # insert with commit (see Database example above)
        db.insert()

        # delete object and close connection
        del db

        # recreate the object to get sure my data was added and
        # the changes were commited
        db = Database("test.db")

        # I use the way not to use my own methods of Database object
        t = ('RHAT',)
        db.cursor.execute('SELECT * FROM stocks WHERE symbol=?', t)
        result = db.cursor.fetchone()
        self.assertEqual(result, (u'2006-01-05', u'BUY', u'RHAT', 100.0, 35.14))
        # close connection with deleting of the db object
        del db

