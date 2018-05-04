from pprint import pprint

session = {}


def set_session(sess):
    session = sess
    pprint(session)


def purge_first_name():
    session.pop('first_name', None)
