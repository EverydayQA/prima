#!/usr/bin/env python3
"""Discover UPnP devices"""
import socket


class ssdpClass():
    """Handle Simple Service Discovery Protocol"""

    msg = \
        'M-SEARCH * HTTP/1.1\r\n' \
        'HOST:239.255.255.250:1900\r\n' \
        'ST:upnp:rootdevice\r\n' \
        'MX:2\r\n' \
        'MAN:"ssdp:discover"\r\n' \
        '\r\n'

    def msearch(self):
        """Search for UPnP devices on the local network"""

        # Set up UDP socket with timeout and send a M-SEARCH structure
        # to the upnp multicast address and port
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        s.settimeout(2)
        s.sendto(self.msg.encode(), ('239.255.255.250', 1900))

        # print received data within the timeout
        try:
            while True:
                data, addr = s.recvfrom(65507)
                print(addr)
                print(data.decode())
        except socket.timeout:
            pass
