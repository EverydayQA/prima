import logging
import sys
from termcolor import cprint
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

    def parse_selected_input(self, s):
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

    def select_raw_input(self, items, prompt):
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
        return inputstr

    def get_input(self, timeout=20):

        rlist,  _,  _ = select([sys.stdin], [], [], timeout)
        if rlist:
            s = sys.stdin.readline()
        else:
            print("timeout")
        return s

    def pre_selection(self, items, prompt):
        # refactor to a func
        index = 0
        for item in items:
            print(str(index) + " ## " + item)
            index = index + 1
        print(prompt)
        print('select: ')

    def select_once(self, items, prompt, timeout=20):
        """
        --timeout
        --prompt
        --separator
        --cycle(number of times to make it right)

        --search
        --range check
        --limit 0 or 1 or any
        --default if no selections
        """
        self.pre_selection(items, prompt)
        s = self.get_input(timeout=timeout)
        sels = self.parse_selected_input(str(s))
        return sels

    def get_valid_items(self, sels, items):
        if not sels:
            return None
        maxindex = len(items)

        selections = []
        for sel in sels:
            if sel >= maxindex:
                return False
            selections.append(items[sel])
        return selections

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
            sels = self.select_once(items, prompt, timeout=timeout)
            print(sels)
            selected = self.get_valid_items(sels, items)
            print(selected)
            if selected:
                return selected
            count = count + 1
            cprint('try another selection', 'yellow')
            if count > 5:
                # max cycles
                return None
        return None
