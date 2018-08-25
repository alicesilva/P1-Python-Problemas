#coding: utf-8
#Aluna: Alice Fernandes Silva / Programação 1, 2015
#questão: remove menores de uma lista

def remove_menores(N, lista):
	cont = 0
	for i in range(len(lista)-1,-1,-1):
		if N > lista[i]:
			del lista[i]
			cont += 1
	
	return cont
