import logging
import logging.config
import time


class LoggingConfig(object):

    def format_simple(self):
        return '%(name)-12s: %(levelname)-8s %(message)s'

    def format_verbose(self):
        return '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'

    @classmethod
    def d_config(self, level=logging.DEBUG, logfile=None):
        if not logfile:
            logfile = '/tmp/logfile'

        LOGGING = {
            'version': 1,
            'disable_existing_loggers': False,
            'formatters': {
                'console_format': {
                    'format': '%(name)-12s: %(levelname)-8s %(message)s', },
                'file_format': {
                    'format': '%(asctime)s %(name)-12s %(levelname)-8s %(message)s', }, },
            'handlers': {
                'console': {
                    'class': 'logging.StreamHandler',
                    'level': 'INFO',
                    'formatter': 'console_format', },

                'logfile': {
                    'class': 'logging.FileHandler',
                    'formatter': 'file_format',
                    'filename': logfile,
                    'mode': 'w'}, },
            'root': {
                'level': 'INFO',
                'handlers': ['console', 'logfile'], },
        }
        return LOGGING


def get_logger(name, level=logging.INFO, logfile=None):
    dc = LoggingConfig.d_config(level=logging.INFO, logfile='/tmp/helo')
    logging.config.dictConfig(dc)
    logging.warning('get_logger %s', time.asctime())
    logger = logging.getLogger(name)
    return logger


if __name__ == '__main__':
    dc = LoggingConfig.d_config(level=logging.INFO, logfile='/tmp/helo')
    logging.config.dictConfig(dc)
    logging.warning('The local time is %s', time.asctime())
    logger = logging.getLogger(__name__)
    logger.warning('logger')
    logger.info('info')
    logger = get_logger(__name__, logfile=None)
    logger.critical('get_logger')
