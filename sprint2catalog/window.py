from tkinter import ttk
import tkinter as tk
from cell import Cell
from detail_window import showDetail

class MainWindow:
    cells = []
    def __init__(self,root, json_data):
        self.root = root
        root.title("Animales")
        #self.root.geometry("170x120") # Esto crea el tamaño por defecto de la ventana
        #self.root.resizable(False, False) #No le dejamos redimensionar x ni y
        for  animal in json_data:
            name = animal.get("name")
            description = animal.get("description")
            image_url = animal.get("image_url")
            cell = Cell(name, image_url, description) ##inicializamos la celda
            self.cells.append(cell) ##añadimos la nueva celda a la lista d celdas

        for i, cell in enumerate(self.cells): #Enumeramos las celdas
            label = ttk.Label(self.root, image=cell.image_tk, text=cell.title, compound= tk.BOTTOM) ## Imagen y label title
            label.grid(row=i,column=0)
            label.bind("<Button-1>",lambda event, cell = cell: showDetail(cell)) 

