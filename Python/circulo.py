# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 15:49:40 2017

@author: BruceNolasco
"""
#Se importa la constante pi y la función raiz cuadrada del modulo math
from math import pi
from math import sqrt
#SE le presenta al usuario las instrucciones y el menu de opciones
print "Bienvenido a la Calculadora de Diametro, Perimetro o Area."
#Variable para idenificar la validez de la opcion
#(0 es invalida y por defecto, 1 es valida)
valid = 0
while valid == 0:
    print "Por favor seleccione el dato que desea ingresar (en cm.):"
    print "1. Diametro"
    print "2. Perimetro"
    print "3. Area"
    print "4. Salir"
    #Se utiliza raw_input para ller la opcion deseada y se convierte a entero
    selection = int(raw_input());
    
    #Rutina para calcular perimetro y area dado el diametro
    if selection == 1:
        #Se marca como valida la seleccion
        valid = 1
        #Se solicita el valior del diametro
        diametro= float(raw_input("Diametro:"))
        #Calculo de perimetro y area
        perimetro = pi*diametro
        area = pi*((diametro/2.)**2)
    else:
        #Rutina para calcular area y diametro dado el perimetro
        if selection == 2:
            #Se marca como valida la seleccion
            valid = 1
            perimetro= float(raw_input("Perimetro:"))
            diametro = perimetro/pi
            area = pi*((diametro/2.)**2)
        else:
        #Rutina para calcular diametro y perimetro dado el area
            if selection == 3:
                #Se marca como valida la seleccion
                valid = 1            
                area= float(raw_input("Area:"))
                diametro = 2*sqrt(area/pi)
                perimetro = pi*diametro
            #Si no se cumple ninguna de las condiciones previas la seleccion es invalida
            else:
                if selection == 4:
                    valid = 2
                else:
                    print "Seleccion invalida. Por favor vuelve a seleccionar una opcion:"
#SE imprimen los valores calculados si la seleccion es valida 
if valid ==1:
    print "El diametro es ",diametro,"cm."
    print "El perimetro es ",perimetro,"cm."
    print "El area es ",area,"cm2."