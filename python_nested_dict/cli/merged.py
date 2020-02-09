from pprint import pprint
from src.dict_merge import DictMerge


def main():
    print('merge of a dict')
    adict = {'key1': 1, 'key2': 2, 'key3': 3}
    ds = DictMerge(**adict)
    d2 = {'Ritika': 5, 'Sam': 7, 'John': 10}
    d = ds.merge(d2)
    pprint(d)
    ds.demo()


if __name__ == "__main__":
    main()
