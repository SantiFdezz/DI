from tkinter import ttk, messagebox
import tkinter as tk
from cell import Cell
from detail_window import showDetail

class MainWindow:
    cells = []
    def __init__(self,root, json_data):
        self.root = root
        root.title("Animales")
        x = (self.root.winfo_screenwidth() - self.root.winfo_reqwidth()) / 2 ##screenwidth devuelve el ancho de la pantalla,  y reqwidth nos devuelve la anchura en pixels de la ventana.
        y = (self.root.winfo_screenheight() - self.root.winfo_reqheight()) / 2
        self.root.geometry(f"+{int(x)}+{int(y)}") # Esto crea el tamaño por defecto de la ventana
        #self.root.resizable(False, False) #No le dejamos redimensionar x ni y
        barras_menu = tk.Menu()
        menu_Ayuda = tk.Menu(barras_menu, tearoff=False)## creamos el primer menú
        menu_Ayuda.add_command(label="Acerca de",command=self.show_info) ##añadimos al menu Ayuda la entrada Acerca De
        barras_menu.add_cascade(menu=menu_Ayuda, label="Ayuda")
        self.root.config(menu=barras_menu)
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
    
    def show_info(self):
        messagebox.showinfo("Acerca De ", "Desarollador: Fdezz1t0")
        
