from tkinter import ttk, messagebox
import tkinter as tk
from cell import Cell
from detail_window import showDetail
from PIL import Image, ImageTk
from io import BytesIO
import threading
import requests

class MainWindow:
    cells = []
    def __init__(self,root, json_data):
        self.root = root
        root.title("Animales")
        for  animal in json_data:
            name = animal.get("name")
            description = animal.get("description")
            image_url = animal.get("image_url")
            self.thread = threading.Thread(target=self.load_image, args =(name,image_url, description)) # mandamos a otro hilo la ejecución de convertir de la url a imagen dandole el target de la funcion y los argumentos que le enviamos.
            self.thread.start()

        for i, cell in enumerate(self.cells):
            label = ttk.Label(self.root, image=cell.img, text=cell.title, compound= tk.BOTTOM) ## Imagen y label title
            label.grid(row=0,column=i)
            ##label.bind("<Button-1>",lambda event, celda = cell: showDetail(celda)) 

    def load_image(self, name, url, desc):
        response = requests.get(url)
        img_data = Image.open(BytesIO(response.content))
        img = ImageTk.PhotoImage(img_data)
        cell = Cell(name, img, desc)
        self.cells.append(cell)
