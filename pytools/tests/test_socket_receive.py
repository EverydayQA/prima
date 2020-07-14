#/usr/bin/env pthon
import unittest
import mock
from mock import MagicMock
import socket

class SocketRecv(object):
    def socket_recv_single_msg(self, port):
        try:
            """ will be mocked away anyway"""
            msg = socket.socket.recv
        except:
            msg =  ['0000000066{key=value', ', key=value}']
        line = '\n\n*** running socket_recv_single_msg {0}\n'.format(msg)
        print line
        return msg


class TestSocketRecv(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        msg =  ['0000000066{key=value', ', key=value}']
        msg_mock =  ['0000000022{key=value', ', key=value}']
        cls.mock_value = msg_mock
        cls.expected = msg_mock

    @mock.patch('socket.socket.recv')
    def test_mocksocket_recv(self, mock_recv):
        mock_recv.return_value = self.mock_value
        sr = SocketRecv()
        result = sr.socket_recv_single_msg('port')
        self.assertEquals(result, self.expected)


    def test_recvsocket_recv_single_msg(self):
        mock_recv = mock.Mock(name='socket_recv_single_msg')
        mock_recv.socket_recv_single_msg.return_value = self.mock_value
        recv = SocketRecv()
        recv.socket_recv_single_msg = mock_recv.socket_recv_single_msg
        result = recv.socket_recv_single_msg()
        self.assertEquals(result, self.expected)

    def test_recvsocket_recv_single_msg3(self):
        recv_obj = SocketRecv()
        mockRecv = mock.Mock(spec = SocketRecv)
        mock_obj = mockRecv()
        mock_obj.socket_recv_single_msg.return_value = self.mock_value
        result = mock_obj.socket_recv_single_msg()
        self.assertEquals(result, self.expected)

    def test_recvsocket_recv_single_msg2(self):
        recv_obj = SocketRecv()
        mockRecv = mock.Mock(return_value = recv_obj, side_effect = self.mock_value)
        result = mockRecv()
        self.assertEquals(result, self.expected[0])
        result = mockRecv()
        self.assertEquals(result, self.expected[1])

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSocketRecv)
    unittest.TextTestRunner(verbosity=2).run(suite)
