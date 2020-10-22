

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
