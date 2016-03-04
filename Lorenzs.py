#Thursday, 3 March 2016
#Tema: simulacion del modelo de Lorenzs 
#Objetivo: aplicar las ecuaciones e informacion dada, de manera correcta para llegar a la modelacion del tambien llamado "Caos" utilizado en sistemas fisicos, graficando x en funcion de z.
#Autor: David Felipe Velez Cadavid

import numpy
import matplotlib
import matplotlib.pyplot

delta=0.01
x0=0
y0=1
beta=2.2667
rho=28
sigma=10
z0=1.05

x=range(10001)
y=range(10001)
z=range(10001)
t=range(10001)

for i in range(10001):

    x1=delta*sigma*y0-delta*sigma*x0+x0
    x0=x1
    y1=delta*x0*rho-delta*x0*z0-delta*y0+y0
    y0=y1
    z1=delta*x0*y0-delta*beta*z0+z0
    z0=z1
    x[i]=x1
    y[i]=y1
    z[i]=z1
    t[i]=i*0.01

xnew=numpy.array(x)
ynew=numpy.array(y)
znew=numpy.array(z)
tnew=numpy.array(t)

print xnew
print ynew
print znew
print tnew

matplotlib.pyplot.plot(xnew,znew)
matplotlib.pyplot.show()

