from blessings import Terminal
import time
term  = Terminal()
with term.location():
    print (term.move(0,(term.width/2)-7) + term.bold_green("Test"))
    print (term.move(5,(term.width/2)-7) + term.bold_red("Test"))

time.sleep(5)
term.clear
term.exit_fullscreen



