# coding: utf-8
# Aluna: Alice Fernandes Silva / Programação 1, 2015
# Encontra menores

def encontra_menores(num, lista):
	cont = 0
	for i in range(len(lista)):
		if lista[i] < num:
			return lista[i]
			break
		if lista[i] >= num:
			cont += 1
	
	if cont == len(lista):
		return -1



	
