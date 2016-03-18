#ALGOTIRMO RSA
#Creado por:
#David Felipe Velez Cadavid
#Estudiante Computacion Cientifica
#Universidad de Medellin


#PROBLEMA NUMERO DOS

#Escriba una funcion que dada la clave publica y un mensaje compuesto de cuatro digitos desencripte el mensaje formado 
#por estos cuatro numeros
import random

#se crea una funcion para definir si un numero es primo
def prime_num(num):
                   
	
    for i in range(2, num):  
	if num % i == 0:    
	 return 0
    return 1


#creo una funcion que me desencriptara el mensaje cifrado
#en esta funcion se procesan e, N y los cuatro numeros daos por el usuario.
def hackrsa (e, N, n1, n2, n3, n4):
		
	for p in range(2,N):#basicamente lo que hacemos es buscar en un rango de 2 a N-1 un p que sea primo
		for q in range(2,N):#De igual forma hacemos en este rango
			if primo(p)==1 and primo(q)==1 and p*q == N:#si p y q me cumplen estas condiciones podemos hallar N.

		for d in range(phi*2):#
			  if e * d % phi == 1:
				d
				m1 = n1**d%N
				m2 = n2**d%N
				m3 = n3**d%N
				m4 = n4**d%N
				return n1, n2, n3, n4


			


e=(input ("Por favor ingrese el valor de (e) de la LLave publica generada: " ))
N=(input ("Por favor ingrese el valor de (N) de la LLave publica generada: "))




m1=(input ("Ingrese el primer digito a desencriptar: ")) 
m2=(input ("Ingrese el segundo digito a desencriptar: "))
m3=(input ("Ingrese el tercer digito a desencriptar: "))
m4=(input ("Ingrese el cuarto digito a desencriptar: "))


finAl=hackrsa (e, N, m1, m2, m3, m4)
print finAl








