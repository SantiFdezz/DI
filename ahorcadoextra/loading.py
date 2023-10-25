import tkinter as tk
from ventana_seleccion import Ahorcado
import threading
import requests

class Loading:
    def __init__(self, root):
        self.finished = False;
        self.json_data = []
        self.root = root;
        self.root.title("CARGANDO...")
        x = (self.root.winfo_screenwidth() - self.root.winfo_reqwidth()) / 2 ##screenwidth devuelve el ancho de la pantalla,  y reqwidth nos devuelve la anchura en pixels de la ventana.
        y = (self.root.winfo_screenheight() - self.root.winfo_reqheight()) / 2
        self.root.geometry(f"+{int(x)}+{int(y)}") # Esto crea el tamaño por defecto de la ventana
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
        if self.thread.is_alive():
            self.check_Thread()




    def draw_progress_circle(self, progress):
        self.canvas.delete("progress") #eliminamos el progress anterior
        angle = int(360 * (progress/100))

        self.canvas.create_arc(10, 10, 35, 35, start = 0, extent=angle, tags="progress", outline='green', width=5, style=tk.ARC ) ##Aqui creamos el cuadrado donde se va generar dentro el circulo el tk.ARC define el arco y que no tenga por dentro color.
    
    def update_progress_circle(self):
        if self.progress < 100:
            self.progress+=14.20
        else:
            self.progress=0
        
        self.draw_progress_circle(self.progress)
        self.root.after(100, self.update_progress_circle)#aqui definimos el tiempo entre que se ejecuta el metodo update.
    
    def fetch_json_data(self):
        response = requests.get("https://raw.githubusercontent.com/SantiFdezz/DI/main/ahorcadoextra/ahorcado/words.json")
        response2 = requests.get("https://raw.githubusercontent.com/SantiFdezz/DI/main/ahorcadoextra/ahorcado/error.json") #cogemos los json de el github
        if response.status_code == 200 and response2.status_code == 200:
            self.json_data = response.json()
            self.json_error = response2.json()
            self.finished = True
        else:
            print("Error al cargar los datos.")
    def check_Thread(self):
        if self.finished:
            self.root.destroy()
            launch_main_window(self.json_data, self.json_error)
        else:
            self.root.after(100, self.check_Thread)

def launch_main_window(json_data, json_error):
    root = tk.Tk()
    app = Ahorcado(root, json_data, json_error)
    root.mainloop()