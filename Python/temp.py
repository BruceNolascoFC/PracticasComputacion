# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal
"""

###comentarios###

from math import *

print "Este programa realiza la suma de enteros consecutivos desde 1 hasta:"

num = int(raw_input("Digita el entero deseado: "))

print "El numero que recibi es: ",num
print "El tipo de variable es: ",type(num)

i = 0
sum = 0
while (i<=num):
    sum = sum +i
    i = i + 1
    print "Suma: ",sum
    #print "El valor de i es ",i-1

print "El resultado final es: ",sum
print "La suma consecutiva de ",num,"es:",sum