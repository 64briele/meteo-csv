import tkinter as tk
from tkinter import ttk
import os

root = tk.Tk()
root.title('Demo Centralina')
root.geometry('800x600+50+50')
root.columnconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

columns = ('nome_file','data_file')
tree = ttk.Treeview(root, columns=columns, show='headings')
tree.heading('nome_file', text='Nome File')
tree.heading('data_file', text='Data File')

files = (sorted(os.listdir('./csv/')))
print(files)

for file in files:
    tree.insert('', tk.END, values=file)

tree.grid(row=0, column=0, sticky='nsew')

scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.grid(row=0, column=1, sticky='ns')

root.mainloop()
