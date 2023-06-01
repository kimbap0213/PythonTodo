from tkinter import *

tk = Tk()
stringArr = [];
label = Label(tk, text = "aabb")

def add():
    stringArr.append("aa")
    label['text'] = stringArr

label.pack(side = LEFT, padx = 10, pady = 10)
button = Button(tk, text = "plus" , command = add)
button.pack(sid = LEFT, padx = 10, pady = 10)
tk.mainloop()
