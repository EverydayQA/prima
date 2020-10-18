from beautifulsoup import BeautifulSoup

fp = open('test2.xml')
soup = BeautifulSoup(fp, 'xml')

items =  soup.find_all('oif-name')

for item in items:
    print item
    print item.get_text()
