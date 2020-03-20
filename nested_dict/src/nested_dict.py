import collections


class NestedDict(object):
    """
    Before a nested dict in installed, this will be tested and used
    """

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

    def d_deep_get(self, d_original, keys, default=None):
        items = list(keys)
        return self.deep_get_recursive(d_original, items)

    def deep_get_recursive(self, d, keys):
        if not d:
            return None
        if not keys:
            return None
        if isinstance(d, dict):
            key = keys.pop(0)
            dv = d.get(key, None)
            if isinstance(dv, dict):
                return self.deep_get_recursive(dv, keys)
            else:
                return dv
        else:
            return d

    def deep_get(self, d, keys):
        """
        return reduce(lambda d, k: d.get(k) if d else None, keys, sourceDict)
        """
        dtmp = d
        for key in keys:
            dtmp = dtmp.get(key, None)
            if isinstance(dtmp, dict):
                pass
            else:
                return dtmp
        return dtmp

    def deep_set(self, sourceDict, value, keys):
        # pop() the last item of the list, use your deepGet on it and set the popped off key on the resulting dict
        items = list(keys)
        last_key = items.pop()
        d = self.deep_get(sourceDict, items)
        d[last_key] = value
        return sourceDict
