# tkinter  -> GUI

import tkinter as tk
from tkinter import Entry, Button, Listbox

main = tk.Tk()

listBox1 = Listbox(main)
listBox1.insert(0, 'suman')
listBox1.pack()

input1 = Entry(main)
input1.pack()


def onAdd():
    listBox1.insert(listBox1.size(),
                    input1.get())
    input1.delete(0, 'end')


b1 = Button(main, text='Add', command=onAdd)
b1.pack()


def onDelete():
    listBox1.delete(listBox1.curselection())


b2 = Button(main, text='Delete', command=onDelete)
b2.pack()

main.geometry('500x500')
main.mainloop()
