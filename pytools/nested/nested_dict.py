import collections
import copy


class NestedDict(object):
    """
    set/update -- assume it is a single key per depth/level
    """

    def update(self, dnew={}, dinput={}):
        """
        recursive
        this func has some flaws by design
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

    def update2(self, dinput={}, dnew={}):
        """
        recursive
        assume dnew is complicated with multiple keys at the same depth
        """
        raise Exception('has not been tested yet')
        if not dnew:
            return dinput
        if not isinstance(dnew, dict):
            return dinput

        for key, value in dnew.iteritems():
            if isinstance(value, collections.Mapping) and value:
                vinput = dinput.get(key)
                dinput[key] = self.update2(dinput=vinput, dnew=value)
            else:
                dinput[key] = value
        return dinput

    def get(self, keys=[], dinput={}):
        """
        """
        if not dinput:
            return None
        if not isinstance(dinput, dict):
            return None

        value = dinput
        for key in keys:
            value = value.get(key)
            if not value:
                return value
            if not isinstance(value, dict):
                return value
        return value

    def set(self, value=None, keys=[], dinput={}):
        """
        refactor -- for keys len from 1 to len(keys)
        if the value is a dict, it will replaced the previous one if exists
        """
        if not keys:
            return dinput

        if not dinput:
            # create a new one if empty
            dinput = self.create(value=value, keys=keys)
            return dinput

        if not isinstance(dinput, dict):
            raise Exception('dinput is expected to be dict')

        # keys looped already
        items = []
        # keys has not been used yet
        others = copy.deepcopy(keys)
        for key in keys:
            items.append(key)
            others.pop(0)
            vin = self.get(keys=items, dinput=dinput)
            if not vin or not isinstance(vin, dict):
                # set value
                # the value has to be set in the depth of the key
                dnew = self.create(keys=others, value=value)
                dinput[key] = dnew
        return dinput

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

    def merge_shallow(self, dnew={}, dinput={}):
        """
        this will be replaced by {**d, **d2} in python3.8
        """
        # first loop -- update dinput if key in dnew
        for key in dinput.keys():
            vnew = dnew.get(key)
            if key in dnew:
                dinput[key] = vnew

        # second loop -- update dinput if key not in dinput
        # add if missing
        for key, value in dnew.iteritems():
            if key not in dinput:
                dinput[key] = value
        return dinput
