import tkinter
import tkinter.ttk

def add():
    stringArr.append(entryinput.get())
    label['text'] = stringArr
    entryinput.delete(0,"end")

tk = tkinter.Tk()
tk.title("PythonTodo")
stringArr = [];
label = tkinter.Label(tk, text = "aabb")
entryinput = tkinter.Entry(tk)
entryinput.grid(row=0, column = 0)
label.grid(row=1, column = 0)
button = tkinter.Button(tk, text = "plus" , command = add)
button.grid(row = 2, column = 0)
treeview = tkinter.ttk.Treeview(tk, columns=["할일","날짜"], displaycolumns=["할일","날짜"])
treeview.grid(row=3,column=0)
tk.mainloop()
