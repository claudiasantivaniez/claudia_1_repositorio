#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Claudia Santivañez
#
# Created:     15/09/2022
# Copyright:   (c) Claudia Santivañez 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
#ejercicio 2
#Pedir al usuario que ingrese dos nros
#Luego imprimir 3 opciones (1. sumar, 2. restar y 3. multiplicar)
#Pedir al usuario que ingrese una opción
#Verificar la opción del usuario
#Mientras que el usuario no ingrese una opción correcta se volverá a pedir que
#ingrese una opción
#Ejecutar la operación
#Mostrar por pantalla el resultado

    a = int(input("ingrese un numero "))
    b = int(input("ingrese un numero "))
   # print ("1 sumar, 2 restar, 3 multiplicar")
    operacion = int(input("ingrese una opcion: 1 sumar, 2 restar, 3 multiplicar "))
    while operacion < 1 or operacion > 3:
        operacion = int(input("ingrese una opcion valida: 1 sumar, 2 restar, 3 multiplicar "))
    if (operacion==1):
        op=(a+b)
    elif (operacion==2):
        op=(a-b)
    else:
        op=(a*b)
    print(f'El resultado es: {op}')

if __name__ == '__main__':
    main()
