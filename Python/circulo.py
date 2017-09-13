# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 15:49:40 2017

@author: BruceNolasco
"""
"""
1) Preguntar un numero al usuario
    a. Escribe la pregunta
    b. Capturar la entrada del usuario
    c. Convertir entrada en numero
    d. Asignar a una variable x
2) Preguntar acción a realizar
    a. Asignar una variable y la opcion a ejecutar.
3) Ejecutar la accion
4) Salir 

"""

#Se importa la constante pi y la función raiz cuadrada del modulo math
from math import pi
from math import sqrt
#SE le presenta al usuario las instrucciones y el menu de opciones
print "Bienvenido a la Calculadora de Diametro, Perimetro o Area."
radio = float(raw_input("Ingrese el radio en cm. : \n"))
#Variable para idenificar la validez de la opcion
#(0 es invalida y por defecto, 1 es valida)
valid = 0
while valid == 0:
    print "Por favor seleccione el dato que desea calcular:"
    print "1. Diametro"
    print "2. Perimetro"
    print "3. Area"
    print "4. Salir"
    #Se utiliza raw_input para leer la opcion deseada y se convierte a entero
    selection = int(raw_input());
    
    #Rutina para calcular perimetro y area dado el diametro
    if selection == 1:
        #Se marca como valida la seleccion
        valid = 1
        dato = "diametro"        
        #Calculo de perimetro y area
        dpa = 2*radio
        
        
    else:
        #Rutina para calcular area y diametro dado el perimetro
        if selection == 2:
            #Se marca como valida la seleccion
            valid = 1
            dato = "perimetro"
            dpa = pi*2*radio 
        else:
        #Rutina para calcular diametro y perimetro dado el area
            if selection == 3:
                #Se marca como valida la seleccion
                valid = 1            
                dato = "area"
                dpa = pi*(radio**2)
            #Si no se cumple ninguna de las condiciones previas la seleccion es invalida
            else:
                if selection == 4:
                    valid = 2
                else:
                    print "Seleccion invalida. Por favor vuelve a seleccionar una opcion:"
#SE imprimen los valores calculados si la seleccion es valida 
if valid ==1:
    print "El %s de un circulo de radio %.2f cm. es %.2f cm."%(dato,radio, dpa)
print "Adios"