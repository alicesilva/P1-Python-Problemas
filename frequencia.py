#coding: utf-8
#Aluna: Alice Fernandes Silva / Programação 1, 2015
#questão: frequência

def get_frequencia(lista):
	auxiliar = []
	for i in range(len(lista)):
		if lista[i] not in auxiliar:
			auxiliar.append(lista[i])
	
	contadores = []
	for i in range(len(auxiliar)):
		cont = 0
		for j in range(len(lista)):
			if auxiliar[i] == lista[j]:
				cont +=  1
		
		contadores.append(cont)
	
	return contadores
