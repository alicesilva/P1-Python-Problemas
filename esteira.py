#coding: utf-8
#Aluna: Alice Fernandes Silva / Programação 1, 2015
#questão: filtrando elementos em uma lista

def verifica_esteira(l1, l2):
	for i in range(len(l1)):
		for j in range(len(l2)):
			if l2[j] == l1[i]:
				return True
			else:
				return False
	
	if len(l1) == 0 or len(l2) == 0:
		return False

