import tkinter as tk
from window import MainWindow 
from loading import Loading 

if __name__ == "__main__":
    root = tk.Tk()
    app = Loading(root)
    root.mainloop()