#coding: utf-8
#Aluna: Alice Fernandes Silva / Programação 1, 2015
#questão: remove palavras com mais vogais

def remove_palavras_com_mais_vogais(lista):
	contadores = []
	for i in range(len(lista)):
		cont = 0
		for j in range(len(lista[i])):
			if lista[i][j] in "aeiouAEIOU":
				cont += 1
				
		contadores.append(cont)
	
	maior = contadores[0]
	for i in range(len(contadores)-1,-1,-1):
		if contadores[i] >= maior:
			maior = contadores[i]
	
	
	for i in range(len(contadores)-1,-1,-1):
		if contadores[i] == maior:
			lista.pop(i)


	
		
		

