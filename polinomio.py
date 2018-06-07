# coding: utf-8
# Aluna: Alice Fernandes Silva / Programação 1, 2015
# Polinomio

def valor_polinomio(polinomio, valor):
	valor_polinomio = polinomio[0]
	for i in range(1,len(polinomio)):
		valor_polinomio += polinomio[i] * valor ** i
	
	return valor_polinomio		
		
		
