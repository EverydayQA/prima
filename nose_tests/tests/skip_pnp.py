import unittest
import mock
from python3_unittests.lib.pnp import ssdpClass


class TestPnp(unittest.TestCase):

    def test_msearch(self):
        patcher = mock.patch('python3_unittests.lib.pnp.socket')
        mock_socket = patcher.start()
        mock_s = mock_socket.socket = mock.Mock()
        mock_s.settimeout = mock.Mock()
        mock_s.sendto = mock.Mock()
        mock_s.timepoint = mock.Mock()
        # instantiate our service and set it up
        mock_s.recvfrom.return_value = [bytes(b'data\r\n'), '192.168.10.200']
        oSsdp = ssdpClass()
        oSsdp.msearch()
        patcher.stop()

    def test_msearch2(self):
        patcher = mock.patch('python3_unittests.lib.pnp.socket')
        mock_socket = patcher.start()

        mock_socket.socket = mock.Mock()
        mock_socket.settimeout = mock.Mock()
        mock_socket.sendto = mock.Mock()
        mock_socket.timepoint = mock.Mock()
        # instantiate our service and set it up
        mock_socket.recvfrom = mock.Mock()
        mock_socket.recvfrom.return_value = [bytes(b'data\r\n'), '192.168.10.200']
        oSsdp = ssdpClass()
        oSsdp.msearch()
        patcher.stop()
