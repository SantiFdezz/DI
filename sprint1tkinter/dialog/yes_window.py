import tkinter as tk
from tkinter import ttk

def show_yes_window():
    yes_root = tk.Tk()
    yes_root.title("Yes Window")

    label = ttk.Label(yes_root, text="¡Sí!")
    label.pack(pady=10)

    yes_root.mainloop()
