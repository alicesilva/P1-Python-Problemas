#coding: utf-8
#Aluna: Alice Fernandes Silva / Programação 1, 2015
#questão: remove palavras com letras consecutivas

def remove_consecutivas(lista):
	remover = []
	for i in range(len(lista)):
		for j in range(len(lista[i])-1):
			if lista[i][j].lower() == lista[i][j+1].lower():
				remover.append(lista[i])
	
	for i in range(len(remover)-1,-1,-1):
		for j in range(len(lista)-1,-1,-1):
			if lista[j] == remover[i]:
				del lista[j]
