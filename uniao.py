#coding: utf-8
#Aluna: Alice Fernandes Silva / Programação 1, 2015
#questão: união de listas

def uniao_listas(l1,l2):
	for i in range(len(l2)):
		cont = 0
		for j in range(len(l1)):
			if l2[i] == l1[j]:
				cont += 1
		if cont == 0:
			l1.append(l2[i])

	for i in range(len(l1)-1,-1,-1):
		cont = 0
		for j in range(len(l1)-1,-1,-1):
			if l1[i] == l1[j]:
				cont += 1
		if cont > 1:
			l1.pop(i)
