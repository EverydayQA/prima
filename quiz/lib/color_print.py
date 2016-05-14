#!/usr/bin/python
import sys

class ColorPrint(object):
    def __init__(self):
        (BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE) = range(8)
        self.BLACK = BLACK
        self.RED = RED
        self.GREEN = GREEN
        self.YELLOW = YELLOW
        self.BLUE = BLUE
        self.MAGENTA = MAGENTA
        self.GYAN = CYAN
        self.WHITE = WHITE


    def has_colours(self, stream):
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
    def color_string(self, text, colour):
        if self.has_colours:
            seq = "\x1b[1;%dm" % (30+colour) + text + "\x1b[0m"
            return seq
        else:
            return text

    def printout(self, text, colour):
        if self.has_colours:
            seq = "\x1b[1;%dm" % (30+colour) + text + "\x1b[0m"
            sys.stdout.write(seq)
        else:
            sys.stdout.write(text)


def main():
    cp = ColorPrint()
    # not sure what this line is for?!
    #has_colours = cp.has_colours(sys.stdout)
    cp.printout("xxxx" , cp.GREEN)

if __name__ == '__main__':
    main()

