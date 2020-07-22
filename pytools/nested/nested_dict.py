import collections
import copy


class NestedDict(object):
    """
    set/update -- assume it is a single key per depth/level
    """

    def update(self, dchg={}, dnow={}):
        """
        recursive
        this func has some flaws by design

        this is the same for set/update/update2/merge_shallow
        dnow in parameters will be updated, this is unavoidable, make a deepcopy before(and outside) this func

        --set has the logic of merging if both were dict with multiple keys?
        the logic might not be reached, need to add tests to verify this

        --update do not have the logic, apply a simple replacement?
        """
        if not dchg:
            return dnow

        if not isinstance(dchg, dict):
            print('dchg is {}'.format(dchg))
            raise Exception('update nested not dict')

        # first level keys
        for key in dchg.keys():
            # updated dkey should automatically change d
            v = dnow.get(key, None)
            vnest = dchg.get(key, None)
            if not isinstance(v, dict):
                # value or not being set in original d
                # set value to be value of dchg(or dchg_sub)
                # the original v is replaced
                dnow[key] = vnest
                return dnow

            if not isinstance(vnest, dict):
                # replace existing dict with a value, loosing information
                dnow[key] = vnest
                return dnow

            vkey = self.update(dchg=vnest, dnow=v)
            # replace the original value(v) with vkey
            dnow[key] = vkey
        return dnow

    def update2(self, dchg={}, dnow={}):
        """
        recursive
        assume dchg is complicated with multiple keys at the same depth
        dnow in the parameter will be updated, expected or side effect?
        """
        if not dchg:
            return dnow
        if not isinstance(dchg, dict):
            return dnow

        for key, value in dchg.iteritems():
            if isinstance(value, collections.Mapping) and value:
                vinput = dnow.get(key)
                dnow[key] = self.update2(dnow=vinput, dchg=value)
            else:
                dnow[key] = value
        return dnow

    def get(self, keys=[], dnow={}):
        """
        """
        if not dnow:
            return None
        if not isinstance(dnow, dict):
            return None

        value = dnow
        for key in keys:
            value = value.get(key)
            if not value:
                # print('key {} value {} is None'.format(key, value))
                return value
            if not isinstance(value, dict):
                # print('key {} value {} is not dict type'.format(key, value))
                return value
        return value

    def set(self, value=None, keys=[], dnow={}):
        """
        replace in general
        if value and the existing one are both dict, merge
        """
        if not keys:
            # not going to return silently
            raise Exception('Keys must not be empty')

        if not dnow:
            # create one with keys and value
            dnow = self.create(value=value, keys=keys)
            return dnow

        if not isinstance(dnow, dict):
            raise Exception('Expecting type dict')

        # keys looped already
        items = []
        # keys has not been used yet
        others = copy.deepcopy(keys)
        for key in keys:

            # make sure items(keys) is not empty
            items.append(key)
            vkey = self.get(keys=items, dnow=dnow)

            if vkey and isinstance(vkey, dict):
                others.pop(0)
                # keep going if type dict
                if items == keys:
                    # last one
                    if isinstance(value, dict):
                        # merge? same as update
                        # vkey changed
                        self.merge_shallow(dchg=value, dnow=vkey)

                        # value fully replacement, no merge
                        # vkey[key] = value
                        return dnow
                continue

            # None/empty list|set|dict/ type not dict/
            # not vkey or not isinstance(vkey, dict):
            # set value(?) with proper keys(?)
            dchg = self.create(keys=others, value=value)
            print('key {} empty vin others {}, value {} dchg {}'.format(key, others, value, dchg))

            if len(items) == 1:
                # first item
                # no need to pop others since return
                return dchg

            print(items[0:-1])
            vkey_prev = self.get(keys=items[0:-1], dnow=dnow)
            if isinstance(vkey_prev, dict):
                # vkey_prev merged and changed
                self.merge_shallow(dchg=dchg, dnow=vkey_prev)
                return dnow
            else:
                # same result
                # dnow[items[-1]] = dchg
                vkey_prev = dchg
                return dnow
        return dnow

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

    def merge_shallow(self, dchg={}, dnow={}):
        """
        must be the same depth
        """
        # first loop
        for key in dnow.keys():
            if key in dchg:
                # replace or update with new value at the same depth
                dnow[key] = dchg.get(key)

        # second loop
        for key in dchg.keys():
            if key not in dnow:
                # add a new entry
                dnow[key] = dchg.get(key)
        return dnow
