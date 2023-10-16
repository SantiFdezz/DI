from tkinter import Tk
from window import MainWindow 
from loading import Loading 

if __name__ == "__main__":
    root = Tk()
    app = Loading(root)
    root.mainloop() 