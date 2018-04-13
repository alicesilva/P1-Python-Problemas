# coding: utf-8
# Aluna: Alice Fernandes Silva / Programação 1, 2015
# Filtrando elementos em uma lista

def filtra_lista(num, lista):
	nova_lista = []
	for i in range(len(lista)):
		if i % num == 0:
			nova_lista.append(lista[i])
	
	return nova_lista
	
