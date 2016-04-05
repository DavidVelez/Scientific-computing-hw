#4 de abril de 2016
#Simulacion del modelo de Hodgkin-Huxley
#Bases: definir varias funciones y un rango con la idea de unirlas reemplazando valores en una ultima funcion principal.
#AutorDavid Velez.



import numpy as np
import matplotlib.pyplot as plt


delta=0.001
CM=1
I=15

Vk=-12
VNa=115
VL=10.599
gK=36
gNa=120
gL=0.3

T=6.3



def phi(T): 
	return 3**((T-6.3)/10)



def an(V):
	return phi(T)*(0.01*(10-V)/(np.exp((10-V)/10)-1))
	
def Bn(V):
	return phi(T)*(0.125 *np.exp(-V/80))


def am(V):
	return phi(T)*(0.01*(25-V)/(np.exp((25-V)/10)-1))
	
def Bm(V):
	return phi(T)*4*np.exp(-V/18)

	
def ah(V):
	return phi(T)*0.07*np.exp(-V/20)

def Bh(V):
	return phi(T)*1/(np.exp((30-V)/10)+1)

def IK(V,n): return gK*n**4*(V-Vk)

def IL(V): return gL*(V-VL)
def INa(V, m, h): return gNa*m**3*h*(V-VNa)




t = np.linspace(0, 5, num =20000, endpoint=True)
n = np.zeros(len(t))
m = np.zeros(len(t))
h = np.zeros(len(t))
V = np.zeros(len(t))

V[0]=-65
n[0]=0.317
m[0]=0.05
h[0]=0.6

for i in range(len(t)-1):

   Vdt, ndt, mdt, hdt = fp(V[i], n[i], m[i], h[i])

   Vdtt, ndtt, mdtt, hdtt = fp(V[i] + (0.5*delta*Vdt), n[i] + (0.5*delta*ndt), m[i] + (0.5*delta*mdt), h[i] + (0.5*delta*hdt))
   V[i+1] = V[i] + (delta*Vdtt)	
   n[i+1] = n[i] + (delta*ndtt)
   m[i+1] = m[i] + (delta*mdtt)
   h[i+1] = h[i] + (delta*hdtt)

										
plt.plot(t, m, 'r', label='m')
plt.plot(t, h, 'g', label='h')
plt.plot(t, n, 'b', label='n')
plt.legend()
plt.show()

plt.plot(V,n)
plt.title('')
plt.show()

plt.plot(t,V)
plt.xlabel('vs')
plt.ylabel('V(t)')
plt.show()
