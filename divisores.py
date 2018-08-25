#coding: utf-8
#Aluna: Alice Fernandes Silva / Programação 1, 2015
#questão: seleciona divisores em uma lista

def filtra_divisores(lista):
	for i in range(len(lista)-1,-1,-1):
		lista_ele = str(lista[i])
		soma = 0
		for j in range(len(lista_ele)):
			soma += int(lista_ele[j])
		if lista[i] % soma != 0:
			lista.pop(i)
	
				
