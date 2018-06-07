# coding: utf-8
# Aluna: Alice Fernandes Silva /Programação 1, 2015.1
# Último índice

def ultimo_indice(num,lista):
	for i in range(len(lista)):
		if num == lista[i]:
			indice = i
	
	if num not in lista:
		indice = -1
	
	return indice
