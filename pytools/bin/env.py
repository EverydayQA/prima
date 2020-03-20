#!/usr/bin/python
import os


for item in os.environ:
    val = os.environ.get(item)
    print item
    print val
