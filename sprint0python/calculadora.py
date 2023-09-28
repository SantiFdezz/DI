from operaciones import suma, resta,div,multip 

class calculadora ():
    while True:
        num1 = int(input("Primer número: "))
        num2 = int(input("Segundo número: "))
        print('\nOperaciones: ')
        print(' - 1.Suma.')
        print(' - 2.Resta.')
        print(' - 3.División.')
        print(' - 4.Multiplicación.')
        op = int(input('\n-----> ¿Qué operación quieres realizar? '))
        while (op != 1) and (op!= 2) and (op != 3) and (op != 4):
            print("OPCIÓN NO VÁLIDA!")
            op = int(input('\n----> ¿Qué operación quieres realizar? '))
        if op == 1:
            total = suma(num1,num2)
            print ("\nLa suma de {} + {} = {}".format(num1,num2,total))
        elif op == 2:
            total = resta(num1,num2)
            print ("\nLa resta de {} + {} = {}".format(num1,num2,total))
        elif op == 3:
            total = div(num1,num2)
            print ("\nLa división de {} + {} = {}".format(num1,num2,total))
        elif op == 4:
            total = multip(num1,num2)
            print ("\nLa multiplicación de {} + {} = {}".format(num1,num2,total))

        opc = input('\n-----> ¿Desea realizar otra operación (s/n)? ')
        while (opc != 's' and opc != 'n'):
            print("[!]Carácter Inválido")
            opc = input('\n-----> ¿Desea realizar otra operación (s/n)? ')
        if opc == 's':
            True
        else:
            break
