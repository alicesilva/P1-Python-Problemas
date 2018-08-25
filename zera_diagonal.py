#coding: utf-8
#Aluna: Alice Fernandes Silva / Programação 1, 2015
#questão: zera diagonal

def zera_diagonal(M):
	cont = 0
	for i in range(len(M)):
		cont += 1
	i = 0
	for j in range(0,cont):
		M[i][j] = 0
		i += 1
		
