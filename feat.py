import tkinter
import tkinter.ttk
import time
import json

def add():
    global treeiid
    stringArr.append(entryinput.get())
    treeview.insert("", "end", values=(time.strftime("%Y년 %m/%d %H시 %M분", time.localtime(time.time())), entryinput.get()), iid=treeiid)
    entryinput.delete(0,"end")
    treeiid=treeiid+1

def delitem(self):
    treeview.delete(treeview.selection())

def exitcommand():
    treeview.item
    tmparr = []
 
    for i in treeview.get_children():
        tmparr+=treeview.item(i)["values"]
    print(tmparr)
    with open("data.json", "w") as f:       #tmparr을 json형태로 저장
        json.dump(tmparr, f, indent= "\t")

    tk.destroy()

treeiid = 0
tk = tkinter.Tk()
tk.title("PythonTodo")
tk.protocol("WM_DELETE_WINDOW", exitcommand)

stringArr = []
entryinput = tkinter.Entry(tk, width = 150)
entryinput.grid(row=0, column = 0)

button = tkinter.Button(tk, text = "plus" , command = add, width = 10)
button.grid(row = 0, column = 1)

treeview = tkinter.ttk.Treeview(tk, columns=["날짜","할일"], displaycolumns=["날짜","할일"])
treeview.bind("<Double-1>", delitem)
treeview.column("날짜", width = 200, anchor="center")
treeview.column("할일", width = 1000, anchor="w")
treeview["show"] = "headings"
treeview.grid(row=1,column=0,columnspan=2)


firstarr = []
temp = []

try: #파일이 비어있는 경우 예외처리
    with open("data.json", "r") as f:
        temp = json.load(f)
        for i in range(0, len(temp), 2):        #날짜와 시간을 튜플형으로 변환
            firstarr.append((temp[i],temp[i+1]))

except json.JSONDecodeError:
    firstarr = []            

for i in range(len(firstarr)):
    treeview.insert("", "end", value=firstarr[i],iid=treeiid)
    treeiid=treeiid+1

tk.mainloop()