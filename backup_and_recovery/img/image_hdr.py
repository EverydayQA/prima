from PIL import Image
from PIL.ExifTags import TAGS
from pprint import pprint
import subprocess


class ImgJpeg(object):
    """
    get header info from a jpeg file
    date
    device
    user?
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


def main():
    img = None
    if not img:
        return
    jpg = ImgJpeg()
    d = jpg.header_from_exif(img)
    pprint(d)
    print(img)
    print('\n** header')
    jpg.header3(img)


if __name__ == '__main__':
    main()
