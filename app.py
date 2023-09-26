import tkinter as tk
from tkinter import ttk
import os
from modules import estraiData

root = tk.Tk()
root.title('Demo Centralina')
root.geometry('800x600+50+50')
root.columnconfigure(1, weight=0)
root.rowconfigure(0, weight=0)
root.resizable(0, 0)

columns = ('nome_file','data_file')
tree = ttk.Treeview(root, columns=columns, show='headings')
tree.heading('nome_file', text='Nome File')
tree.heading('data_file', text='Data File')

tree_values = [] 
files = (sorted(os.listdir('./csv/')))
for file in files:
    tree_values.append((file, estraiData(file)))

for value in tree_values:
    tree.insert('', tk.END, values=value)

tree.grid(row=0, column=0, sticky='nsew')

scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.grid(row=0, column=1, sticky='nsew')

root.mainloop()
