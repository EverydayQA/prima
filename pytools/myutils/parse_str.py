

class ParseStr(object):

    def __init__(self):
        self.rstr = 'aaa_bbb_bccc_eddbccd.txt'

    def parse(self):
        print(self.rstr)
        found = []
        found = self.rparse(self.rstr, found=[], not_include=self.not_include)
        print(found)

    @property
    def not_include(self):
        return ['aaa', 'bccc', 'ddd']

    def rparse(self, rstr, found=[], not_include=[]):
        """
        rstr -- any part of the original string
        found -- found items so far in list from the start
        remainingstr -- string not decided yet
        not_include -- not changed for now
        """
        print('\n\n** rparse {}'.format(rstr))
        print('not {}'.format(not_include))
        change = 'bcc'
        if change not in rstr:
            found.append(rstr)
            print('change not in rstr {}'.format(rstr))
            print('use new string')
            found_str = ''.join(found)
            index = len(found_str)
            newstr = self.rstr[index:]
            print(newstr)
            return self.rparse(newstr, found=found, not_include=not_include)

        # func -- none of the notinclude in the string
        print('decide rstr {} has not no item in list {}'.format(rstr, not_include))
        if not self.iteminlist(rstr, not_include):
            # split the change
            print('split change {}'.format(change))
            items = self.rsplit(change, rstr)
            found.extend(items)
            return found

        # rstr contains notinclude
        for ninc in not_include:
            if ninc in rstr:
                items = self.rsplit(ninc, rstr)
                for item in items:
                    if item in found:
                        found.append(item)
                    elif len(item) < len(change):
                        found.append(item)
                    elif item == change:
                        found.append(item)
                    elif item == ninc:
                        found.append(item)
                    else:
                        return self.rparse(item, found=found, not_include=not_include)
        return found

    def iteminlist(self, rstr, not_include):
        for item in not_include:
            if item in rstr:
                return True
        return False

    def rsplit(self, ninc, rstr):
        items = rstr.split(ninc)
        found = []
        for item in items:
            if not item:
                found.append(ninc)
                continue
            found.append(item)
            found.append(ninc)
        found.pop(-1)
        return found


if __name__ == '__main__':
    par = ParseStr()
    par.parse()
