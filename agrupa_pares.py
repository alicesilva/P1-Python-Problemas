#coding: utf-8

def agrupa_pares_impares(lista):
	pares = []
	impares = []
	for i in range(len(lista)):
		if lista[i] % 2 == 0:
			pares.append(lista[i])
		else:
			impares.append(lista[i])
	
	
	dic = {}
	dic["impares"] = impares
	dic["pares"] = pares
	
	
	
	
	
	return dic


