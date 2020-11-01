import sys
import os
from logg import other_logger


def main():
    """
    tranverse
    normalize path first
    normalize_files then
    """
    from args.normalize_name import ArgNormalizeName
    ren = ArgNormalizeName()
    args = ren.parse_args(sys.argv[1:])
    # this is very import to debugging-level for the whole session in every modules
    other_logger.OtherLogger.setenv_console(level=args.logging_level)
    name = os.path.basename(sys.argv[0])
    other_logger.OtherLogger.setenv_file(level=args.logging_level, name=name)

    logger = other_logger.OtherLogger.logger()
    from logg.logging_config import LoggingConfig
    conf = LoggingConfig()

    logger.critical(args)
    d = conf.get_envconfig()
    logger.critical(d)
    logger.critical(logger.getEffectiveLevel())

    from rename.cli_normalize_name import CliNormalizeName
    cli = CliNormalizeName(**vars(args))
    cli.rename()


if __name__ == '__main__':
    main()
