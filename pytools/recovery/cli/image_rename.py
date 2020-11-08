import sys


def main():
    # args
    from recovery.args.image_rename import ArgImageRename
    ren = ArgImageRename()
    args = ren.parse_args(sys.argv[1:])

    # logger env
    from logg import other_logger
    other_logger.OtherLogger.setenv_console(level=args.logging_level)
    other_logger.OtherLogger.setenv_file(level=args.logging_level, name=sys.argv[0])

    # cli class
    from recovery.img.cli_image_rename import CliImageRename
    cli = CliImageRename(**vars(args))
    cli.rename()


if __name__ == '__main__':
    main()
