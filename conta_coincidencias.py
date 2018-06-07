# coding: utf-8
# Aluna: Alice Fernandes Silva / Programação 1, 2015
# Conta coincidências

def conta_coincidencias(lista1, lista2):
	cont = 0
	for i in range(len(lista1)):
		for j in range(len(lista2)):
			if lista1[i] == lista2[j] and i == j:
				cont += 1
	
	return cont


numeros1 = raw_input()
numeros2 = raw_input()
lista1 = numeros1.split()
lista2 = numeros2.split()
print conta_coincidencias(lista1,lista2)
