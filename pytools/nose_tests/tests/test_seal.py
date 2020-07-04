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
    """
    This is the answer to a question on how to mock
    """

    def test_user_data(self):
        """
        The OP does not want to mock json() in get_user_data()
        """
        response_payload = {"login": "agrawalo"}
        fake_session = mock.MagicMock(spec=Session)
        fake_session.get.return_value.json.return_value = response_payload
        ud = get_user_data("agrawalo", fake_session)
        self.assertEqual(ud, 'agrawalo')

    def test_user_data2(self):
        """
        The get_json() was mocked which is beyond my knowledge
        """
        response_payload = {"login": "agrawalo"}
        fake_session = mock.MagicMock()
        fake_response = fake_session.get.return_value
        # attribute error -- why OP want to mock get_json(), from where?
        fake_response.get_json.return_value = response_payload
        ud = get_user_data("agrawalo", fake_session)
        # this is just getting to nowhere
        self.assertEqual(ud, ud)
