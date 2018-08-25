#coding: utf-8
#Aluna: Alice Fernandes Silva / Programação 1, 2015
#questão: abaixo e acima

def organiza_por_media(lista):
	soma = 0
	for i in range(len(lista)):
		soma += lista[i]
	if len(lista) != 0:
		media = float(soma) / len(lista)
	
	maiores = []
	for i in range(len(lista)):
		if lista[i] > media:
			maiores.append(lista[i])
	
	for i in range(len(maiores)-1,-1,-1):
		for j in range(len(lista)-1,-1,-1):
			if lista[j] == maiores[i]:
				lista.pop(j)
	
	for i in range(len(maiores)):
		lista.append(maiores[i])
	
	return lista
	
	
	
