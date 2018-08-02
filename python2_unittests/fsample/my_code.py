import remove3
if remove3.DO_IMPORT:
    import app


def my_func():
    print(remove3.DO_IMPORT)
    if remove3.DO_IMPORT:
        print(app.OTHER_VAR)
        return True
    return False
