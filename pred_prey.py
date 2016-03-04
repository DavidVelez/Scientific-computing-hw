#Marzo 1, 2016
#Tema: implementacion del modelo de Lokta Volterra en el crecimiento y decrecimiento de plobacion en relacion presa y depredador.
#Objetivo: determinar el modelo de interraccion de dos especies en relacion al crecimiento y decrecimiento de poblacion, 
#con (x) depredador y (y) presa.
#Autor: David Velez.

import numpy
import matplotlib
import matplotlib.pyplot

delta = 0.1
X0=15
Y0=100
Ky = 2.0
Kyx = 0.01
Kx = 1.06
Kxy = 0.01
t=range(101)
y=range (101)
x=range (101)
y[0]=Y0
x[0]=X0
for i in range (1,101):
	Y1=delta*Ky*Y0-delta*Kxy*X0*Y0+Y0
	Y0=Y1
	X1=delta*Kyx*Y0*X0-delta*Kx*X0+X0
	X0=X1
	y[i]=Y1
	x[i]=X1
	t[i]=i*delta

ynew=numpy.array(y)
xnew=numpy.array (x)
tnew=numpy.array (t)

print ynew
print xnew
print tnew

matplotlib.pyplot.plot(tnew,ynew)
matplotlib.pyplot.plot(tnew,xnew)
matplotlib.pyplot.show()

matplotlib.pyplot.plot (ynew,xnew)
matplotlib.pyplot.plot (xnew,ynew)
matplotlib.pyplot.show()
