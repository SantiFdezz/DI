from tkinter import Tk, ttk
import tkinter as tk
from yes_window import show_yes_window
from no_window import show_no_window

class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Main Window")
        self.frame = ttk.Frame(self.root)
        self.frame.pack()

        self.label = ttk.Label(self.frame, text="SI o NO")
        self.label.pack()

        self.button = ttk.Button(self.frame, text="SI", command=show_yes_window)
        self.button.pack(side = "left")
        self.button = ttk.Button(self.frame, text="NO", command=show_no_window)

        self.button.pack(side = "right")
