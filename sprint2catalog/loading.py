import tkinter as tk
from window import MainWindow
import threading
import requests

class Loading:
    def __init__(self, root):
        self.root = root;
        self.root.title("CARGANDO...")
        self.root.geometry("170x120") # Esto crea el tamaño por defecto de la ventana
        self.root.resizable(False, False) #No le dejamos redimensionar x ni y
        self.label = tk.Label(self.root, text="Cargando datos...", font=("arial", 14))
        self.label.pack(side=tk.TOP, pady=10)

        label_bg_color = self.label.cget("bg") # guardamos el color de la ventana default en la variable

        self.canvas = tk.Canvas(self.root, width=60, height=60, bg=label_bg_color) #Creamos el canvas donde va a estar el progress bar
        self.canvas.pack()

        self.progress = 0 
        self.draw_progress_circle(self.progress)
        self.update_progress_circle()

        self.thread = threading.Thread(target=self.fetch_json_data) #movemos el progress var a otro hilo que no sea el principal
        self.thread.start()



    def draw_progress_circle(self, progress):
        self.canvas.delete("progress") #eliminamos el progress anterior
        angle = int(360 * (progress/100))

        self.canvas.create_arc(10, 10, 35, 35, start = 0, extent=angle, tags="progress", outline='green', width=5, style=tk.ARC ) ##Aqui creamos el cuadrado donde se va generar dentro el circulo el tk.ARC define el arco y que no tenga por dentro color.
    
    def update_progress_circle(self):
        if self.progress < 100:
            self.progress+=10
        else:
            self.progress=0
        
        self.draw_progress_circle(self.progress)
        self.root.after(200, self.update_progress_circle)#aqui definimos el tiempo entre que se ejecuta el metodo update.
    
