list_dic=[
        {
                'key': 'Son doce señoras con medias, pero sin zapatos. ¿De quiénes se trata?',
                'answ': ['A) El viento', 'B) El mapa', 'C) Las horas del un reloj'],
                'correct': 'C'
        },
        {
                'key': 'Puede silbar sin labios y correr sin pies. Además, te pega en la espalda sin que lo puedas ver.',
                'answ': ['A) El viento', 'B) El mapa', 'C) Las horas del un reloj'],
                'correct': 'A'
        },
        {
                'key': '¿Dónde hay ríos sin agua, ciudades sin casas y bosques sin árboles?',
                'answ': ['A) El viento', 'B) El mapa', 'C) Las horas del un reloj'],
                'correct': 'B'
        }
]
i = 0
score = 0
for clave in list_dic:
        clave = list_dic[i]['key']
        respuestas = list_dic[i]['answ']
        correcta = list_dic[i]['correct']
        print("Adivinanza: {} \nRESPUESTAS: {}".format(clave, respuestas))
        opcion = input('Tu respuesta es: ').upper()
        
        while (opcion != 'A') & (opcion != 'B') & (opcion != 'C'):
                print("Tu respuesta. Debe ser A, B o C")
                opcion = input('Tu respuesta es: ').upper()
        
        if opcion == list_dic[i]['correct'] :
                score+=10
        else:
                score-=5
        i+=1

print("La puntuación total es de: {}".format(score))