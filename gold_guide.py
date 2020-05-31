#!/usr/bin/python3
from tkinter import *
import app.py

def startClicked():
	start_button.configure(text="Started!", bg="#28a745")

def quitClicked():
	window.destroy()




window = Tk(className = 'GOLDesp Guide 1.0')
window.geometry("400x200")
window.configure(bg="#f8f9fa")

menu = Menu(window)
new_item = Menu(menu, tearoff=0)
new_item.add_command(label='Start Guide', command=startClicked)
new_item.add_separator()
new_item.add_command(label='Quit', command=quitClicked)
menu.add_cascade(label='File', menu=new_item)
window.config(menu=menu)

title_lbl = Label(window, text="GOLDesp Guide v1.0", bg="blue", font=("Arial Bold", 25))
start_button = Button(window, text="Start Guide", bg="#6c757d", command=startClicked)
quit_btn = Button(window, text="Quit", command=quitClicked)

title_lbl.grid(column=0, row=0)
start_button.grid(column=0, row=1)
quit_btn.grid(column=1, row=2)

window.mainloop()

	