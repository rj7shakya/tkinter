import tkinter as tk
from tkinter import Label, Button

mainWindow = tk.Tk()

# def onClick():
#     print('Clicked')

# btn = Button(mainWindow, text='click me', command=onClick)
# btn.pack()

l1 = Label(mainWindow, bg='red')
l1.place(x=10, y=10, width=100, height=100)


def rightHandler(e):
    l1.place(x=l1.winfo_x()+8, y=l1.winfo_y())


def leftHandler(e):
    l1.place(x=l1.winfo_x()-8, y=l1.winfo_y())


def upHandler(e):
    l1.place(x=l1.winfo_x(), y=l1.winfo_y()-8)


def DownHandler(e):
    l1.place(x=l1.winfo_x(), y=l1.winfo_y()+8)


mainWindow.bind('<Right>', rightHandler)
mainWindow.bind('<Left>', leftHandler)
mainWindow.bind('<Up>', upHandler)
mainWindow.bind('<Down>', DownHandler)


# lw = Label(mainWindow, text="Hello World")
# lw.place(x=100, y=100)

# lw2 = Label(mainWindow, text="Hello World")
# lw2.place(x=200, y=200)


mainWindow.title('My GUI')
mainWindow.geometry('500x500')
mainWindow.resizable(True, True)
mainWindow.mainloop()
