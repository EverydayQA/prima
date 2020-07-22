import collections
import copy


class NestedDict(object):
    """
    set/update -- assume it is a single key per depth/level
    """

    def update(self, dnew={}, dold={}):
        """
        recursive
        this func has some flaws by design
        dold in parameers will be updated?!
        use copy if do not want this to be changed
        """
        if not dnew:
            return dold

        if not isinstance(dnew, dict):
            print('dnew is {}'.format(dnew))
            raise Exception('update nested not dict')

        # first level keys
        for key in dnew.keys():
            # updated dkey should automatically change d
            v = dold.get(key, None)
            vnest = dnew.get(key, None)
            if not isinstance(v, dict):
                # value or not being set in original d
                # set value to be value of dnew(or dnew_sub)
                # the original v is replaced
                dold[key] = vnest
                return dold

            if not isinstance(vnest, dict):
                # replace existing dict with a value, loosing information
                dold[key] = vnest
                return dold

            vkey = self.update(dnew=vnest, dold=v)
            # replace the original value(v) with vkey
            dold[key] = vkey
        return dold

    def update2(self, dnew={}, dold={}):
        """
        recursive
        assume dnew is complicated with multiple keys at the same depth
        dold in the parameter will be updated, expected or side effect?
        """
        if not dnew:
            return dold
        if not isinstance(dnew, dict):
            return dold

        for key, value in dnew.iteritems():
            if isinstance(value, collections.Mapping) and value:
                vinput = dold.get(key)
                dold[key] = self.update2(dold=vinput, dnew=value)
            else:
                dold[key] = value
        return dold

    def get(self, keys=[], dold={}):
        """
        """
        if not dold:
            return None
        if not isinstance(dold, dict):
            return None

        value = dold
        for key in keys:
            value = value.get(key)
            if not value:
                # print('key {} value {} is None'.format(key, value))
                return value
            if not isinstance(value, dict):
                # print('key {} value {} is not dict type'.format(key, value))
                return value
        return value

    def set(self, value=None, keys=[], dold={}):
        """
        refactor -- for keys len from 1 to len(keys)
        if the value is a dict, it will replaced the previous one if exists
        """
        if not keys:
            return dold

        if not dold:
            # create a new one if empty
            dold = self.create(value=value, keys=keys)
            return dold

        if not isinstance(dold, dict):
            raise Exception('dold is expected to be dict')

        # keys looped already
        items = []
        # keys has not been used yet
        others = copy.deepcopy(keys)
        for key in keys:
            items.append(key)
            vkey = self.get(keys=items, dold=dold)

            if not vkey or not isinstance(vkey, dict):
                # set value
                # the value has to be set in the depth of the key
                dnew = self.create(keys=others, value=value)
                print('key {} empty vin others {}, value {} dnew {}'.format(key, others, value, dnew))

                if len(items) > 1:
                    print(items[0:-1])
                    vkey_prev = self.get(keys=items[0:-1], dold=dold)
                    if isinstance(vkey_prev, dict):
                        vmerge = self.merge_shallow(dnew=dnew, dold=vkey_prev)
                        dold[items[-1]] = vmerge
                        return dold
                    else:
                        dold[items[-1]] = dnew
                        return dold
                else:
                    return dnew
                # this is odd, there is overlapping of key and others[0]
                dold[key] = dnew.get(key)
            others.pop(0)

        return dold

    def create(self, keys=[], value=None):
        """
        create a nested dict with single entry on each depth
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

    def merge_shallow(self, dnew={}, dold={}):
        """
        this will be replaced by {**d, **d2} in python3.8
        """
        # first loop -- update dold if key in dnew
        for key in dold.keys():
            vnew = dnew.get(key)
            if key in dnew:
                dold[key] = vnew

        # second loop -- update dold if key not in dold
        # add if missing
        for key, value in dnew.iteritems():
            if key not in dold:
                dold[key] = value
        return dold
