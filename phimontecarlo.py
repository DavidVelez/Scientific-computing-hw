from random import random
from math import sqrt

def phi(t):
    """Calcula y devuelve el valor aproximado
    de pi usando el metodo de Montecarlo a
    partir de t puntos.
    """
    c=0.0

    for i in range(t):
     
        x = random()
	
        y = random()
	
        d =  sqrt(x ** 2 + y ** 2)
	
        if d < 1.0:
            c += 1.0
	
    return (c / t)*4
print phi(1000)




