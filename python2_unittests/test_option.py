from Tkinter import StringVar
from Tkinter import OptionMenu
from Tkinter import Tk
from Tkinter import Button
from Tkinter import mainloop

root = Tk()
ex1 = StringVar(root)
ex1.set("Pick Option")
option = OptionMenu(root, ex1, "one", "two", "three")
option.pack()


def choice():
    chosen = ex1.get()
    print 'chosen {}'.format(chosen)
    ex1.set(chosen)
    root.quit()


button = Button(root, text="OK", command=choice)

button.pack()
mainloop()

print 'The final chosen value {}'.format(ex1.get())
