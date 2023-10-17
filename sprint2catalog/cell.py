import tkinter as tk
from PIL import Image, ImageTk

class Cell:
    def __init__(self, title, img, description):
        self.title = title
        self.img = (Image.open(img)).resize((100, 100), Image.Resampling.LANCZOS) ## Redimensionar imagen de la celda
        self.description = description


