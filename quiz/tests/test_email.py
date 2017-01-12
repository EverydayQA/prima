#!/usr/bin/python
import unittest
from ..quiz import email

class MimeSendTest(object):
    def __init__(self):
        pass
    def test_text_str(self):
        ms = email.MimeSend()
        txt = ms.text_str()
        self.assertEqual(txt, 'are you text_str')

