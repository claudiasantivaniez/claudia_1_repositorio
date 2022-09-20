#-------------------------------------------------------------------------------
# Name:        clase2_ejercicio1
# Purpose:
#
# Author:      Claudia Santivañez
#
# Created:     15/09/2022
# Copyright:   (c) Claudia Santivañez 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():

#Ejercicio 1.
#Pedir al usuario que ingrese un nro impar
#Mientras que el usuario no ingrese un nro impar se volverá a pedir que ingrese
#un nro impar
#deberá indicar por pantalla si es impar

        num = int(input("Ingrese un número: "))
        while(num % 2 == 0):
            print("Ingrese un numero impar")
            num = int(input("Ingrese un número: "))
        print(f'El numero impar es: {num}')


if __name__ == '__main__':
    main()

