import collections


class NestedDict(object):
    """
    """

    def update(self, dnew={}, dinput={}):
        """
        recursive
        """
        if not dnew:
            return dinput

        if not isinstance(dnew, dict):
            print('dnew is {}'.format(dnew))
            raise Exception('update nested not dict')

        # first level keys
        for key in dnew.keys():
            # updated dkey should automatically change d
            v = dinput.get(key, None)
            vnest = dnew.get(key, None)
            if not isinstance(v, dict):
                # value or not being set in original d
                # set value to be value of dnew(or dnew_sub)
                # the original v is replaced
                dinput[key] = vnest
                return dinput

            if not isinstance(vnest, dict):
                # replace existing dict with a value, loosing information
                dinput[key] = vnest
                return dinput

            vkey = self.update(dnew=vnest, dinput=v)
            # replace the original value(v) with vkey
            dinput[key] = vkey
        return dinput

    def update2(self, dnew={}, dinput={}):
        """
        not recursive
        """
        if not dnew:
            return dinput

        if not isinstance(dnew, dict):
            print('dnew is {}'.format(dnew))
            raise Exception('update nested not dict')

        deepkeys = self.deepset_keys(dnew)
        if not deepkeys:
            return self.merge_shallow(dnew=dnew, dinput=dinput)

        vdeep = self.get(keys=deepkeys, dinput=dinput)
        vdeep_new = self.get(keys=deepkeys, dinput=dnew)

        if isinstance(vdeep_new, dict) and isinstance(vdeep, dict):
            vmerge = self.merge_shallow(dnew=vdeep_new, dinput=vdeep)
            return self.set(value=vmerge, keys=deepkeys, dinput=dinput)
        return self.set(value=vdeep_new, keys=deepkeys, dinput=dinput)

    def update4(self, dinput={}, dnew={}):
        """
        recursive
        """
        for key, value in dnew.iteritems():
            if isinstance(value, collections.Mapping) and value:
                returned = self.update4(dinput.get(key, {}), value)
                dinput[key] = returned
            else:
                dinput[key] = dnew[key]
        return dinput

    def get(self, keys=[], dinput={}):
        """
        """
        if not dinput:
            return None

        value = dinput
        for key in keys:
            value = value.get(key, None)
            if not value:
                return value
            if not isinstance(value, dict):
                return value
        return value

    def set(self, value=None, keys=[], dinput={}):
        """
        refactor -- for keys len from 1 to len(keys)
        found -- keep going
        not -- dnew  keys_left with values, d[the_key] = dnew
        test and find the key to be used
        test keys_left
        test dnew
        thekey point: keys.pop(0) or just pop()?
        """
        if not keys:
            return dinput

        vnow = self.get(keys=keys, dinput=dinput)
        if vnow == value:
            return dinput

        if len(keys) == 1:
            # shallow
            dinput[keys[0]] = value
            return dinput
        dprev = self.get(keys=keys[0:-1], dinput=dinput)
        # replace with lastkey
        dprev[keys[-1]] = value
        return dinput

    def create(self, keys=[], value=None):
        """
        None recursive creation of nested dict
        """
        if not keys:
            return {}

        d = None
        for key in reversed(keys):
            if d is None:
                d = {key: value}
                continue
            d = {key: d}
        return d

    def merge_shallow(self, dnew={}, dinput={}):
        """
        this will be replaced by {**d, **d2} in python3.8
        """
        for key in dnew.keys():
            v = dinput.get(key, None)
            vnew = dnew.get(key, None)
            if v == vnew:
                # no change
                continue
            dinput[key] = vnew
        return dinput

    def deepset_keys(self, d):
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
