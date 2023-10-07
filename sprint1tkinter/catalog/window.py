from tkinter import ttk, messagebox
import tkinter as tk
from cell import Cell
from PIL import Image, ImageTk
from detail_window import DetailWindow

class MainWindow():
    def on_button_clicked(self, cell):
        message = "Has hecho click en el "+cell.title
        messagebox.showinfo("Informacion", message)

    def __init__(self, root):
        self.root = root
        root.title("Animales")
        self.cells = [
            Cell("León", "C:\\msys64\\home\\Fdezz1t0\\DI\\sprint1tkinter\\catalog\\data\\unedited\\lion.jpg", "El tigre es un gran felino rayado."),
            Cell("Ardilla", "C:\\msys64\\home\\Fdezz1t0\\DI\\sprint1tkinter\\catalog\\data\\unedited\\squirrel.jpg", "La ardilla es un roedor saltarín."),
            Cell("Panda", "C:\\msys64\\home\\Fdezz1t0\\DI\\sprint1tkinter\\catalog\\data\\unedited\\panda.jpg", "El panda es un oso de peluche."),
            Cell("Mapache", "C:\\msys64\\home\\Fdezz1t0\\DI\\sprint1tkinter\\catalog\\data\\unedited\\racoon.jpg", "El mapache es nocturno y astuto."),
            Cell("Tigre", "C:\\msys64\\home\\Fdezz1t0\\DI\\sprint1tkinter\\catalog\\data\\unedited\\tiger.jpg", "El tigre es un depredador poderoso.")
        ]

        for i, cell in enumerate(self.cells):
            img = (Image.open(cell.path)).resize((100, 100), Image.Resampling.LANCZOS)
            cell.image_tk = ImageTk.PhotoImage(img)
            label = ttk.Label(root, image=cell.image_tk, text=cell.title, compound= tk.BOTTOM)
            label.grid(row=0,column=i)
            label.bind("<Button-1>",lambda event, celda = cell: self.on_button_clicked(celda))
