#!/usr/bin/python
import logging
import sys


class Merge(object):

    def __init__(self, *args, **kwargs):
        self.logger = logging.getLogger(__name__)
        self.logger.info('class init')


def init_logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    return logger


def main():
    logger = init_logger()
    logger.info('step 1: afile2list()')

    logger.info('step 2: merge lists()')

    logger.info('step 3: alist2afile_write()')

    logger.info('step 4: alist2afile_append()')


if __name__ == '__main__':
    main()
