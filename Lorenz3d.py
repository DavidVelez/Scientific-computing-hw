#Fecha de creacion: 7 de marzo,2016
#Tema: Atractor de Lorenz
#Objetivo: construir una grafica 3D del Atractor de Lorenz.
#Estrategia: t = al tiempo, x = la conveccion del aire, y = el flujo de aire que sube y baja, z = desviacion de la temperatura.
#Autor: David Velez

import numpy
import matplotlib
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111,projection= '3d')

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

ax.scatter(x,y,z)
ax.set_xlabel( ' (x) Conveccion Aire')
ax.set_ylabel( ' (y) Movimiento Aire')
ax.set_zlabel( ' (z) Desviacion Temperatura')
plt.show()
