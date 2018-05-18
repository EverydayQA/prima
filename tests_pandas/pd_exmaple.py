import pandas as pd
import numpy as np
from pprint import pprint


df = pd.DataFrame([[2009, 1, 15, 'City1', 'Housing'],  [2010, 2, np.nan, 'City2', 'Housing']], columns=['year', 'month', 'day', 'city', 'sector'])
pprint(df)

df['day'] = 15
df['date'] = pd.to_datetime(df[['year', 'month', 'day']])
ind = df.set_index(['date', 'sector', 'city'], drop=False).sort_index()
cols = ['month', 'year', 'sector']
per_city = ind.loc[(slice(None), slice(None), 'City1'), cols].dropna(how='any')
item = per_city.unstack()
pprint(item)

d = {
    'vote': [100, 50, 1, 23, 55, 67, 89, 44],
    'vote2': ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'],
    'ballot1': [None, False, -1, True, 'b', 'a', 'c', ''],
    'voteId': [1, 2, 3, 4, 5, 6, 7, 8]}
d1 = {
    'vote': [100, 50, 1, 23, 55, 67, 89, 44],
    'vote2': [10, 'a', 18, 55, 77, 99, 9, 40],
    'ballot1': [1, None, 3, 4, 5, 6, 7, 8],
    'voteId': [1, 2, 3, {}, 5, 6, 7, 8]}
d2 = {
    'vote': [10, None, 2, 23, 55, 67, 89, 44],
    'vote2': [10, 2, 3, 55, 77, 99, 9, 40],
    'ballot1': [1, '', 3, 4, 5, 6, 7, 8],
    'voteId': ['a', True, 'a', 'a', 'c', 'a', 'c', 'a']}

pprint(d)
df1 = pd.DataFrame(d, dtype=np.float32)
df1 = df1.drop_duplicates(['voteId', 'ballot1'], keep='last')

print('df1 len {}'.format(len(df1)))
pprint(df1)
print(pd.__version__)
print('df1 is mixed type {}'.format(df1._is_mixed_type))
# index?
print('set maximum size to be :10 dfx')
s = df1[:6].set_index(['voteId', 'ballot1'], verify_integrity=True).unstack()
pprint(s)
print(pd.__version__)
print('s is mixed type {}'.format(s._is_mixed_type))

# s.columns = s.columns.map('(ballot1={0[1]}){0[0]}'.format)
# dflw = pd.DataFrame(s)
# print(type(dflw))


def foo_func_first():
    foo = pd.DataFrame(np.random.randn(2, 3), columns=['aaa', 'bbb', 'ccc'])
    pprint(foo)
    foo.to_hdf('foo.h5', 'foo')
    bar = pd.read_hdf('foo.h5', 'foo')
    pprint(bar)


class Col(object):

    def __init__(self, name, other_info):
        self.name = name
        self.other_info = other_info

    def __str__(self):
        return self.name


def foo_func():
    foo = pd.DataFrame(np.random.randn(2, 3), columns=[Col('aaa', {'z': 5}), Col('bbb', {'y': True}), Col('ccc', {})])
    pprint(foo)
    df = foo.unstack()
    foo.to_hdf('foo.h5', 'foo')
    bar = pd.read_hdf('foo.h5', 'foo')
    pprint(bar)


foo_func()
