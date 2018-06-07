# coding: utf-8
# Aluna: Alice Fernandes Silva / Programação 1, 2015
# Move impostor

def move_impostor(lista):
	impostor = lista[0]
	for i in range(1,len(lista)):
		if lista[i-1] > lista[i]:
			impostor = lista[i]
			lista[i-1],lista[i] = lista[i], lista[i-1]
	
	
	
	
	
