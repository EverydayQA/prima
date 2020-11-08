from ..lib import quiz_email


class MimeSendTest(object):

    def __init__(self):
        pass

    def test_text_str(self):
        ms = quiz_email.MimeSend()
        txt = ms.text_str()
        self.assertEqual(txt, 'are you text_str')
