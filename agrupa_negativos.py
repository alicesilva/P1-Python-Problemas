#coding: utf-8

def agrupa_negativos(lista):
	nao_negativos = []
	negativos = []
	for i in range(len(lista)):
		if lista[i] >= 0:
			nao_negativos.append(lista[i])
		else:
			negativos.append(lista[i])
	
	
	dic = {}
	dic["negativos"] = negativos
	dic["nao_negativos"] = nao_negativos
	
	
	
	
	
	return dic


