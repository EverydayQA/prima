import StringIO
import unittest
from mock import patch
import mock


class ReadWrite(object):

    def __init__(self, *args, **kwargs):
        self._file_to_read = kwargs.get('file_to_read', None)
        self._file_to_write = kwargs.get('file_to_write', None)

    @property
    def file_to_read(self):
        return self._file_to_read

    @property
    def file_to_write(self):
        return self._file_to_write


    def output(self):
        output = StringIO.StringIO()
        output.write('line1')
        contents = output.getvalue()
        output.close()
        return contents
    def input_str(self, input_str):
        ipo = StringIO.StringIO(input_str)
        print str(ipo)
        print type(ipo)
        line = ipo.read()
        return line

class TestReadWrite(unittest.TestCase):
    @patch("StringIO.StringIO")
    def test_1(self, MockStringIO):
        MockStringIO().read.return_value = 'mock line1'
        rw = ReadWrite()
        self.assertEquals(rw.input_str('anything'), 'stg')
    
    @patch("StringIO.StringIO", spec=StringIO.StringIO)
    def test_2(self, MockStringIO):
        MockStringIO.assert_called_once() 

    def test_3(self):
        mk = mock.Mock(spec='StringIO.StringIO')
        sio = StringIO.StringIO()
        sio.read()
        mk.read = sio.read()
        mk.read.return_value = 'mock_read'
        mk.assert_called_once()

def main():
    ws = ReadWrite()
    contents = ws.output()
    print contents

    line = ws.input_str('read me')
    print line
if __name__ == '__main__':
    main()

