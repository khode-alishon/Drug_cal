

from tkinter import *
from tkinter import messagebox


root = Tk()
root.title("محاسبه‌گر خسارت دارویی")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = int( (screen_width/2) - (500/2) )
y = int( (screen_height/2) - (500/2) )
root.geometry(f"{400}x{400}+{x}+{y}")
root.config(bg = "#a5d6b8")
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.rowconfigure(0,weight=1)
root.rowconfigure(1,weight=1)
root.rowconfigure(2,weight=1)
root.rowconfigure(3,weight=1)
root.rowconfigure(4,weight=1)
root.rowconfigure(5,weight=1)
root.rowconfigure(6,weight=1)
focus_index = 0



def calculate(e):
    
    #calculate using sahm biamr
    print(total.get())


def up(e):
    global focus_index
    
    if focus_index == 0:
        focus_index = 6
    else:
        focus_index -= 1

    Entries[focus_index].focus_set()

def down(e):
    global focus_index
    if focus_index == 6:
        focus_index = 0
    else: 
        focus_index += 1

    Entries[focus_index].focus_set()

root.bind("<Return>", calculate)
root.bind("<Up>", up)
root.bind("<Down>", down)


total = StringVar()
Bime = StringVar()
Sazman = StringVar()
Bimar = StringVar()
Azad = StringVar()
Exchange = StringVar()
Pay = StringVar()



def validate(P):
    if str.isdigit(P) or P == "":
        return True
    else:
        return False

vcmd = (root.register(validate), '%P')


total_label = Label(root, text = "جمع کل", font="Bnazanin 14", bg = "#a5d6b8", fg = "#0769d1")
total_label.grid(row = 0, column = 1, sticky = NSEW)
total_Entry = Entry(root, textvariable = total, font = "calibri 12", background="#f8f7e6", validate='key', validatecommand=vcmd)
total_Entry.grid(row = 0, column=0)

Bime_label = Label(root, text = "مورد قبول بیمه", font="Bnazanin 14", bg = "#a5d6b8", fg = "#0769d1")
Bime_label .grid(row = 1, column = 1, sticky = NSEW)
Bime_Entry = Entry(root, textvariable = Bime, font = "calibri 12", background="#f8f7e6", validate='key', validatecommand=vcmd)
Bime_Entry.grid(row = 1, column=0)

Sazman_label = Label(root, text = "سهم سازمان", font="Bnazanin 14", bg = "#a5d6b8", fg = "#0769d1")
Sazman_label.grid(row = 2, column = 1, sticky = NSEW)
Sazman_Entry = Entry(root, textvariable = Sazman, font = "calibri 12", background="#f8f7e6", validate='key', validatecommand=vcmd)
Sazman_Entry.grid(row = 2, column=0)

Bimar_label = Label(root, text = "سهم بیمار", font="Bnazanin 14", bg = "#a5d6b8", fg = "#0769d1")
Bimar_label.grid(row = 3, column = 1, sticky = NSEW)
Bimar_Entry = Entry(root, textvariable = Bimar, font = "calibri 12", background="#f8f7e6", validate='key', validatecommand=vcmd)
Bimar_Entry.grid(row = 3, column=0)

Azad_label = Label(root, text = "سهم آزاد", font="Bnazanin 14", bg = "#a5d6b8", fg = "#0769d1")
Azad_label .grid(row = 4, column = 1, sticky = NSEW)
Azad_Entry = Entry(root, textvariable = Azad, font = "calibri 12", background="#f8f7e6", validate='key', validatecommand=vcmd)
Azad_Entry.grid(row = 4, column=0)

Exchange_label = Label(root, text = "مابه‌التفاوت", font="Bnazanin 14", bg = "#a5d6b8", fg = "#0769d1")
Exchange_label.grid(row = 5, column = 1, sticky = NSEW)
Exchange_Entry = Entry(root, textvariable = Exchange, font = "calibri 12", background="#f8f7e6", validate='key', validatecommand=vcmd)
Exchange_Entry.grid(row = 5, column=0)

Pay_label = Label(root, text = "پرداختی", font="Bnazanin 14", bg = "#a5d6b8", fg = "#0769d1")
Pay_label.grid(row = 6, column = 1, sticky = NSEW)
Pay_Entry = Entry(root, textvariable = Pay, font = "calibri 12", background="#f8f7e6", validate='key', validatecommand=vcmd)
Pay_Entry.grid(row = 6, column=0)

Entries = [total_Entry, Bime_Entry, Sazman_Entry, Bimar_Entry, Azad_Entry, Exchange_Entry, Pay_Entry]
Entries[focus_index].focus_set()
vars = [total, Bime, Sazman, Bimar, Azad, Exchange, Pay]    

root.mainloop()