#!/usr/bin/python
import random
list = [random.randrange(1, 100, 1) for _ in range(20)]
list.sort()
print (list)
