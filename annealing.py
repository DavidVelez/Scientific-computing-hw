#encoding: utf-8
#Optimizacion de costos-Annealing


import numpy as np
from random import random
import matplotlib.pyplot as plt


#funcion costo
def cost(x): 
	fc = np.exp(-(x-1)**2) * np.sin(8*x) + 1
	return fc

#rango de refugio de mejor solucion
plt.xlabel('solution')
plt.ylabel('cost')
plt.title('Annealing')
t = np.linspace(-3, 3, num =100)
plt.plot(t,cost(t), 'b', linewidth = 2)

#funcion posible solucion
def neighbor(s):
	fs=(2 * random() -1) * 1 + s
	return fs

#funcion busqueda apartir de minimo local
def aceptance(oc,nc,T):
	fp = np.exp((oc-nc) / T)
	return fp

#funcion solucion "final"
def anneal(x):
	oc = cost(x)
	T = 1.0
	T_min = 0.00001
	alpha = 0.99
	while T > T_min:
		i = 1
		while i <= 100:

			ns = neighbor(x)
			nc = cost(ns)
			ap= aceptance(oc, nc, T)
			if ap > random():
				x = ns
				oc = nc
			i += 1
		T= T * alpha	
	return x, oc
		
x, c= anneal(2.1)

print x, c
plt.plot([x], [c], 'ro')
plt.show()
