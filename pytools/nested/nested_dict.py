# from termcolor import cprint


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
        vnow = self.get(*keys, **d)
        if vnow == value:
            return d

        if len(keys) == 1:
            # shallow
            d[keys[0]] = value
            return d
        dprev = self.get(*keys[0:-1], **d)
        # replace with lastkey
        dprev[keys[-1]] = value
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

    def merge_shallow(self, dnew, **d):
        for key in dnew.keys():
            v = d.get(key, None)
            vnew = dnew.get(key, None)
            if v == vnew:
                # no change
                continue
            d[key] = vnew
        return d

    def deepset_keys(self, **d):
        """
        single key at each level
        """
        if len(d.keys()) > 1:
            return []
        keys = []
        for key in d.keys():
            v = d.get(key, None)
            # keep lastkey that is not uniq
            keys.append(key)
            if isinstance(v, dict):
                if v.keys() > 1:
                    return keys
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

        deepkeys = self.deepset_keys(**dnew)
        if not deepkeys:
            return self.merge_shallow(dnew, **d)

        vdeep = self.get(*deepkeys, **d)
        vdeep_new = self.get(*deepkeys, **dnew)

        if isinstance(vdeep_new, dict) and isinstance(vdeep, dict):
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
