import collections
# from termcolor import cprint
import copy


class NestedDict(object):
    """
    Before a nested dict in installed, this will be tested and used
    """

    def set(self, keys, value, **d):
        """
        assume a simple set value
        set to add or replace value with keys
        # pop() the last item of the list, use your deepGet on it and set the popped off key on the resulting dict
        """
        if not keys:
            return d

        # prev = self.get(d, keys)

        dtmp = None
        count = 0
        for key in reversed(keys):
            count = count + 1
            if count == 1:
                dtmp = {key: value}
                continue
            dtmp = {key: dtmp}
        return dtmp

    def deep_get(self, d, keys):
        keysc = copy.deepcopy(keys)
        if not d:
            return d
        if not keysc:
            return None

        if not isinstance(d, dict):
            raise Exception('original d not dict')
            return None

        firstkey = keysc.pop(0)
        dfirst = d.get(firstkey, None)
        if not dfirst:
            return dfirst
        if not isinstance(dfirst, dict):
            return dfirst

        # keys reduced 1 by pop(0)
        # dv reduced by 1 level
        return self.get(dfirst, keysc)

    def get(self, d, keys):
        """
        get the value with keys, default value is None?
        return reduce(lambda d, k: d.get(k) if d else None, keys, sourceDict)
        """
        dtmp = None
        count = 0
        for key in keys:
            count = count + 1
            if count == 1:
                dtmp = d.get(key, {})
            else:
                dtmp = dtmp.get(key, {})
            if not isinstance(dtmp, dict):
                return dtmp

        return dtmp

    def create_nested(self, keys, value):
        """
        create a nested dict
        """
        print('create_nested with keys {} value {}'.format(keys, value))
        if not keys:
            return {}
        # keys reduced by 1
        lastkey = keys.pop()
        # lastkey changed
        dnew = {lastkey: value}
        if not keys:
            return dnew
        return self.create_nested(keys, dnew)

    def deep_update(self, source, overrides):
        """Update a nested dictionary or similar mapping.

        Modify ``source`` in place.
        """
        for key in overrides.keys():
            value = overrides.get(key, None)
            if isinstance(value, collections.abc.Mapping) and value:
                returned = self.deep_update(source.get(key, {}), value)
                source[key] = returned
            else:
                source[key] = overrides[key]
        return source

    def update(self, d, dnest):
        """
        update nested with a nested dict
        assume dnest is a single entry for now, should be compliated
        """
        if not dnest:
            return d

        if not isinstance(dnest, dict):
            print('dnest is {}'.format(dnest))
            raise Exception('update nested not dict')
            return d

        # first level keys
        for key in dnest.keys():
            # updated dkey should automatically change d
            v = d.get(key, None)
            vnest = dnest.get(key, None)
            if not isinstance(v, dict):
                # value or not being set in original d
                # set value to be value of dnest(or dnest_sub)
                # the original v is replaced
                d[key] = vnest
                return d

            if not isinstance(vnest, dict):
                # replace existing dict with a value, loosing information
                # d[key] = vnest
                # return d
                print('key {} v is {}'.format(key, v))
                print(vnest)
                raise Exception('vnest not dict')
                continue

            vkey = self.update(v, vnest)
            # replace the original value(v) with vkey
            d[key] = vkey
        return d
