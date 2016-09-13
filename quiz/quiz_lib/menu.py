import re
import string
#from termcolor import colored
#no rpm avail/ colorPrint()
import logging
logger  = logging.getLogger(__name__)

class Menu:

    def __init__(self, *args, **kwargs):
        self.kwargs = kwargs
        self.args = args

    def select_from_menu(self, the_list, prompt):
        logger.debug('select_from_menu')
        index = 1
        for item in the_list:
            print (str(index) + " ## " + item)
            index = index + 1

        print prompt

        selections = []
        sels = map(int, raw_input("space separated: ").split())
        for sel in sels:
            index = int(sel)
            selections.append(index)
        return selections

def print_format_table():
    for style in xrange(8):
        for fg in xrange(30, 38):
            s1 = ''
            for bg in xrange(40, 48):
                format = ';'.join([str(style), str(fg), str(bg)])
                s1 += '\x1b[%sm %s \x1b[0m' % (format, format)
            print s1
        print '\n'
def get_input():
    input_str = raw_input("Please select one or more from the list: ")
    return input_str

def print_menu(the_list):    
    index = 0
    for item in the_list:
        print str(index) + " ## " + item
        index = index + 1

def select_from_list(the_list):
    # multiple select
    logger.info('select_from_list')
    print_menu(the_list)
    input_str = get_input() 
    sels = parse_input_string(input_str)
    selections = selections_in_list(sels, the_list)
    return selections
    
def selections_in_list(sels, the_list):
    selections = []
    for sel in sels:
        try:
            sel = int(sel)
            index = sel
            selections.append(the_list[index])
        except:
            pass
    return selections

def parse_input_string(s):
    selections = []
    try:
        float(s)
        selections.append(s)
        return selections
    except ValueError:
        pass
    else:
        pass

    s = s.rstrip()
    count_comma =  s.count(",")
    count_space = s.count(" ")
    if count_comma ==0 and count_space ==0:
        selections.append(s)
    elif count_space >0:
        selections = re.split(' ', s)
    elif count_comma >0:
        selections = re.split(',', s)
    return selections
