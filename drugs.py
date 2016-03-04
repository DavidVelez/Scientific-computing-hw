#Febrero 25 de 2016
#Tema: La grafica muestra la concentracion de acetil-salicilico en un tiempo de 10 horas, tal que Q se muestra en ug/mL y t en horas.
#Objetivo: hallar las ecuaciones pertinentes, determinar las posibles variaciones de decrecimiento de la droga en el organismo.
#Autor: David Velez.

import numpy
import matplotlib
import matplotlib.pyplot


delta = 0.1
k = 0.2
t = range(101)
Q = range(101)
Q0 = 200
for i in range(101):
         Q1 = Q0-delta*k*Q0
         Q0=Q1    
         Q[i] = Q1
print Q
Qnew=numpy.array(Q)
tnew=numpy.array(t)
print Qnew
print tnew

matplotlib.pyplot.plot(tnew,Qnew)
matplotlib.pyplot.show()
