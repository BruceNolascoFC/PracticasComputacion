# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 16:15:33 2017

@author: Bruce Nolasco
"""
from math import pi
numero = float(raw_input("Dame un numero: "))

print "%d elevado a %d es %d"%(numero,2,numero**2)
print "%d elevado a %d es %d"%(numero,3,numero**3)
print "%d elevado a %d es %d"%(numero,4,numero**4)
print "%d elevado a %d es %d"%(numero,5,numero**5)

numero_pi = pi*numero

print "El valor de %f pi es %f"%(numero,numero_pi)
print "El valor de %6.3f pi es %6.3f" % (numero, numero_pi)