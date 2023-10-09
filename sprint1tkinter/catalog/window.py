from tkinter import ttk, messagebox
import tkinter as tk
from cell import Cell
from detail_window import showDetail

class MainWindow:
    ## def on_button_clicked(self, cell):
    ##    message = "Has hecho click en el "+cell.title
    ##    messagebox.showinfo("Informacion", message)
    ##    self.showDetail()## enviamos el constructor con los datos a enviar
    def __init__(self,root):
        self.root = root
        root.title("Animales")
        self.cells = [ ##celdas con datos
            Cell("León", "C:\\msys64\\home\\Fdezz1t0\\DI\\sprint1tkinter\\catalog\\data\\unedited\\lion.jpg", "El león es el rey de la selva."),
            Cell("Ardilla", "C:\\msys64\\home\\Fdezz1t0\\DI\\sprint1tkinter\\catalog\\data\\unedited\\squirrel.jpg", "La ardilla es un roedor saltarín."),
            Cell("Panda", "C:\\msys64\\home\\Fdezz1t0\\DI\\sprint1tkinter\\catalog\\data\\unedited\\panda.jpg", "El panda es un oso de peluche."),
            Cell("Mapache", "C:\\msys64\\home\\Fdezz1t0\\DI\\sprint1tkinter\\catalog\\data\\unedited\\racoon.jpg", "El mapache es nocturno y astuto."),
            Cell("Tigre", "C:\\msys64\\home\\Fdezz1t0\\DI\\sprint1tkinter\\catalog\\data\\unedited\\tiger.jpg", "El tigre es un depredador poderoso.")
        ]
        for i, cell in enumerate(self.cells):
            label = ttk.Label(root, image=cell.image_tk, text=cell.title, compound= tk.BOTTOM) ## Imagen y label title
            label.grid(row=0,column=i)
            label.bind("<Button-1>",lambda event, celda = cell: showDetail(celda)) ## manda a on_button para abrir detail_winwow
