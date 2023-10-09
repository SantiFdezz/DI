from tkinter import ttk
import tkinter as tk

def showDetail( cell):
    root = tk.Toplevel()
    root.title(cell.title)
    label = ttk.Label(root, image=cell.image_tk) ## label imagen titulo
    label2 = ttk.Label(root, text=cell.description)
    label.pack()
    label2.pack()
    root.mainloop()
