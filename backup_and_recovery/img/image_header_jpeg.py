import os
import sys
from datetime import datetime
from PIL import Image
from PIL.ExifTags import TAGS
from pprint import pprint


class FileDatetime(object):

    def create_time(self, file):
        """
        datetime obj?
        """
        created = os.path.getctime(file)
        return datetime.fromtimestamp(created)
        # return os.stat(file).st_ctime
        # return os.stat(file)[-1]

    def modified_time(self, file):
        modified = os.path.getmtime(file)
        return datetime.fromtimestamp(modified)
        # return os.stat(file)[-2]
        # return os.stat(file).st_mtime

    def date_string_ctime_file(self, file):
        dt = self.create_time(file)
        return self.date_string(dt)

    def date_string(self, dt):
        return dt.strftime("%Y-%m-%d")


class ConstExifJpeg(object):
    """
    'Orientation': 1,
    'ResolutionUnit': 2,
    'SceneCaptureType': 0,
    'SceneType': b'\x01',
    'SensingMethod': 2,
    'ShutterSpeedValue': 7.282087447108603,
    'SubjectLocation': (1757, 993, 1263, 1263),
    'SubsecTimeDigitized': '193',
    'SubsecTimeOriginal': '193',
    'WhiteBalance': 0,
    'XResolution': 72.0,
    'YCbCrPositioning': 1,
    'YResolution': 72.0}
    # skip
    JPEG_THUMBNAIL = 'JPEGThumbnail'
    TIFF_THUMBNAMIL = 'TIFFThumbnail'
    EXIF_MAKE_NOTE = 'EXIF Make Note'
    MAKE_NOTE = 'MakerNote'
    # 'ApertureValue': 2.2750071245369052,
    # 'BrightnessValue': 6.899193548387097,
    # 'ColorSpace': 1,
    # 'ComponentsConfiguration': b'\x01\x02\x03\x00',
    # 'DateTimeDigitized': '2016:07:28 16:13:57',
    # 'ExifImageHeight': 2448,
    # 'ExifImageWidth': 3264,
    # 'ExifOffset': 192,
    # 'ExifVersion': b'0221',
    # 'ExposureBiasValue': 0.0,
    # 'ExposureMode': 0,
    # 'ExposureProgram': 2,
    # 'ExposureTime': 0.00641025641025641,
    # 'FNumber': 2.2,
    # 'Flash': 16,
    # 'FlashPixVersion': b'0100',
    # 'FocalLength': 4.15,
    # 'FocalLengthIn35mmFilm': 29,
    # 'ISOSpeedRatings': 32,
    # 'LensMake': 'Apple',
    # 'LensModel': 'iPhone 6 back camera 4.15mm f/2.2',
    # 'LensSpecification': (4.15, 4.15, 2.2, 2.2),
    # 'MakerNote': 'too long',
    # 'MeteringMode': 5,

    """

    MAKE = 'Make'  # 'Apple',
    MODEL = 'Model'  # 'iPhone 6',
    SOFTWARE = 'Software'  # '9.3.2',
    DATETIIME = 'DateTime'  # '2016:07:28 16:13:57',
    DATETIME_ORIGINAL = 'DateTimeOriginal'  # '2016:07:28 16:13:57',
    FILENAME = 'Filename'

    @property
    def valid_fields(self):
        # return [self.JPEG_THUMBNAIL, self.TIFF_THUMBNAMIL, self.FILENAME, self.EXIF_MAKE_NOTE, self.MAKE_NOTE]
        return [self.MAKE, self.MODEL, self.SOFTWARE, self.DATETIIME, self.DATETIME_ORIGINAL, self.FILENAME]


class ImageHeaderJpeg(ConstExifJpeg, FileDatetime):
    """
    The initial purpose is to reader jpegs after data recovery after lvreduce(extend)
    group by date, device etc
    get header info from a jpeg file
    """

    def header_from_exif(self, img):
        ret = {}
        i = Image.open(img)
        info = i._getexif()
        if not info:
            return {}
        for tag, value in info.items():
            decoded = TAGS.get(tag, tag)
            if decoded not in self.valid_fields:
                continue
            ret[decoded] = value
        return ret

    def header3(self, img):
        import exifread
        # Open image file for reading (binary mode)
        f = open(img, 'rb')

        # Return Exif tags
        tags = exifread.process_file(f)
        for tag in tags.keys():
            if tag not in self.valid_fields:
                continue
            print("Key: <{}>, value <{}>".format(tag, tags[tag]))
        return tags

    def headers(self, img):
        d = self.header_from_exif(img)
        pprint(d)
        print(img)

    def normalize(self, value):
        if not value:
            return value
        value = value.replace(' ', '')
        value = value.replace('/', '-')
        value = value.replace('(', '-')
        value = value.replace(')', '-')
        value = value.replace('\'', '-')
        value = value.replace('\"', '-')
        # null byte
        value = value.replace('\0', '')
        return value

    def str_to_datetime(self, datestr):
        """
        assume this format 2016:07:28 16:13:57
        """
        return datetime.strptime(datestr, '%Y:%m:%d %H:%M:%S')

    def get_datestr(self, d):
        keys = [self.DATETIME_ORIGINAL, self.DATETIIME]
        for key in keys:
            value = d.get(key, None)
            if value:
                return value
        return None

    def datestr_newname(self, afile, d):
        datestr = self.get_datestr(d)
        if not datestr:
            return self.date_string_ctime_file(afile)
        try:
            dt = self.str_to_datetime(datestr)
            return self.date_string(dt)
        except Exception as e:
            print(e)
            return self.date_string_ctime_file(afile)
        return self.date_string_ctime_file(afile)

    def get_newname(self, afile):
        """
        createDate_make_model_software
        make/model/software -- no space, no slash
        """
        try:
            d = self.header_from_exif(afile)
        except Exception as e:
            print(e)
            d = {}
        datestr = self.datestr_newname(afile, d)
        items = [datestr]
        keys = [self.MAKE, self.MODEL, self.SOFTWARE]
        for key in keys:
            value = d.get(key, None)
            if not value:
                continue
            value = self.normalize(value)
            items.append(value)
        return '_'.join(items)


def main():
    """
    No argparse provided
    or create a generic one?
    """
    print(sys.argv)
    if len(sys.argv) < 2:
        raise Exception('usage: python img/image_header_jpeg.py 1.jpg')
    img = sys.argv[1]
    if not img:
        return
    jpg = ImageHeaderJpeg()
    jpg.headers(img)
    newname = jpg.get_newname(img)
    print(newname)


if __name__ == '__main__':
    main()
