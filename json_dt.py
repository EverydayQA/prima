# u'datetime.datetime(2020, 5, 28, 13, 58, 0, 547999, tzinfo=psycopg2.tz.FixedOffsetTimezone(offset=-240, name=None))'

import datetime
import json


def default(obj):
    if isinstance(obj, datetime.datetime):
        return {'_isoformat': obj.isoformat()}
    return super().default(obj)


def object_hook(obj):
    _isoformat = obj.get('_isoformat')
    if _isoformat is not None:
        return datetime.fromisoformat(_isoformat)
    return obj


if __name__ == '__main__':
    d = {'now': datetime.datetime(2000, 1, 1)}
    # d = {'now': datetime.datetime(2000, 1, 1, tzinfo=datetime.timezone(datetime.timedelta(hours=-8)))}
    s = json.dumps(d, default=default)
    print(s)
    print(d == json.loads(s, object_hook=object_hook))
