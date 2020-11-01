import os
from logg import other_logger
# module has its own level
# default logger using env level
logger = other_logger.OtherLogger.logger(name=__name__)


class NormalizeName(object):
    """
    """

    def __init__(self, *args, **kwargs):
        """
        logfile/level to be in kwargs
        """
        self.afile = os.path.basename(__file__)
        # cname = self.__class__.__name__
        # names = [afile, cname]
        # name = '.'.join(names)
        logger.warn('NormalizeName')
        logger.info('NormalizeName')
        logger.debug('NormalizeName')
        logger.critical('NormalizeName')
        logger.info('{}.{}'.format(self.__module__, self.__class__.__name__))

    def normalize_name(self, name):
        original = name
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
        # #
        # ?
        # others?
        if original != name:
            logger.info([original, name])
        return name

    def normalize_path(self, path):
        """
        only basename of the path, not the fullpath
        """
        path = os.path.abspath(path)
        basename = os.path.basename(path)
        new_basename = self.normalize_name(basename)

        dirname = os.path.dirname(path)
        return os.path.join(dirname, new_basename)

    def normalize_file(self, afile):
        """
        only basename of the file
        """
        afile = os.abspath(afile)
        basename = os.path.basename(afile)
        new_basename = self.normalize_name(basename)
        dirname = os.path.dirname(afile)
        return os.path.join(dirname, new_basename)
