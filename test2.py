<<<<<<< HEAD
from tkinter import *



root = Tk()
root.geometry("400x400")

def entry_callback(e, entry):
    print(entry)

entry1 = Entry(root)
entry1.pack()
entry1.bind("<1>", lambda x: entry_callback(x, "entry 1 clicked"))

entry2 = Entry(root)
entry2.pack()
entry2.bind("<1>", lambda x: entry_callback(x, "entry 2 clicked"))


=======
from tkinter import *



root = Tk()
root.geometry("400x400")

def entry_callback(e, entry):
    print(entry)

entry1 = Entry(root)
entry1.pack()
entry1.bind("<1>", lambda x: entry_callback(x, "entry 1 clicked"))

entry2 = Entry(root)
entry2.pack()
entry2.bind("<1>", lambda x: entry_callback(x, "entry 2 clicked"))


>>>>>>> 44e3d95bcb8a9603285c7b3f6900dfe3e6fecdad
root.mainloop()