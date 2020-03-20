import xml2dict
from pprint import pprint


x = xml2dict.XML2Dict()
d = x.parse('./test.xml')
pprint(d)
