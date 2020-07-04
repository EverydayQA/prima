from pprint import pprint


class DictMerge(object):

    def __init__(self, **kwargs):
        self.kwargs = kwargs

    def merge(self, d2):
        """
        assume no common keys
        """
        d = dict(self.kwargs)
        d.update(d2)
        pprint(self.kwargs)
        return d

    def merge_with_common_keys(self, d2):
        """
        It depends how the value of the common key being updated
        combine list/add vaue/ etc
        """
        return {}

    def mergeDict(self, dict1, dict2):
        ''' Merge dictionaries and keep values of common keys in list'''
        # python3 only
        dict3 = {**dict1, **dict2}
        for key, value in dict3.items():
            if key in dict1 and key in dict2:
                dict3[key] = [value , dict1[key]]
        return dict3

    def demo(self):

        # Create first dictionary
        dict1 = {  'Ritika': 5, 'Sam': 7, 'John' : 10 }

        # Create second dictionary
        dict2 = {'Aadi': 8,'Sam': 20,'Mark' : 11 }

        print('Dictionary 1 :')
        print(dict1)

        print('Dictionary 2 :')
        print(dict2)

        print('*** Merge two dictionaries using update() ***')

        # Merge contents of dict2 in dict1
        dict1.update(dict2)

        print('Updated dictionary 1 :')
        print(dict1)

        print('*** Merge two dictionaries using ** trick ***')

        # Create first dictionary
        dict1 = {  'Ritika': 5, 'Sam': 7, 'John' : 10 }

        # Create second dictionary
        dict2 = {'Aadi': 8,'Sam': 20,'Mark' : 11 }

        # Merge contents of dict2 and dict1 to dict3
        dict3 = {**dict1 , **dict2}

        print('Dictionary 3 :')
        print(dict3)

        print('*** Merge 3 dictionaries using ** trick ***')

        # Create second dictionary
        dict3 = {'Mark': 18,'Rose': 22,'Wong' : 22 }

        # Merge contents of dict3, dict2 and dict1 to dict4
        dict4 = {**dict1, **dict2, **dict3}

        print('Dictionary 4 :')
        print(dict4)

        print('*** Merge two dictionaries and add values of common keys ***')
        # Create second dictionary

        # Merge contents of dict2 and dict1 to dict3
        print(dict1)
        print(dict2)

        # Merge dictionaries and add values of common keys in a list
        dict3 = self.mergeDict(dict1, dict2)
        print('Dictionary 3 :')
        print(dict3)

        dict3 = {'Mark': 18, 'Rose': 22, 'Wong': 22}

        print(dict3)

        # Merge 3 dictionary and keep values of common keys in a list
        finalDict = self.mergeDict(dict3, self.mergeDict(dict1, dict2))

        print('Final Dictionary :')
        print(finalDict)


def main():
    print('merge of a dict')
    adict = {'key1':1, 'key2':2, 'key3':3}
    ds = DictMerge(**adict)
    d2 = {  'Ritika': 5, 'Sam': 7, 'John' : 10 }
    d = ds.merge(d2)
    pprint(d)
    ds.demo()


if __name__ == "__main__":
    main()
