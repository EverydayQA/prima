import re


class NormalizeString(object):

    def __init__(self):
        """
        Intend to be generic class without taking any vars
        """
        pass

    def strip_chars(self):
        return ['/', ':', '_']

    def r_strip(self, line):
        if not line:
            return line
        size = len(line)
        for char in self.strip_chars():
            line = line.strip()
            line = line.strip(char)
            line = line.strip()
        if len(line) == size:
            return line
        return self.r_strip(line)

    def normalize_key(self, key):
        if not key:
            return key
        key = self.r_strip(key)
        if not key:
            return key
        key = key.replace(' ', '-')
        return key

    def normalize_value(self, value):
        if not value:
            return value
        # rermove <;>
        value = value.strip(';')

        # remove leading and trailing tab space
        value = value.strip()

        # remove <\\n>
        value = value.replace('\\n', '')

        # replace <\\> with <\>
        value = value.replace('\\\\', '\\')
        # find all instances of ""
        matches = re.findall(r'\"(.+?)\"', value)
        if not matches:
            return value

        items = []
        for match in matches:
            match = match.strip()
            # multiple spaces into one
            match = ' '.join(match.split())
            match = match.rstrip('_')
            if match:
                items.append(match)
        if not items:
            return ''
        if len(items) == 1:
            return items[0]
        return items
