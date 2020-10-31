import sys
from logg import console_logging


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
    console_logging.ConsoleLogging().setenv_logging_level_console(args.logging_level)

    logger = console_logging.ConsoleLogging().console_logger(name=None, level=args.logging_level)
    logger.critical(args)
    from rename.cli_normalize_name import CliNormalizeName
    cli = CliNormalizeName(**vars(args))
    cli.rename()


if __name__ == '__main__':
    main()
