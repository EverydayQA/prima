import os
import sys
import argparse
from logg import logging_config
logger = logging_config.get_logger(__file__, level=10, logfile=None)


class CliNormalizeName(object):

    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        self.ns = argparse.Namespace(**self.kwargs)

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
            if not os.path.isdir(path_tmp):
                continue
            newpath = norm.normalize_path(path_tmp)
            if path_tmp == newpath:
                # logger.info('no change between {} and {}'.format(path_tmp, newpath))
                pass
            else:
                logger.info('change from {} to {}'.format(path_tmp, newpath))


def main():
    """
    tranverse
    normalize path first
    normalize_files then
    """
    from args.normalize_name import ArgNormalizeName
    ren = ArgNormalizeName()
    args = ren.parse_args(sys.argv[1:])

    logger.info(args)

    cli = CliNormalizeName(**vars(args))
    cli.rename()


if __name__ == '__main__':
    main()
