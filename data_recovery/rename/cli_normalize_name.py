import os
import argparse
from logg import other_logger
# module could have its own level
# use env level, default behavior, no need to provide any parameters
logger = other_logger.OtherLogger.logger()


class CliNormalizeName(object):

    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        self.ns = argparse.Namespace(**self.kwargs)
        logger.warn('CliNormalizeName')

    def d_walk(self, rootdir):
        df = {}
        for path, subdirs, files in os.walk(rootdir):
            if files:
                df[path] = list(set(files))
                continue
            if subdirs:
                df[path] = subdirs
                continue
            df[path] = {}
        return df

    def rename(self):
        path = self.ns.path
        logger.info(path)
        logger.critical(path)
        d = self.d_walk(path)
        from rename.normalize_name import NormalizeName
        norm = NormalizeName()
        for path_tmp in d.keys():
            logger.debug(path_tmp)
            if not os.path.isdir(path_tmp):
                continue
            newpath = norm.normalize_path(path_tmp)
            if path_tmp == newpath:
                logger.debug('no change between {} and {}'.format(path_tmp, newpath))
                pass
            else:
                logger.info('change from {} to {}'.format(path_tmp, newpath))
