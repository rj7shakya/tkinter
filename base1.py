# Import the required libraries
from tkinter import *
from tkinter import ttk

# Create an instance of tkinter frame
win = Tk()

# Set the size of the tkinter window
win.geometry("700x350")

# Create an instance of Style widget
style = ttk.Style()
style.theme_use('clam')

# Add a Treeview widget
tree = ttk.Treeview(win, column=("c1", "c2"), show='headings', height=8)
tree.column("# 1", anchor=CENTER)
tree.heading("# 1", text="ID")
tree.column("# 2", anchor=CENTER)
tree.heading("# 2", text="Company")

# Insert the data in Treeview widget
tree.insert('', 'end', values=('1', 'Honda'))
tree.insert('', 'end', values=('2', 'Hyundai'))
tree.insert('', 'end', values=('3', 'Tesla'))
tree.insert('', 'end', values=('4', 'Wolkswagon'))
tree.insert('', 'end', values=('5', 'Tata Motors'))
tree.insert('', 'end', values=('6', 'Renault'))

# tree.bind('<ButtonRelease-1>',)

tree.pack()

entry1 = Entry(win, width=20)
entry1.pack()

entry2 = Entry(win, width=20)
entry2.pack()


def edit():
    # Get selected item to Edit
    # tree.insert('', 'end', values=(entry1.get(), entry2.get()))
    selected_item = tree.selection()[0]
    print('selected_item', tree.item(selected_item)['values'])
    entry1.insert(0, tree.item(selected_item)['values'][0])
    entry2.insert(0, tree.item(selected_item)['values'][1])
    # tree.item(selected_item, values=(entry1.get(), entry2.get()))


def delete():
    # Get selected item to Delete
    selected_item = tree.selection()[0]
    tree.delete(selected_item)


# Add Buttons to Edit and Delete the Treeview items
edit_btn = ttk.Button(win, text="Add", command=edit)
edit_btn.pack()
del_btn = ttk.Button(win, text="Delete", command=delete)
del_btn.pack()

win.mainloop()
