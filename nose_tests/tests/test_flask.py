from flask import Flask
from ..fsample import flask_session
import unittest


class SessionTests(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.app.config['SECRET_KEY'] = 'testsecret'

    def test_purge_first_name_from_session(self):
        with self.app.test_client() as c:
                with c.session_transaction() as sess:
                    sess['first_name'] = 'Test'

                    with self.app.test_request_context():

                        self.assertEqual(sess['first_name'], 'Test')
                        flask_session.set_session(sess)
                        flask_session.purge_first_name()

                        self.assertIsNone(flask_session.session.get('first_name', None))

    def test_purge_first_name(self):
        d = {}
        d['first_name'] = 'Test'
        flask_session.session = d
        self.assertEqual(flask_session.session, d)
        flask_session.purge_first_name()
        self.assertIsNone(flask_session.session.get('first_name', None))
