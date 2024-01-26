

from tkinter import *
from tkinter import messagebox
import pyperclip

root = Tk()
root.title("محاسبه‌گر خسارت دارویی")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = int( (screen_width/2) - (500/2) )
y = int( (screen_height/2) - (500/2) )
root.geometry(f"{400}x{200}+{x}+{y}")
root.config(bg = "#e6e6e6")
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.rowconfigure(0,weight=1)
root.rowconfigure(1,weight=1)
root.rowconfigure(2,weight=1)

root.attributes("-topmost", True)
focus_index = 0

def is_empty(var):
    if var.get() == 0 or var.get() =="0" or var.get() =="":
        return True
    else:
        return False


def set_zero():
    for val in values:
        if val.get() == "":
            val.set("0")

def evaluate():
    for val in values:
        val.set(eval(val.get()))

def calculate(e):
    set_zero()
    evaluate()

    if not is_empty(Bimar) and not is_empty(Pay):
        ghabel_pardakht = ((int(Pay.get()) - int(Bimar.get())) *0.9) + int(Bimar.get())
        print(int(ghabel_pardakht))
        pyperclip.copy(int(ghabel_pardakht))
    else:
        print("NOT ENOUGH SLICES")

    for val in values:
        val.set("")

    


def up(e):
    global focus_index
    
    if focus_index == 0:
        focus_index = 1
    else:
        focus_index -= 1

    Entries[focus_index].focus_set()

def down(e):
    global focus_index
    if focus_index == 1:
        focus_index = 0
    else: 
        focus_index += 1

    Entries[focus_index].focus_set()

def entry_clicked(e, entry):
    global focus_index
    focus_index = Entries.index(entry)

root.bind("<Return>", calculate)
root.bind("<Up>", up)
root.bind("<Down>", down)


Bimar = StringVar()
Pay = StringVar()

values = [Bimar,Pay]

def validate(P):

    def multireplace(var):
        value = var.replace("+","")
        value = value.replace("-", "")
        value = value.replace("*", "")
        return value

    if str.isdigit(P) or P == "" or str.isdigit(multireplace(P)):
        return True
    else:
        return False
 

vcmd = (root.register(validate), '%P')


Bimar_label = Label(root, text = "سهم بیمار", font="Bnazanin 14", bg = "#e6e6e6", fg = "black")
Bimar_label.grid(row = 0, column = 1, sticky = NSEW)
Bimar_Entry = Entry(root, textvariable = Bimar, font = "calibri 12", background="#f8f7e6", validate='key', validatecommand=vcmd)
Bimar_Entry.grid(row = 0, column=0)
Bimar_Entry.bind("<1>", lambda x: entry_clicked(x, Bimar_Entry))


Pay_label = Label(root, text = "پرداختی", font="Bnazanin 14", bg = "#e6e6e6", fg = "black")
Pay_label.grid(row = 1, column = 1, sticky = NSEW)
Pay_Entry = Entry(root, textvariable = Pay, font = "calibri 12", background="#f8f7e6", validate='key', validatecommand=vcmd)
Pay_Entry.grid(row = 1, column=0)
Pay_Entry.bind("<1>", lambda x: entry_clicked(x, Pay_Entry))

global image
image = PhotoImage(file = r"calculate.png")
calculate_Button = Button(root, image = image, command=lambda: calculate(1), borderwidth=0)
calculate_Button.grid(row = 2, column= 0, columnspan=2)

Entries = [Bimar_Entry, Pay_Entry]
Entries[focus_index].focus_set()
vars = [ Bimar, Pay]    

root.mainloop()
