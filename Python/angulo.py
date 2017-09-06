# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 15:50:19 2017

@author: est5
"""

from math import sin,cos
texto_leido= raw_input("Escribe el valor de un angulo para calcular seno y coseno (Radianes): ")
print "El tipo de variable recibida es: ",type(texto_leido)
angulo = float(texto_leido)
print "La variable se transformo al tipo ",type(angulo)
seno = sin(angulo)
coseno = cos(angulo)
print "El coseno de ",angulo," es ",coseno
print "El seno de ",angulo," es ", seno