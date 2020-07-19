# from termcolor import cprint
import copy


class NestedDict(object):
    """
    Before a nested dict in installed, this will be tested and used
    """

    def set(self, value, *keys, **d):
        """
        assume a simple set value
        set to add or replace value with keys
        # pop() the last item of the list, use your deepGet on it and set the popped off key on the resulting dict
        """
        if not keys:
            return d
        # do not want to change the original d
        dcopy = copy.deepcopy(d)
        vnow = self.get(*keys, **dcopy)
        if vnow == value:
            return dcopy
        dprev = self.get(*keys[0:-1], **dcopy)
        # replace with lastkey
        dprev[keys[-1]] = value
        return dcopy

    def remove(self, *keys, **d):
        """
        not sure if needed
        """
        pass

    def reorder(self):
        # reorder keys
        pass

    def create(self, value, *keys):
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

    def get(self, *keys, **d):
        """
        get the value with keys, default value is None?
        return reduce(lambda d, k: d.get(k) if d else None, keys, sourceDict)
        """
        if not d:
            return None

        value = None
        count = 0
        for key in keys:
            count = count + 1
            if count == 1:
                value = d.get(key, None)
            else:
                value = value.get(key, None)
            # cannot continue
            if not isinstance(value, dict):
                if count == len(keys) - 1:
                    raise Exception('keys is not right')
                return value
        return value

    def update(self, dnew, **d):
        """
        update nested with a nested dict
        assume dnew is a single entry for now, should be compliated
        merge the deepest dict, not replace
        """
        if not dnew:
            return d

        if not isinstance(dnew, dict):
            print('dnew is {}'.format(dnew))
            raise Exception('update nested not dict')
            return d

        # how to tell if 2 dict has the same depth?

        # first level keys
        for key in dnew.keys():
            # updated dkey should automatically change d
            v = d.get(key, None)
            vnest = dnew.get(key, None)
            if not isinstance(v, dict):
                # value or not being set in original d
                # set value to be value of dnew(or dnew_sub)
                # the original v is replaced
                d[key] = vnest
                return d

            if not isinstance(vnest, dict):
                # replace existing dict with a value, loosing information
                d[key] = vnest
                return d

            vkey = self.update(vnest, **v)
            # replace the original value(v) with vkey
            d[key] = vkey
        return d
