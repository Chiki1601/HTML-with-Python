from tkinter import *
from tkhtmlview import HTMLLabel

r = Tk()


# We could use any html inside that HTML attribute!
# HTML-label has the same syntax like The normal Labels.
HTMLLabel(r, html='<a href="https://www.google.com">Hello world</a>').pack()

r.mainloop()