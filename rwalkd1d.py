#modelacion del modelo rwalk1d. 
#12 de Abril de 2016
#Autor: David Velez

import numpy as np

#N=input('ingrese el valor de veces que quiere lanzar la moneda:')
N = 100

def rwalk1d(N,c):

	
	p=0
	for i in range (N):
		
		x=np.random.random()

		if x>c:
			p=p+1

		else:
			p=p-1

	return p
print 'la posicion final despues de', N ,'iteracciones es:',rwalk1d(N,0.5)

# for <variable> in <list>:


