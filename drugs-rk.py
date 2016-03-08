#Fecha de creacion: Marzo 8, 2016
#Tema: Decrecimiento de aspirina en el organismo.
#Objetivo: Aplicar la ecuacion llamada Runge-Kutta.
#Estrategia: aplicar la ecuacion diferencial de primer orden de Runge-Kutta, definiendo una sola funcion la solucion del problema.
#Autor: David Velez

import numpy
import matplotlib
import matplotlib.pyplot


delta = 0.1
k = 0.2
t = range(101)
Q = range(101)
Q0 = 200


def f(n):
	return -k * n
for i in range(101):
	Q1=Q0+delta*f(Q0+0.5*delta*f(Q0))
        Q0=Q1
	Q[i]=Q1*delta
		

print Q1
Qnew=numpy.array(Q)
tnew=numpy.array(t)
print Qnew
print tnew

matplotlib.pyplot.plot(tnew,Qnew)
matplotlib.pyplot.show()
         



