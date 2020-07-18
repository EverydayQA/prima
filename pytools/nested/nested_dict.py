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
        # do not want to change the original d
        dcopy = copy.deepcopy(d)
        vnow = self.get(dcopy, keys)
        if vnow == value:
            return d
        dprev = self.get(dcopy, keys[0:-1])
        # replace with lastkey
        dprev[keys[-1]] = value
        return dcopy

    def create(self, keys, value):
        """
        create a single entry nested dict
        """
        dtmp = None
        for key in reversed(keys):
            if not dtmp:
                dtmp = {key: value}
                continue
            dtmp = {key: dtmp}
        return dtmp

    def get(self, d, keys):
        """
        get the value with keys, default value is None?
        return reduce(lambda d, k: d.get(k) if d else None, keys, sourceDict)
        """
        value = None
        count = 0
        for key in keys:
            count = count + 1
            if count == 1:
                value = d.get(key, None)
            else:
                value = value.get(key, None)
            if not isinstance(value, dict):
                return value
        return value

    def update2(self, d, dnew):
        """
        reversed keys(how?)
        get old/new, compare, merge/update/replace
        """
        raise Exception('not coded yet')

    def update(self, d, dnest):
        """
        update nested with a nested dict
        assume dnest is a single entry for now, should be compliated
        merge the deepest dict, not replace
        """
        if not dnest:
            return d

        if not isinstance(dnest, dict):
            print('dnest is {}'.format(dnest))
            raise Exception('update nested not dict')
            return d

        # how to tell if 2 dict has the same depth?

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
                d[key] = vnest
                return d

            vkey = self.update(v, vnest)
            # replace the original value(v) with vkey
            d[key] = vkey
        return d
