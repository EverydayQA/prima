import random


class PopItem(object):

    def __init__(self):
        d = {'a': 'A', 'b': 'B'}
        self.d = d
        self.keys_list = d.keys()
        self.values_list = d.values()

    def popitem(self):
        number = self.keys_list[random.randint(0, len(self.keys_list) - 1)]
        print number
        i = 0
        while i < len(self.values_list):
            print i
            if i == number:
                needed_key = self.keys_list[i]
                needed_value = self.values_list[i]
                self.keys_list.remove(needed_key)
                self.values_list.remove(needed_value)
                return (needed_key, needed_value)
            i = i + 1
