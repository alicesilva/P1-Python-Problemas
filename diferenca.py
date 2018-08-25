#coding: utf-8
#Aluna: Alice Fernandes Silva / Programação 1, 2015
#questão: diferença entre listas

def diferenca_listas(l1, l2):
	for i in range(len(l2)-1,-1,-1):
		for j in range(len(l1)-1,-1,-1):
			if l1[j] == l2[i]:
				l1.pop(j)



			
	
