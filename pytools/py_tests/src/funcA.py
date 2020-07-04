from utils import helper


def f():
    try:
        helper()
    except Exception:
        raise Exception('error: fail to call helper')
