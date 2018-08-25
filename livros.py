#coding: utf-8

def ausentes(livros):
	valores = livros.values()
	cont = 0
	for i in range(len(valores)):
		if valores[i] == 0:
			cont += 1
	return cont
