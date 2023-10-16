import tkinter as tk
from PIL import Image, ImageTk

class Cell:
    def __init__(self, title, path, description):
        self.title = title
        self.path = path
        ##self.image_tk = ImageTk.PhotoImage(file = self.path)
        self.img = (Image.open(self.path)).resize((100, 100), Image.Resampling.LANCZOS) ## Redimensionar imagen de la celda
        self.image_tk = ImageTk.PhotoImage(self.img) ##abrimos la imagen y igualamos la imagen redimensionada a la vsariable imagen_tk
        self.description = description


