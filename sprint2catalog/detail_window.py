from tkinter import ttk
import tkinter as tk
import cell as Cell

def showDetail(cell):
    det_root = tk.Toplevel() ##Con Toplevel abrimos una pestaña nueva 
    det_root.title(cell.title)
    label = ttk.Label(det_root, image=cell.image_tk, text=cell.title, compound= tk.BOTTOM) ## label imagen titulo
    label2 = ttk.Label(det_root, text=cell.description) ## label de descripcion
    label.pack()
    label2.pack() ## label packeado para su visualización
    det_root.mainloop()
