import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from io import BytesIO
import requests


class Game:
    def __init__(self, game, word, mode, json_error, root):
        self.game = game
        self.root = root
        self.game.title("Dificultad: "+mode)
        x = (self.game.winfo_screenwidth() - self.game.winfo_reqwidth()) / 2 ##screenwidth devuelve el ancho de la pantalla,  y reqwidth nos devuelve la anchura en pixels de la ventana.
        y = (self.game.winfo_screenheight() - self.game.winfo_reqheight()) / 2
        self.game.geometry(f"+{int(x)}+{int(y)}") # Esto crea el tamaño por defecto de la ventana y lo centra
        self.game.geometry("300x200")
        self.root.resizable(False,False)
        self.word = word
        self.wordT = self.makePass()
        self.error = 0
        self.errorLet=[]
        self
        self.lettcorrect = ""
        self.letterror = ""
        self.let = ''
        self.json_error = json_error
        self.showInterface()


    def showInterface(self):
        self.labelimag = ttk.Label(self.game) #inicializamos el label sin nada dentro, (en callImage se le actualza)
        self.labelimag.grid(row=0, column=0, pady=10)
        self.callImage()
        labelword = ttk.Label(self.game, text=self.wordT)
        labelword.grid(row=1, column=0, pady=10) #mostramos la palabra con guiones debajo de la imagen
        labelerror = ttk.Label(self.game, text="Errores: "+str(self.error)) 
        labelerror.grid(row=0, column=1, pady=10) #mostramos los errores

        labelerror = ttk.Label(self.game, text="Intentos: "+ self.letterror)
        labelerror.grid(row=1, column=1, pady=10) # mostramos las letras erradas probadas

        E1 = ttk.Entry(self.game, width=10) # width manda el ancho de el campo
        E1.grid(row=2, column=1, pady=10, padx=10)
        applybutton = ttk.Button(self.game, text="Adivinar", command= lambda: self.checkLet(E1.get()))
        applybutton.grid(row=2, column=2, pady=10)
        if self.wordT != self.word.lower() and self.error == 6:
            messagebox.showinfo("¡Perdiste!", "¡Lo siento, has perdido la palabra era: "+self.word+"!")
            self.exit()
        elif self.wordT == self.word.lower() and self.error < 6:
            messagebox.showinfo("¡Ganaste!", "¡Felicidades, has adivinado la palabra era: "+self.word+"!")
            self.exit()

    def makePass(self):
        wordT = ""
        for i in range(len(self.word)):
                wordT+='-' #por cada letra de self.word añade a wordT un -
        return wordT
    
    def callImage(self):
        image_url = self.json_error[self.error]['image']#cogemos la imagen segun el numero de errores(están en lista)
        response = requests.get(image_url)
        image = Image.open(BytesIO(response.content))
        image = image.resize((100, 100), Image.Resampling.LANCZOS)#redimensionamos la imagen para que ocupe 100x100px
        self.image = ImageTk.PhotoImage(image)
        self.labelimag.configure(image=self.image) #añadimos al label la imagen correspondiente

    def checkLet(self, let):
        if let == '' or len(let) > 1:
            messagebox.showinfo("CÁRACTER INVALIDO", "SOLO SE PUEDE 1 CARÁCTER.")
            self.showInterface() #enviamos mensaje de error y lo mandamos de vuelta a enviar carácter
        else:
            self.let = let.lower().strip() # ponemos la letra en minuscula y quitamos los espacios
            self.processLetter()

    def processLetter(self):
        if self.let in self.word.lower():
            for z in range(len(self.word.lower())):
                if self.let == self.word[z].lower():
                    self.wordT = self.wordT[:z] + self.let + self.wordT[z + 1:] #rellenamos la palabra secreta cambiando solo la letra cambiada en el string
        else:
            self.error+=1
            self.errorLet.append(self.let)
            for i in self.errorLet:
                if i == self.let:
                    self.letterror = ", ".join(self.errorLet) #igualamos en string separado por comas las letras falladas de el array

        self.showInterface()
        
    def exit(self):
        self.root.deiconify()
        self.game.destroy()
