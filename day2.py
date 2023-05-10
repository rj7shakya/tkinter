import tkinter as tk
from tkinter import Label, Entry, Button

main = tk.Tk()

e1 = Entry(main)
e1.place(x=10, y=10)

b1 = Button(main, text='submit')
b1.place(x=200, y=10)


# l1 = Label(main)
# l1.place(x=100, y=100, width=100, height=100)

main.geometry("500x500")
main.resizable(True, True)
main.mainloop()
