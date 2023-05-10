import tkinter as tk
from tkinter import Label, Button, Listbox, Entry
from tkinter import ttk

mainWindow = tk.Tk()

# **** Label ****
# lw = Label(mainWindow, text="Hello World")
# lw2 = Label(mainWindow, text="Hello World")
# lw.config(bg='red', fg='black', padx=20, pady=20)
# lw2.config(bg='red', fg='black', padx=20, pady=20)
# lw.pack()
# lw.grid(row=2, column=2)
# lw2.grid(row=3, column=3)
# lw.place(x=100, y=100)
# lw2.place(x=300, y=300)

# **** Button ****
# def btn_handler():
#     print('clicked!')
# btn = Button(mainWindow, text='Click Me', command=btn_handler)
# btn.pack()

# **** Move Widgets ****
# l1 = Label(mainWindow, bg='red')
# l1.place(x=10, y=10, width=100, height=100)
# def right_key_handler(event):
#     print('event', event)
#     l1.place(x=l1.winfo_x()+8, y=l1.winfo_y())
# mainWindow.bind('<Right>',  right_key_handler)
# mainWindow.bind('<Left>',  right_key_handler)
# mainWindow.bind('<Down>',  right_key_handler)
# mainWindow.bind('<Up>',  right_key_handler)

# **** Input - Entry ****
# label = Label(mainWindow, text="")
# label.pack()


# def display_text():
#     global entry
#     string = entry.get()
#     label.configure(text=string)


# entry = Entry(mainWindow, width=40)
# entry.focus_set()
# entry.pack()

# btn = Button(mainWindow, text="Okay", width=20, command=display_text)
# btn.pack(pady=20)

# **** ListBox ****
# lb = Listbox(mainWindow)
# lb.insert(0, "Apple")
# lb.insert(1, "Android")
# lb.pack()
# # lb.grid(row=1, column=1)


# def remove():
#     data = lb.get(lb.curselection())
#     print('data', data,  'index', lb.curselection())
#     lb.delete(lb.curselection())


# def add():
#     global entry
#     data = entry.get()
#     print('data', data, 'size', lb.size())
#     lb.insert(lb.size(), data)
#     entry.delete(0, 'end')
#     # lb.delete(lb.curselection())


# r_btn = Button(mainWindow, text='Remove', command=remove)
# # r_btn.grid(row=1, column=1)
# r_btn.pack()

# entry = Entry(mainWindow, width=20)
# entry.focus_set()
# entry.pack()

# a_btn = Button(mainWindow, text='Add', command=add)
# # a_btn.grid(row=1, column=2)
# a_btn.pack()


# **** TABS ****
# tabControl = ttk.Notebook(mainWindow)
# tab1 = ttk.Frame(tabControl)
# tab2 = ttk.Frame(tabControl)

# Label(tab1, text="Welcome to GeeksForGeeks").pack()
# Label(tab2, text="Lets dive into the world of computers").pack()

# tabControl.add(tab1, text='Tab 1')
# tabControl.add(tab2, text='Tab 2')

# tabControl.pack(expand=1, fill="both")


mainWindow.title('My GUI')
mainWindow.geometry('500x500')
mainWindow.resizable(True, True)
mainWindow.mainloop()
