import DbHandler
import Task
from tkinter import *

def createTask():
	task = Task.Task(name.get(), description.get())
	task.showTask()
	DbHandler.save(task)
	name.delete(0,END)
	description.delete(0,END)

if __name__ == '__main__':
	window = Tk()
	Label(window, text="Name").grid(row=0)
	Label(window, text="Description").grid(row=1)

	name = Entry(window)
	description = Entry(window)

	name.grid(row=0, column=1)
	description.grid(row=1, column=1)

	Button(window, text='Save', command=createTask).grid(row=3, column=0, sticky=W, pady=4)
	Button(window, text='Quit', command=window.quit).grid(row=3, column=1, sticky=W, pady=4)

	mainloop()