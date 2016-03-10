#!/usr/bin/python
import datetime
d = datetime.datetime.now()
format = '%d/%m/%Y'
str = d.strftime(format)
ptime = d.strptime(str, format)
str2 = ptime.strftime(format)
print (str)
print (str2)

#get_ipython().magic(u'save test 1-31 test.py')
