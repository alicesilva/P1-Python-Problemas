#coding: utf-8
#Aluna: Alice Fernandes Silva / Programação 1, 2015
#questão: squeeze

def squeeze(lista):
	for i in range(len(lista)-1,0,-1):
		if lista[i] == lista[i-1]:
			lista.pop(i-1)
	
	return lista


