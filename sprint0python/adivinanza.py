import random
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
adiv1=random.sample(list_dic, 1)[0]['key']
adiv2=random.sample(list_dic, 1)[0]['key']
while adiv1 == adiv2:
        adiv2=random.sample(list_dic, 1)[0]['key']

for j in list_dic:
        if adiv1 == j['key']:
                break
for z in list_dic:
        if adiv2 == z['key']:
                break
for i in range(2):
        if i == 0:
                x = j
        else:
                x = z
        print("Adivinanza{}: {} \nRESPUESTAS: {}".format(i+1,x['key'],x['answ'] ))
        option = input('Tu respuesta es: ').upper()

        while (option != 'A') & (option != 'B') & (option != 'C'):
                print("Tu respuesta. Debe ser A, B o C")
                option = input('Tu respuesta es: ').upper()

        if option == x['correct'] :
                score+=10
        else:
                score-=5

print("La puntuación total es de: {}".format(score))