import sys


def main():
    from quiz.args.quiz import ArgsQuiz
    arg = ArgsQuiz()
    args = arg.parse_args(sys.argv[1:])

    from logg import other_logger
    other_logger.OtherLogger.setenv_console(level=args.logging_level)
    other_logger.OtherLogger.setenv_file(level=args.logging_level, name=sys.argv[0])
    logger = other_logger.logger(__name__)
    logger.debug(__name__)

    from quiz.add.add_wrapper import AddWrapper
    aw = AddWrapper(**vars(args))
    # dispatch handover to AddQuiz?
    aw.dispatch()


if __name__ == '__main__':
    main()
