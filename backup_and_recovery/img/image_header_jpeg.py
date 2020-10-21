import sys
from PIL import Image
from PIL.ExifTags import TAGS
from pprint import pprint
from const.exif_jpeg import ConstExifJpeg
from img.file_datetime import FileDatetime


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

    def normalize(self, name):
        if not name:
            return name
        name = name.replace('(', '')
        name = name.replace(')', '')
        name = name.replace('\'', '')
        name = name.replace('\"', '')
        name = name.replace(' ', '')
        name = name.replace('+', '')
        name = name.replace('[', '')
        name = name.replace(']', '')
        name = name.replace(',', '')
        name = name.replace(';', '')
        name = name.replace(':', '')
        name = name.replace('!', '')
        # null byte
        name = name.replace('\0', '')
        return name

    def get_datestr(self, d):
        keys = [self.DATETIME_ORIGINAL, self.DATETIIME]
        for key in keys:
            value = d.get(key, None)
            if value:
                return value
        return None

    def datetime_str_newname(self, afile, d):
        datestr = self.get_datestr(d)
        if datestr:
            try:
                dt = self.exif_datetime_str_to_datetime(datestr)
                return self.date_string(dt)
            except Exception as e:
                print(e)
                return self.datetime_string_ctime_file(afile)
        return self.datetime_string_ctime_file(afile)

    def datestr_newname(self, afile, d):
        datestr = self.get_datestr(d)
        if datestr:
            try:
                dt = self.exif_datetime_str_to_datetime(datestr)
                return self.date_string(dt)
            except Exception as e:
                print(e)
                return self.date_string_ctime_file(afile)
        return self.date_string_ctime_file(afile)

    def get_newname(self, afile, filename=True):
        """
        createDate(date_only)_make_model_software
        make/model/software -- no space, no slash
        """
        try:
            d = self.header_from_exif(afile)
        except Exception as e:
            print(e)
            d = {}
        if filename is True:
            datestr = self.datetime_str_newname(afile, d)
        else:
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
