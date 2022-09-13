#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Claudia Santivañez
#
# Created:     12/09/2022
# Copyright:   (c) Claudia Santivañez 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
#ejercicio 1
    papa  =  1
    cebolla  =  2
    suma  =  papa  +  cebolla
    print ( suma )
#ejercicio 2
    nombre = "claudia cecilia "
    apellido = "santivañez aparicio"
    print (nombre + apellido)
#ejercicio 3
    nombre = input("Ingrese su nombre ")
    dni = input("Ingrese su dni ")
    print(f'El nombre del usuario es {nombre}')
    print(f'El DNI del usuario es {dni}')
if __name__ == '__main__':
    main()
