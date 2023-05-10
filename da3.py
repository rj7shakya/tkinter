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


m.geometry("500x500")
m.title('CRUD App')
m.mainloop()
