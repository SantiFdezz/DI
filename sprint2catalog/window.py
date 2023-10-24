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
        self.root.resizable(False, False) #No le dejamos redimensionar x ni y
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

        self.canvas = tk.Canvas(self.root)        # Creación del Canvas
        self.scrollbar = tk.Scrollbar(self.root, orient="vertical", command =self.canvas.yview)        # Creación del Scrollbar
        
        # Creamos el frame que servira de scroll
        self.scrollable_frame = tk.Frame(self.canvas)
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )
        #Creamos la pagin en el canvas y configuramos el scrollbar en el propio canvas
        self.canvas.create_window((0,0), window=self.scrollable_frame, anchor= "nw")
        self.canvas.configure(yscrollcommand= self.scrollbar.set)

        for i, cell in enumerate(self.cells):
            self.add_items(cell, i)

        #Config de posicion de la Scrollbar en la ventana
        self.canvas.grid(row=0, column=0, sticky="nsew")
        self.scrollbar.grid(row=0, column=1, sticky="ns")
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

    def add_items(self, cell, i):
        frame = ttk.Frame(self.scrollable_frame)
        frame.pack(pady=10,  padx=140)
        label = ttk.Label(frame, image=cell.image_tk, text=cell.title, compound= tk.BOTTOM) ## Imagen y label title
        label.grid(row=i,column=0, padx=5, pady=5)
        label.bind("<Button-1>",lambda event, cell = cell: showDetail(cell)) 
    
    def show_info(self):
        messagebox.showinfo("Acerca De ", "Desarollador: Fdezz1t0")
        
