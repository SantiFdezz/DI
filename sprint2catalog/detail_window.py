from tkinter import ttk
import tkinter as tk
import cell as Cell

def showDetail(cell):
    det_root = tk.Toplevel() ##Con Toplevel abrimos una pestaña nueva 
    det_root.title(cell.title)
    x = (det_root.winfo_screenwidth() - det_root.winfo_reqwidth()) / 2 ##screenwidth devuelve el ancho de la pantalla,  y reqwidth nos devuelve la anchura en pixels de la ventana.
    y = (det_root.winfo_screenheight() - det_root.winfo_reqheight()) / 2
    det_root.geometry(f"+{int(x)}+{int(y)}") # f lo centra
    label = ttk.Label(det_root, image=cell.image_tk, text=cell.title, compound= tk.BOTTOM) ## label imagen titulo
    label2 = ttk.Label(det_root, text=cell.description) ## label de descripcion
    label.pack()
    label2.pack() ## label packeado para su visualización
    det_root.mainloop()
