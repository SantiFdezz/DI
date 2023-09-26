respuestas_dic={
    'A': 'EL VIENTO',
    'B': 'LAS HORAS DE UN RELOJ',
    'C': 'EL MAPA'
}
print("Son doce señoras con medias, pero sin zapatos. ¿De quiénes se trata?")
for clave in respuestas_dic :
        respuesta = respuestas_dic.get(clave)
        print("La respuesta {} es {}".format(clave, respuesta))

opcion = input('Tu respuesta es: ')
opM = opcion.upper()
while (opM != 'A') & (opM != 'B') & (opM != 'C'):
        print("Tu respuesta. Debe ser A, B o C")
        opcion = input('Tu respuesta es: ')
        opM = opcion.upper()
if opM == 'A' or opM == 'C':
        print ("Respuesta Fallida.")
else:
        print ("Acertaste!!.")

