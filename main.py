from tkinter import *

def add(arr, string):
    arr.append(string)
    label['text'] = arr
    print(arr)

tk = Tk()
stringArr = [];
label = Label(tk, text = "aabb")
label.pack(side = LEFT, padx = 10, pady = 10)
button = Button(tk, text = "plus" , command = add(stringArr, "a"))
button.pack(sid = LEFT, padx = 10, pady = 10)
tk.mainloop()
