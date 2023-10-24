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
        self.root.geometry("150x400")
        label = ttk.Label(self.root, text="Ahorcado")
        description = ttk.Label(self.root, text="[+] Dificultad Facil (3-5 letter)\n[+] Dificultad Normal (6-9 letter) \n[+] Dificultad Dificil (+9 letter)")
        button = ttk.Button(self.root, text="Facil", command= lambda: self.togame("facil", json_data, json_error))
        button2 = ttk.Button(self.root, text="Normal", command= lambda: self.togame("normal", json_data, json_error))
        button3 = ttk.Button(self.root, text="Dificil", command= lambda: self.togame("dificil", json_data, json_error))
        buttonout = ttk.Button(self.root, text="SALIR", command= lambda: self.exit)
        label.pack(side=tk.TOP, pady=10)
        description.pack(side=tk.TOP, pady=10)

        button.pack(side=tk.TOP, fill=tk.X, padx=20) 
        button2.pack(side=tk.TOP, fill=tk.X, padx=20)
        button3.pack(side=tk.TOP, fill=tk.X, padx=20)
        buttonout.pack(side=tk.TOP, fill=tk.X, padx=20, pady=10)

    def togame(self, mode, json_data, json_error):
        word = random.choice(json_data[mode])            
        self.root.destroy()
        self.game = tk.Tk()
        app = Game(self.game, word, mode, json_error)
        self.game.mainloop()
    def exit(self):
        self.root.destroy()