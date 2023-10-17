from tkinter import ttk
import tkinter as tk

def showDetail(cell):
    root = tk.Tk() ##Con Toplevel abrimos una pestaña nueva 
    root.title(cell.title)
    label = ttk.Label(root, image=cell.image_tk) ## label imagen titulo
    label2 = ttk.Label(root, text=cell.description) ## label de descripcion
    label.pack()
    label2.pack()## label packeado para su visualización
    root.mainloop()
