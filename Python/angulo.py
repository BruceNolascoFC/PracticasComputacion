# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 15:50:19 2017

@author: Bruce Nolasco
"""

from math import sin,cos  #Se importan las funciones seno y coseno
#Se registra el texto introducido por el usuario en consola
texto_leido= raw_input("Escribe el valor de un angulo para calcular seno y coseno (Radianes): ")
#Imprimir le tipo de variable ingresada
print "El tipo de variable recibida es: ",type(texto_leido)
#Transformo la variable a tipo flotante
angulo = float(texto_leido)
#Imprimo el tipo de variable de angulo
print "La variable se transformo al tipo ",type(angulo)
#Uso angulo para calcular el seno y el coseno
seno = sin(angulo)
coseno = cos(angulo)
#Imprimo los valores de seno y coseno
print seno,coseno
#Imprimo separadamente el valor de coseno y seno
print "El coseno de ",angulo," es ",coseno
print "El seno de ",angulo," es ", seno