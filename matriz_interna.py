#coding: utf-8
#Aluna: Alice Fernandes Silva / Programação 1, 2015
#questão: matriz interna

def soma_matriz_interna(matriz,inicio, fim):
	lista = []
	for k in range(inicio[0],fim[0]+1):
		 for l in range(inicio[1],fim[1]+1):
			  lista.append(matriz[k][l])
	
	soma = 0
	for i in range(len(lista)):
		soma += lista[i]
	return soma
					
				

