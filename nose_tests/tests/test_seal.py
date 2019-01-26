import unittest
import mock
from requests import Session


def get_user_data(user, session):
    '''Given a github user, gets it data'''
    url = 'https://api.github.com/users/{user}'
    response = session.get(url)
    json_response = response.json()
    return json_response["login"]


class TestUserData(unittest.TestCase):

    def test_user_data(self):
        response_payload = {"login": "agrawalo"}
        fake_session = mock.MagicMock(spec=Session)
        fake_session.get.return_value.json.return_value = response_payload
        ud = get_user_data("agrawalo", fake_session)
        self.assertEqual(ud, '')

    def test_user_data2(self):
        response_payload = {"login": "agrawalo"}
        fake_session = mock.MagicMock()
        fake_response = fake_session.get.return_value
        # attribute error on json`:
        fake_response.get_json.return_value = response_payload
        ud = get_user_data("agrawalo", fake_session)
        self.assertEqual(ud, '')
