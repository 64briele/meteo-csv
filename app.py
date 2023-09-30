import tkinter as tk
from tkinter import ttk
import os
from modules import estraiData
from modules import plot

def select():
    curItems = tree.selection()
    rows = [tree.item(i, 'values') for i in curItems]
    tuple_rows = tuple(rows)
    for i in range(len(tuple_rows)):
        plot('./csv/' + tuple_rows[i][0])

root = tk.Tk()
root.title('Demo Centralina')
root.resizable(False, False)

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

tree.bind('<Motion>', 'break')
tree.grid(row=0, column=0, sticky='nsew')

scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.grid(row=0, column=1, sticky='nsew')

genera_grafico = ttk.Button(root, text="Genera Grafico")
genera_grafico.grid(row=1, column=2)
genera_grafico.bind("<Button-1>", lambda e: select())

root.mainloop()
