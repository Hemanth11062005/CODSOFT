from tkinter import *

tasks = []

def addtask():
    task = taskentry.get()
    if task:
        tasks.append(task)
        update_task()

def removetask():
    selected_index = tasklistbox.curselection()
    if selected_index:
        index = selected_index[0]
        del tasks[index]
        update_task()

def update_task():
    tasklistbox.delete(0,END)
    for task in tasks:
        tasklistbox.insert(END,task)

window = Tk()
window.title("To-Do List App")

taskentry = Entry(window,width=40)
taskentry.grid(row=0,column=0,padx=5,pady=5)

addbutton = Button(window,text = "Add task",command = addtask)
addbutton.grid(row =0, column=1, padx=5,pady=5)

tasklistbox = Listbox(window,width=50)
tasklistbox.grid(row=1,column=0,columnspan=2,padx=5,pady=5)

removebutton = Button(window,text = "Remove Task",command = removetask)
removebutton.grid(row = 2,column =0,columnspan=2,padx=5,pady=5)

exitbutton = Button(window,text="Exit",command=window.quit)
exitbutton.grid(row=3,column=0,columnspan=2,padx=5,pady=5)

window.mainloop()

    