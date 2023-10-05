import tkinter as tk
from tkinter import ttk

def show_no_window():
    no_root = tk.Tk()
    no_root.title("No Window")

    label = ttk.Label(no_root, text="No!")
    label.pack(pady=10)

    no_root.mainloop()