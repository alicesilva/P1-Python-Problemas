#coding: utf-8
#Aluna: Alice Fernandes Silva / Programação 1, 2015
#questão: diagonais

def diagonais(M):
	nova_M = []
	cont = 0
	for i in range(len(M[0])):
		cont += 1
	p = []
	i = 0
	for k in range(0,cont):
		p.append(M[i][k])
		i += 1
	p1 = []
	i = 0
	for k in range(cont-1, -1,-1):
		p1.append(M[i][k])
		i += 1
	
	nova_M.append(p)
	nova_M.append(p1)
	
	return nova_M

