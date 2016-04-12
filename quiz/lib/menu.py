import re
import string

def select_from_menu(the_list):
    index = 0
    for item in the_list:
        print str(index) + " " + item
        index = index + 1

    selections = []
    sels = map(int, raw_input("space separated: ").split())
    for sel in sels:
        index = int(sel)
        selections.append(the_list[index])
    return selections


def select_from_list(the_list):
    # multiple select
    index = 0
    for item in the_list:
        print str(index) + " " + item
        index = index + 1

    
    input_str = raw_input("Please select one or more from the list: ")
    print input_str
    # could be comma or space separated integers
    selections = []
    sels = parse_input_string(input_str)
    for sel in sels:
        index = int(sel)
        selections.append(the_list[index])
    return selections

def parse_input_string(s):
    selections = []

    try:
        float(s)
        selections.append(s)
        return selections
    except ValueError:
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
