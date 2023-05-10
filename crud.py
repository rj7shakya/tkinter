import tkinter as tk
from tkinter import Listbox, Button, Entry

import pymysql.cursors

connection = pymysql.connect(host='localhost',
                             user='rajad',
                             password='rajad',
                             database='crud',
                             )

cur = connection.cursor()
cur.execute("SELECT  * FROM names")
data = cur.fetchall()
cur.close()

mainWindow = tk.Tk()
lb = Listbox(mainWindow)

for i in data:
    lb.insert(lb.size(), i[0])


def remove():
    data = lb.get(lb.curselection())
    # print('data', data,  'index', lb.curselection())
    cur = connection.cursor()
    cur.execute("DELETE FROM names WHERE name=%s", (data,))
    connection.commit()
    lb.delete(lb.curselection())


def add():
    global entry
    data = entry.get()
    # print('data', data, 'size', lb.size())
    cur = connection.cursor()
    cur.execute(
        "INSERT INTO names (name) VALUES (%s)", (data,))
    connection.commit()
    lb.insert(lb.size(), data)
    entry.delete(0, 'end')
    # lb.delete(lb.curselection())


entry = Entry(mainWindow, width=20)
entry.focus_set()
entry.place(x=60, y=10)

a_btn = Button(mainWindow, text='Add', command=add)
a_btn.place(x=260, y=8)

r_btn = Button(mainWindow, text='Remove Selected', command=remove)
r_btn.place(x=330, y=8)

lb.place(x=150, y=50)


mainWindow.title('Crud App')
mainWindow.geometry('500x500')
mainWindow.resizable(True, True)
mainWindow.mainloop()
