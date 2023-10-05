from tkinter import ttk, messagebox
import tkinter as tk
from cell import Cell
from PIL import Image, ImageTk

class MainWindow():
    def on_button_clicked(self, cell):
        message = "Has hecho click en el "+cell.title
        messagebox.showinfo("Informacion", message)
    def __init__(self, root):
        root.title("Animales")
        self.cells = [
            Cell("Lion", "C:\\msys64\\home\\Fdezz1t0\\DI\\sprint1tkinter\\catalog\\data\\unedited\\lion.jpg"),
            Cell("Squirrel", "C:\\msys64\\home\\Fdezz1t0\\DI\\sprint1tkinter\\catalog\\data\\unedited\\squirrel.jpg"),
            Cell("Panda", "C:\\msys64\\home\\Fdezz1t0\\DI\\sprint1tkinter\\catalog\\data\\unedited\\panda.jpg"),
            Cell("Racoon", "C:\\msys64\\home\\Fdezz1t0\\DI\\sprint1tkinter\\catalog\\data\\unedited\\racoon.jpg"),
            Cell("Tiger", "C:\\msys64\\home\\Fdezz1t0\\DI\\sprint1tkinter\\catalog\\data\\unedited\\tiger.jpg")
        ]

        for i, cell in enumerate(self.cells):
            foto = Image.open(cell.path)
            img = foto.resize((100, 100), Image.Resampling.LANCZOS)

            cell.image_tk = ImageTk.PhotoImage(img)

            label = ttk.Label(root, image=cell.image_tk, text=cell.title, compound= tk.BOTTOM)
            label.grid(row=0,column=i)
            label.bind("<Button-1>",lambda event, celda = cell: self.on_button_clicked(cell))
