import random
from pprint import pprint


lst1 = [random.randint(1, 100) for i in range(10)]
lst2 = [random.randint(1, 100) for i in range(10)]
lst = list(zip(lst1, lst2))
pprint(lst)

