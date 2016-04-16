#!/usr/bin/python
import sys
BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE = range(8)

def has_colours(stream):
    if not hasattr(stream , "isatty"):
        return False
    if not stream.isatty():
        return False

    try: 
        import curses
        curses.setupterm()
        return curses.tigetnum("colors") >2
    except:
        return False

has_colours = has_colours(sys.stdout)

def printout(text, colour=WHITE):
    if has_colours:
        seq = "\x1b[1;%dm" % (30+colour) + text + "\x1b[0m"
        sys.stdout.write(seq)
    else:
        sys.stdout.write(text)

printout("[debug] ", GREEN)
print("in green")
printout("[debug] ", YELLOW)
print("in green")
printout("[debug] ", RED)
print("in green")
printout("[debug] ", BLUE)
print("in green")

path = '/shared/xx/yy/zz/aa/bb/cc/'
items = path.split('/')
print items
path_back = '/'.join(items)
print path_back

items = path.strip('/').split('/')
print items

