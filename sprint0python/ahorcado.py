import random
from random import choice
win = True
while win:
    mode = ''
    print('---------------------------------\n\tAHORCADO\n---------------------------------\n')
    print('\n\n[-] Elige tu nivel de juego:\n\t[1] Dificultad Facil (3-5 letter)\n\t[2] Dificultad Normal (6-9 letter) \n\t[3] Dificultad Dificil (+9 letter)\n')
    
    diff = int(input('Introduce número de dificultad (1/2/3): '))
    
    while diff < 1 or diff > 3:
        print('[!] SOLO SE PUEDE ELEGIR 1, 2 o 3 PARA LA DIFICULTAD.')
        diff = int(input('Introduce número de dificultad (1/2/3): '))

    if diff == 1:
        mode = 'easy'
    elif diff == 2:
        mode = 'normal'
    elif diff == 3:
        mode = 'hard'

    with open("palabras.txt", "r") as r:
        lines = r.read().splitlines()
        valid_words = []

        for i in range(len(lines)):
            if lines[i] == mode:
                valid_words.extend(lines[i+1:i+4])
        if valid_words:
            word = random.choice(valid_words)
    error = 0
    triedlett=[] 
    wordT = ''
    for i in range(len(word)):
        wordT=wordT+'_'
    print('-------------------------------------->  '+wordT)
    while error < 6 and wordT!=word:
        aux = ''
        lett= input('Introduce letra: ').lower()
        while len(lett) != 1:
            print('[!] SOLO SE PUEDE 1 CARACTER.')
            lett= input('Introduce letra: ').lower()

        if lett in word:
            for z in range(len(word)):
                if lett == word[z]:
                    wordT = wordT[:z] + lett + wordT[z + 1:]

        else:
            error+=1
            triedlett.append(lett)

        print('-------------------------------------->  '+wordT)
        print('Errores totales:'+str(error))
        print('Lista de letras erradas: '+', '.join(triedlett))
    if error >=6:
        print('Has perdido. La palabra era ' + word)
    elif error < 6 and wordT == word:
        print('¡Felicidades, has adivinado la palabra: ' + word + '!')

    if input('Quieres volver a jugar? (s/n) ') == 's':
        win = True
    else:
        win = False