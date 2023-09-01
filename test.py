from tkinter import *

root = Tk()

def callback(P):
    if str.isdigit(P) or P == "":
        return True
    else:
        return False

vcmd = (root.register(callback), '%P')

entry = Entry(root, validate='key', validatecommand=vcmd)
entry.pack()


root.mainloop()