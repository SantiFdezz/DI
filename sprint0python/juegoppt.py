import random


ppt_dic=[
    {
        'name' : 'papel',
        'breaks' : 'tijera'
    },
    {
        'name' : 'piedra',
        'breaks' : 'papel'
    },
    {
        'name' : 'tijera',
        'breaks' : 'piedra'
    }
]
print('\t\tPIEDRA PAPEL TIJERA\n\t\t-------------------')
print('\nEl juego consiste en dictar piedra, papel o tijera pudiendo suponer lo que va a hacer el otro para ganarle a un total de 5 partidas.')

p1 = 0
p2 = 0
for i in range(6):
    opt=input('\nElige (piedra/papel/tijera): ').lower()
    while opt not in ['piedra','tijera','papel']:
        print('[!] OPCIÓN NO VÁLIDA')
        opt=input('Elige (piedra/papel/tijera): ').lower()
    opt2 = random.choice(['piedra', 'papel', 'tijera'])
    print("El ordenador ha elegido: "+opt2)

    for j in ppt_dic:
        if opt == j['name']:
            break
    
    for z in ppt_dic:
        if opt2 == z['name']:
            break

    if j['breaks'] == z['name']:
        p2+=1
        print('\nHa  ganado 1 punto el player 2, '+z['name']+' gana a '+j['name'])
    elif z['breaks'] == j['name']:
        p1+=1
        print('\nHa  ganado 1 punto el player 1, '+j['name']+' gana a '+z['name'])
    else:
        print('\nHabeis empatado')
        i-=1
print('\nPuntaje final: Jugador 1:', p1, 'Jugador 2:', p2)




