from tkinter import ttk
import tkinter as tk
from PIL import ImageTk, Image
from cell import Cell

class DetailWindow:
    def __init__(self, root, image_tk, title, description):
        self.root = root
        self.title = title
        self.image_tk = image_tk
        self.description = description
        self.detail_root = tk.Tk()
        self.detail_root.title(self.title)

        frame = ttk.Frame(self.detail_root)
        frame.pack()
        label = ttk.Label(frame, image=self.image_tk, text=self.title, compound= tk.BOTTOM)
        label.pack(side="top")

        desc_label = ttk.Label(frame, text=self.description)
        desc_label.pack(side="bottom")

    def showDetail(title, image_tk, description):

        detail_window = DetailWindow(title, image_tk, description)
        detail_window.detail_root.mainloop()

