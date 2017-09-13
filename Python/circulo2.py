# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 16:01:36 2017

@author: Bruce Nolasco
"""
from math import pi
a= True
while a:
    x = raw_input("Escribe un numero:")
    try:
        x = float(x)
    except ValueError:
        print "Tu entrada no es numerica"
        
    print "Escriba una se las siguientes opciones: "
    print "1) Diametro"
    print "2) Perimetro"
    print "3) Area"
    print "4) Salir"

    y= raw_input("¿Que quieres hacer? ")
    try:
        y = int(y)
    except ValueError:
        print "No escogiste una opcion valida."
    
    if y==1:
        d= 2*x
        print "El diametro es ",d
    elif y == 2:
        d = 2*pi*x
        print "El perimetro es ",d
    elif y == 3:
        d = pi*(x**2)
        print "El area es ",d
    elif y == 4:
        a = False
print "Bye"