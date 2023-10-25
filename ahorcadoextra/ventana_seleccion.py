import math
import tkinter as tk
from tkinter import ttk
import random
from random import choice
from ventana_juego import Game

class Ahorcado:
    def __init__(self, root, json_data, json_error):
        self.root = root
        self.root.title("Ahorcado")
        x = (self.root.winfo_screenwidth() - self.root.winfo_reqwidth()) / 2 ##screenwidth devuelve el ancho de la pantalla,  y reqwidth nos devuelve la anchura en pixels de la ventana.
        y = (self.root.winfo_screenheight() - self.root.winfo_reqheight()) / 2
        self.root.geometry(f"+{int(x)}+{int(y)}") # Esto crea el tamaño por defecto de la ventana centrada
        self.root.geometry("175x300")
        self.root.resizable(False,False)
        self.json_data = json_data
        self.json_error = json_error
        label = ttk.Label(self.root, text="Ahorcado")
        description = ttk.Label(self.root, text="[+] Dificultad Facil (3-5 letter)\n[+] Dificultad Normal (6-9 letter) \n[+] Dificultad Dificil (+9 letter)")
        button = ttk.Button(self.root, text="Facil", command= lambda: self.togame("facil"))
        button2 = ttk.Button(self.root, text="Normal", command= lambda: self.togame("normal"))
        button3 = ttk.Button(self.root, text="Dificil", command= lambda: self.togame("dificil"))
        buttonout = ttk.Button(self.root, text="SALIR", command= lambda: self.exit())
        label.pack(side=tk.TOP, pady=10)
        description.pack(side=tk.TOP, pady=10)

        button.pack(side=tk.TOP, fill=tk.X, padx=20) 
        button2.pack(side=tk.TOP, fill=tk.X, padx=20)
        button3.pack(side=tk.TOP, fill=tk.X, padx=20)
        buttonout.pack(side=tk.TOP, fill=tk.X, padx=20, pady=10)

    def togame(self, mode):
        word = random.choice(self.json_data[mode])            
        self.root.withdraw()  # Ocultamos la ventana actual
        self.game = tk.Toplevel(self.root)
        app = Game(self.game, word, mode, self.json_error, self.root)
        self.game.mainloop()

    def exit(self):
        self.root.deiconify()
        self.root.destroy()