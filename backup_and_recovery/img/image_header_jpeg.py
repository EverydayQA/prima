from PIL import Image
from PIL.ExifTags import TAGS
from pprint import pprint
import subprocess


class ImageHeaderJpeg(object):
    """
    The initial purpose is to reader jpegs after data recovery after lvreduce(extend)
    group by date, device etc
    get header info from a jpeg file
    """

    def hdr_from_file(self, afile):
        cmds = ['file', afile]
        out = subprocess.check_output(cmds)
        out = out.decode("utf-8")
        pprint(out)
        print(afile)
        out = out.upper()

        if '2017' in out:
            print('found {}'.format(afile))
        if 'iPhone'.upper() in out:
            print('found {}'.format(afile))

    def header_from_exif(self, img):
        ret = {}
        i = Image.open(img)
        info = i._getexif()
        if not info:
            return {}
        for tag, value in info.items():
            decoded = TAGS.get(tag, tag)
            if tag in self.skip_fields():
                continue
            ret[decoded] = value
        return ret

    def skip_fields(self):
        return ('JPEGThumbnail', 'TIFFThumbnail', 'Filename', 'EXIF Make Note', 'MakerNote')

    def header3(self, img):
        import exifread
        # Open image file for reading (binary mode)
        f = open(img, 'rb')

        # Return Exif tags
        tags = exifread.process_file(f)
        for tag in tags.keys():
            if tag in self.skip_fields():
                continue
            print("Key: {}, value {}".format(tag, tags[tag]))
        return tags

    def headers(self, img):
        d = self.header_from_exif(img)
        pprint(d)
        print(img)
        print('\n** header')
        self.header3(img)


def main():
    img = None
    if not img:
        return
    jpg = ImageHeaderJpeg()
    jpg.headers()


if __name__ == '__main__':
    main()
