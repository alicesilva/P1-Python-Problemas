#coding: utf-8

def senha(cadastro, usuario):
	lista = cadastro.keys()
	lista1 = cadastro.values()
	valor = -1
	for i in range(len(lista1)):
		for j in range(len(lista1[i])):
			if usuario == lista1[i][j]:
				valor = lista[i]
	return valor
