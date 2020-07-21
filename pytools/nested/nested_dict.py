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

        # dnew = self.create(value, *keys)
        # return self.update(dnew, **d)

        if not d:
            return None
        items = copy.deepcopy(list(keys))
        v = None
        keys_past = []
        keys_left = copy.deepcopy(items)
        dprev = None
        for key in items:
            if not keys_past:
                v = d.get(key)
            else:
                v = v.get(key)

            keys_past.append(key)

            keys_left.pop(0)

            # None or empty [] {}
            if not v:
                # final
                if dprev is None:
                    d[key] = self.create(value, *keys_left)
                    return d
                else:
                    dprev[key] = value
                return d

            if not isinstance(v, dict):
                # final
                # replacement?
                dprev[key] = value
                return d

            dprev = v
        return d

    def todo(self):
        """
        remove/reorder/reverse?
        """
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
        items = copy.deepcopy(list(keys))

        if not d:
            return None

        value = None
        keys_past = []
        for key in items:
            if not keys_past:
                value = d.get(key, None)
            else:
                if not isinstance(value, dict):
                    return value
                value = value.get(key, None)

            keys_past.append(key)
            # cannot continue
            if not value:
                return value
        return value

    def merge_shallow(self, dnew, **d):
        for key in d.keys():
            v = d.get(key, None)
            vnew = dnew.get(key, None)
            if key in dnew.keys():
                d[key] = vnew
            else:
                d[key] = v

        for key in dnew.keys():
            v = d.get(key, None)
            vnew = dnew.get(key, None)
            d[key] = vnew

        return d

    def deep_keys(self, keys, **d):
        """
        assume single key at each level
        if multiple keys in a dict, not consider as a key, but a value
        keys to get, will miss one if lastkey is in dict with multiple keys
        set -- dict with multiple keys
        update -- dict with multiple keys
        """
        if not isinstance(d, dict):
            return keys

        if len(d.keys()) > 1:
            return keys

        for key in d.keys():
            v = d.get(key, None)
            # keep lastkey that is not uniq
            keys.append(key)
            if not isinstance(v, dict):
                return keys

            return self.deep_keys(keys, **v)
        return keys

    def shallow_setstar(self, key, value, **d):
        """
        if d is not to be changed outside this func, use this
        """
        d[key] = value
        return d

    def shallow_set(self, key, value, d):
        """
        if d is to be changed outside this func, use this way
        """
        d[key] = value
        return d

    def update2(self, dnew, **d):
        """
        update nested with a nested dict
        assume dnew is a single entry for now, should be complicated
        merge the deepest dict, not to replace
        No need to do deepcopy with **d
        the return d changed, but d is not from the place where d is provided as input
        """
        if not dnew:
            return d

        if not isinstance(dnew, dict):
            print('dnew is {}'.format(dnew))
            raise Exception('update nested not dict')
            return d
        deepkeys = []
        deepkeys = self.deep_keys(deepkeys, **dnew)
        if not deepkeys:
            return self.merge_shallow(dnew, **d)

        vdeep = self.get(*deepkeys, **d)
        vdeep_new = self.get(*deepkeys, **dnew)

        if isinstance(vdeep_new, dict) and isinstance(vdeep, dict):
            pass
            # do not want to merge
            vmerge = self.merge_shallow(vdeep_new, **vdeep)
            return self.set(vmerge, *deepkeys, **d)
        return self.set(vdeep_new, *deepkeys, **d)

    def update(self, dnew, **d):
        """
        update nested with a nested dict
        assume dnew is a single entry for now, should be complicated
        merge the deepest dict, not to replace
        """
        if not dnew:
            return d

        if not isinstance(dnew, dict):
            print('dnew is {}'.format(dnew))
            raise Exception('update nested not dict')
            return d

        # how to tell if 2 dict has the same depth?
        deepkeys = []
        deepkeys = self.deep_keys(deepkeys, **dnew)
        keys = copy.deepcopy(list(deepkeys))
        for key in deepkeys:
            # updated dkey should automatically change d
            v = d.get(key, None)
            vnest = dnew.get(key, None)
            keys.pop(0)

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

            if isinstance(v, dict) and isinstance(vnest, dict):
                if len(keys) == 1:
                    vkey = self.merge_shallow(vnest, **v)
                    d[key] = vkey
                    return d

            vkey = self.update(vnest, **v)
            # replace the original value(v) with vkey
            d[key] = vkey
        return d
