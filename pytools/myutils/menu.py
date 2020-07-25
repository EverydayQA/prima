import logging
import re
import sys
import time
# selectors2
from select import select

logger = logging.getLogger(__name__)


class Menu(object):
    """
    a solid menu is the start of everything
    """

    def __init__(self, *args, **kwargs):
        self.kwargs = kwargs
        self.args = args

    @property
    def fake(self):
        return 'fake'

    def get_selections(self, s):
        """
        - range 0-3
        separator space only, comma not supported
        tight on the rules instead of guessing
        """
        sels = []

        # 0-2 only, 0 - 2 not supported

        # 0-2 4 6 9-16

        # 0-2,4,6,9-12 not supported

        if ',' in s:
            return None

        s = s.rstrip()
        items = s.split(' ')
        if '-' in items:
            return None
        for item in items:
            if '-' in item:
                eles = item.split('-')
                ss = range(int(eles[0]), int(eles[1]) + 1)
                sels.extend(ss)
            else:
                sels.append(int(item))
        return sels

    def select_once(self, items, prompt):
        """
        --timeout
        --prompt
        --search
        --range check
        --separator
        --cycle(number of times to make it right)
        --limit 0 or 1 or any
        --default
        """
        t1 = time.time()

        index = 0
        for item in items:
            print(str(index) + " ## " + item)
            index = index + 1

        print(prompt)
        if sys.version_info[0] > 2:
            # input of py2 only accept number, string is needed
            inputstr = input('range or number:')
        else:
            inputstr = raw_input('range or number:')

        t2 = time.time()
        print(t1)
        print(t2)
        print("inputstr {}".format(inputstr))

        print("select to wair srsin: ")
        rlist, _, _ = select([sys.stdin], [], [], 10)
        if rlist:
            s = sys.stdin.readline()
            print(s)
        else:
            print("timeout")
        sels = self.get_selections(str(inputstr))
        return sels

    def select_from_menu(self, items, prompt, cycle=3, timeout=30):
        """
        args class for this?
        --check max < len(items), duplicated
        --cycle, default 3 max 5
        --timeout
        --warning
        --limit
        --search a b --and --or
        """
        count = 0
        sels = []
        while count < cycle:
            # timeout
            sels = self.select_once(items, prompt)
            count = count + 1
            if sels:
                # --check
                return sels
            if count > 5:
                # max cycles
                return None
        return None

    def todo(self):
        """
        max number of times to choose
        number 0 - all
        separator
        range index check
        timeout
        search + --and --or
        """
        pass


def print_format_table():
    for style in range(8):
        for fg in range(30, 38):
            s1 = ''
            for bg in range(40, 48):
                format = ';'.join([str(style), str(fg), str(bg)])
                s1 += '\x1b[%sm %s \x1b[0m' % (format, format)
            print(s1)
        print('\n')


def get_input():
    input_str = input("Please select one or more from the list: ")
    return input_str


def print_menu(items):
    index = 0
    for item in items:
        print('{} ## {}'.format(index, item))
        index = index + 1


def select_from_list(items):
    # multiple select
    logger.info('select_from_list')
    print_menu(items)
    input_str = get_input()
    sels = parse_input_string(input_str)
    selections = selections_in_list(sels, items)
    return selections


def selections_in_list(sels, items):
    selections = []
    for sel in sels:
        try:
            sel = int(sel)
            index = sel
            selections.append(items[index])
        except Exception as e:
            print(e)
    return selections


def parse_input_string(s):
    """
    - range 0-3
    separator space comma
    """
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
    count_comma = s.count(",")
    # what about 2 spaces by mistake --confirmation
    count_space = s.count(" ")
    if count_comma == 0 and count_space == 0:
        selections.append(s)
    elif count_space > 0:
        selections = re.split(' ', s)
    elif count_comma > 0:
        selections = re.split(',', s)
    return selections
