#coding: utf-8

def coluna(matriz,i):
	lista = []
	for j in range(len(matriz)):
		for k in range(len(matriz[j])):
			if k == i:
				lista.append(matriz[j][k])
	
	return lista

M = [[1,1,1,1],[2,2,2,2],[3,3,3,3]]
assert coluna(M,0) == [1,2,3]
assert coluna(M,1) == [1,2,3]
assert coluna(M,2) == [1,2,3]
assert coluna(M,3) == [1,2,3]
				
