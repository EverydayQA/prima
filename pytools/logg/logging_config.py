import os


class LoggingConfig(object):

    """
    LOGGING-LEVEL in env for both logfile and console
    each module could has the same logfile and logging-level of their own
    but env logging-level is for every module of the session
    """

    LOGGING_LEVEL_CONSOLE = 'LOGGING_LEVEL_CONSOLE'
    LOGGING_FILE = 'LOGGING_FILE'
    ERROR_LOGGING_FILE = 'ERROR_LOGGING_FILE'
    LOGGING_LEVEL_FILE = 'LOGGING_LEVEL_FILE'

    LOGFORMAT = "  %(log_color)s%(levelname)-8s%(reset)s | %(log_color)s%(message)s%(reset)s"
    # LOGFORMAT = "%(log_color)s - %(asctime)s - %(name)-12s - %(levelname)s - %(message)s",

    # for CONSOLE_LOGGING
    CFORMAT_LONG = "%(log_color)s[%(asctime)s %(levelname)-8s%(module)s]%(reset)s %(white)s%(message)s"

    def keys_envconfig(self):
        return [self.LOGGING_FILE, self.ERROR_LOGGING_FILE, self.LOGGING_LEVEL_CONSOLE, self.LOGGING_LEVEL_FILE]

    def get_envconfig(self):
        d = {}
        for key in self.keys_envconfig():
            d[key] = os.environ.get(key, None)
        return d

    @property
    def format_simple(self):
        # return self.LOGFORMAT
        return '%(module)-12s: %(levelname)-8s %(message)s'

    @property
    def format_verbose(self):
        return '%(asctime)s %(module)-12s %(levelname)-8s %(message)s'
