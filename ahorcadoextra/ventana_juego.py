import tkinter as tk
from tkinter import ttk, messagebox, Image
from io import BytesIO
import requests


class Game:
    def __init__(self, game, word, mode, json_error):
        self.game = game
        self.game.title("Nivel "+mode)
        self.game.geometry("300x300")
        finish = False
        while not finish:
            wordT = ""
            wordT = self.makePass(word, wordT)
            error = 0
            triedlett=[]
            letterror = ""
            lettcorrect = ""
            while error < 6 and wordT!=word:
                self.image = self.game.after(100, self.callimage(error))
                labelimag = ttk.Label(self.game, image=self.image)
                labelimag.grid(row=0, column=0)
                labelword = ttk.Label(self.game, text=wordT)
                labelword.grid(row=1, column=0)
                labelacierto = ttk.Label(self.game, text="Aciertos: "+lettcorrect)
                labelacierto.grid(row=1, column=1)
                labelerror = ttk.Label(self.game, text="Errores: "+str(error))
                labelerror.grid(row=2, column=1)
                labelerror = ttk.Label(self.game, text="Letras erróneas: "+ letterror)
                labelerror.grid(row=3, column=1)
                E1 = ttk.Entry(self.game)
                E1.grid(row=4, column=1)
                let = ((E1.get()).lower())
                while let == '' or len(let) > 1:
                    messagebox.showinfo("Error", "SOLO SE PUEDE 1 CARACTER.")
                    let = ((E1.get()).lower())
                if let in word:
                    for z in range(len(word)):
                        if let == word[z]:
                            wordT = wordT[:z] + let + wordT[z + 1:] #rellenamos la palabra secreta cambiando solo la letra cambiada en el string
                            lettcorrect += let+", "
                else:
                    error+=1
                    triedlett.append(let)
                    for i in triedlett.size():
                        letterror += triedlett.index(i)+", "
    
    def makePass(self, word, wordT):
        for i in range(len(word)):
                wordT+='-'
        return wordT
    def callimage(error, json_error):
        response = requests.get(json_error[image].get(error))
        ##image = Image.open(BytesIO(response.content))
        image = (Image.open(BytesIO(response.content))).resize((100, 100), Image.Resampling.LANCZOS)
        return image
