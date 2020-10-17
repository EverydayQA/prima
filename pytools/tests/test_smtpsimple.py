import unittest


class TestSMTP(unittest.TestCase):

    # @pytest.fixture
    def smtp_connection(self):
        import smtplib
        return smtplib.SMTP("smtp.gmail.com", 587, timeout=5)

    def test_ehlo(self):
        """
        do not know how to use fixture
        """
        response, msg = self.smtp_connection().ehlo()
        self.assertEqual(response, 250)
