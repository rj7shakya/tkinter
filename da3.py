import tkinter as tk
from tkinter import Button, Listbox, Entry

import pymysql.cursors


connection = pymysql.connect(
    host='localhost',
    user='rajad',
    password='rajad',
    database='crud',
)

cur = connection.cursor()
cur.execute("SELECT  * FROM names")
data = cur.fetchall()
cur.close()


m = tk.Tk()

lb = Listbox(m)
for i in data:
    lb.insert(lb.size(), i[0])

lb.pack()


def onDelete():
    data = lb.get(lb.curselection())
    cur = connection.cursor()
    cur.execute("DELETE FROM names WHERE name=%s", (data,))
    connection.commit()
    lb.delete(lb.curselection())


delBtn = Button(m, text='Delete',
                command=onDelete)
delBtn.pack()


m.geometry("500x500")
m.title('CRUD App')
m.mainloop()
